"""Measure native ty release builds and paired runtime behavior at 16 and 1 CGUs."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import statistics
import subprocess
import time
from dataclasses import asdict
from pathlib import Path

import build_ty_pgo as pgo
import cgu_measurements as measure
import compare_codegen_runtime as runtime

HOLDOUT_PROJECTS = (
    pgo.EcosystemProject(
        name="black",
        repository="psf/black",
        revision="ce1897a8f20d0f64844dd666d07f4003500d0e09",
        source_directories=("src",),
        python_version="3.10",
    ),
    pgo.EcosystemProject(
        name="jinja",
        repository="pallets/jinja",
        revision="5ef70112a1ff19c05324ff889dd30405b1002044",
        source_directories=("src",),
        python_version="3.10",
    ),
)


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def capture(command, cwd, environment):
    return subprocess.run(
        command, cwd=cwd, env=environment, capture_output=True, text=True, check=True
    ).stdout.strip()


def describe_binary(path, environment):
    return {
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": hashlib.file_digest(path.open("rb"), "sha256").hexdigest(),
        "version": capture(
            [str(path), "version"], pgo.RUST_WORKSPACE_ROOT, environment
        ),
    }


def prepare_corpus(root, environment, *, runtime_only=False):
    training_projects = pgo.CORPUS_PROJECTS
    all_projects = (*training_projects, *HOLDOUT_PROJECTS)
    try:
        pgo.CORPUS_PROJECTS = all_projects
        paths = pgo.ecosystem_python_files(root / "corpus", environment=environment)
        interpreters = pgo.prepare_project_environments(
            root / "environments", root / "corpus", environment=environment
        )
    finally:
        pgo.CORPUS_PROJECTS = training_projects
    files = {
        str(Path(path).relative_to(root / "corpus")): hashlib.sha256(
            Path(path).read_bytes()
        ).hexdigest()
        for path in paths
    }
    python = {
        name: capture([str(path), "--version"], root, environment)
        for name, path in interpreters.items()
    }
    dependencies = {
        name: capture(["uv", "pip", "freeze", "--python", str(path)], root, environment)
        for name, path in interpreters.items()
    }
    save(
        root
        / "evidence"
        / ("corpus-runtime-only.json" if runtime_only else "corpus.json"),
        {
            "projects": [asdict(project) for project in all_projects],
            "held_out_from_training": [project.name for project in HOLDOUT_PROJECTS],
            "files": files,
            "python": python,
            "dependencies": dependencies,
            "note": "Both configurations train and run against these exact shared paths and environments.",
        },
    )
    if runtime_only:
        original = json.loads((root / "evidence" / "corpus.json").read_text())
        if (
            files != original["files"]
            or python != original["python"]
            or dependencies != original["dependencies"]
        ):
            raise RuntimeError(
                "Recovered runtime corpus or Python environments differ from the original build"
            )
    return interpreters, sum(
        Path(name).parts[0] not in {p.name for p in HOLDOUT_PROJECTS} for name in files
    )


def build(units, target, root, environment, interpreters, corpus_size):
    directory = root / f"cgu{units}"
    directory.mkdir(parents=True, exist_ok=True)
    profiles = directory / "profiles"
    profiles.mkdir(exist_ok=True)
    if any(profiles.iterdir()) or (directory / "instrumented").exists():
        raise RuntimeError(f"Build directory is not fresh: {directory}")
    executable = "ty.exe" if "windows" in target else "ty"
    environment = environment | {"CARGO_PROFILE_RELEASE_CODEGEN_UNITS": str(units)}
    instrumented_environment = environment | {
        "CARGO_TARGET_DIR": str(directory / "instrumented"),
        "RUSTFLAGS": pgo.append_flags(
            environment.get("RUSTFLAGS"), f"-Cprofile-generate={profiles}"
        ),
    }
    result = {"codegen_units": units}
    result["instrumented"] = measure.measure_build(
        pgo.cargo_command(target),
        cwd=pgo.RUST_WORKSPACE_ROOT,
        environment=instrumented_environment,
        output=root / "evidence" / f"cgu{units}-instrumented.json",
    )
    training_binary = directory / "instrumented" / target / "release" / executable
    result["instrumented_binary"] = describe_binary(training_binary, environment)
    started = time.perf_counter()
    raw = pgo.train_ty(
        training_binary,
        root / "corpus",
        profiles,
        corpus_size=corpus_size,
        project_environments=interpreters,
        environment=instrumented_environment,
    )
    result["training_elapsed_seconds"] = time.perf_counter() - started
    profiler = pgo.find_llvm_profdata(target, None)
    merged = directory / "ty.profdata"
    pgo.merge_profiles(profiler, raw, merged, environment=environment)
    hot_count = pgo.profile_hot_count(profiler, merged, environment=environment)
    result["profile_hot_count"] = hot_count
    result["profile_bytes"] = merged.stat().st_size
    optimized_environment = environment | {
        "CARGO_TARGET_DIR": str(directory / "optimized"),
        "RUSTFLAGS": pgo.append_flags(
            environment.get("RUSTFLAGS"),
            f"-Cprofile-use={merged} -Cllvm-args=--profile-summary-hot-count={hot_count}",
        ),
    }
    result["optimized"] = measure.measure_build(
        pgo.cargo_command(target),
        cwd=pgo.RUST_WORKSPACE_ROOT,
        environment=optimized_environment,
        output=root / "evidence" / f"cgu{units}-optimized.json",
    )
    binary = root / "binaries" / f"cgu{units}" / executable
    binary.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(directory / "optimized" / target / "release" / executable, binary)
    result["binary"] = describe_binary(binary, environment)
    save(root / "evidence" / f"cgu{units}-build.json", result)
    return binary


def compare_lsp(binaries, root, environment, repetitions, evidence):
    project = root / "runtime" / "language-server"
    runtime.prepare_language_server(project)
    expected = None
    samples = []
    for round_index in range(2):
        measure.wait_for_idle(evidence / f"lsp-idle-{round_index}.json")
        for pair in range(-2, repetitions):
            order = (16, 1) if (pair + round_index) % 2 == 0 else (1, 16)
            for units in order:
                result = runtime.language_server(binaries[units], project, environment)
                if expected is None:
                    expected = result["replies"]
                    save(evidence / "lsp-replies.json", expected)
                elif result["replies"] != expected:
                    save(
                        evidence / f"lsp-mismatch-cgu{units}.json",
                        result["replies"],
                    )
                    raise RuntimeError("Language-server replies differ")
                if pair >= 0:
                    sample = {
                        "round": round_index,
                        "pair": pair,
                        "codegen_units": units,
                        "elapsed_seconds": result["elapsed_seconds"],
                        "edit_seconds": result["edit_seconds"],
                    }
                    samples.append(sample)
                    with (evidence / "lsp-samples.jsonl").open(
                        "a", encoding="utf-8"
                    ) as stream:
                        stream.write(json.dumps(sample) + "\n")
        save(
            evidence / "lsp-comparison.json",
            {
                "samples": samples,
                "replies_match": True,
                "session_median_seconds": {
                    units: statistics.median(
                        s["elapsed_seconds"]
                        for s in samples
                        if s["codegen_units"] == units
                    )
                    for units in (16, 1)
                },
                "edits_median_seconds": {
                    units: statistics.median(
                        sum(s["edit_seconds"])
                        for s in samples
                        if s["codegen_units"] == units
                    )
                    for units in (16, 1)
                },
            },
        )


def compare_runtime(
    binaries, root, environment, interpreters, repetitions, evidence, selected_cases
):
    for variable in pgo.EXCLUDED_ENVIRONMENT_VARIABLES:
        environment.pop(variable, None)
    environment.update({"NO_COLOR": "1", "UV_OFFLINE": "1", "PYTHONHASHSEED": "0"})
    for variable in ("TY_MAX_PARALLELISM", "RAYON_NUM_THREADS"):
        environment.pop(variable, None)
    cases = [
        ("startup-version", ["version"], environment),
        ("startup-help", ["--help"], environment),
    ]
    for project in (*pgo.CORPUS_PROJECTS, *HOLDOUT_PROJECTS):
        checkout = root / "corpus" / project.name
        arguments = [
            "check",
            "--python",
            str(interpreters[project.name]),
            "--project",
            str(checkout),
            "--python-version",
            project.python_version,
            *(
                argument
                for directory in sorted(pgo.EXCLUDED_DIRECTORIES)
                for argument in ("--exclude", f"{directory}/")
            ),
            "--exit-zero",
            "--no-progress",
            "--color",
            "never",
            "--output-format",
            "concise",
            *(str(checkout / source) for source in project.source_directories),
        ]
        cases.append((f"check-{project.name}", arguments, environment))
        if project.name in ("black", "warehouse"):
            cases.append(
                (
                    f"check-{project.name}-single-thread",
                    arguments,
                    environment | {"TY_MAX_PARALLELISM": "1", "RAYON_NUM_THREADS": "1"},
                )
            )
    unknown = selected_cases - {name for name, _, _ in cases} - {"language-server"}
    if unknown:
        raise RuntimeError(f"Unknown runtime cases: {sorted(unknown)}")
    for round_index in range(2):
        measure.wait_for_idle(evidence / f"runtime-idle-{round_index}.json")
        for name, arguments, case_environment in cases:
            if selected_cases and name not in selected_cases:
                continue
            measure.compare_commands(
                name=name,
                baseline=[str(binaries[16]), *arguments],
                candidate=[str(binaries[1]), *arguments],
                cwd=root,
                environment=case_environment,
                output=evidence / f"runtime-{name}-round{round_index}.json",
                repetitions=repetitions,
                warmups=2,
            )
    if not selected_cases or "language-server" in selected_cases:
        compare_lsp(binaries, root, environment, repetitions, evidence)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--runtime-only", action="store_true")
    parser.add_argument(
        "--cases",
        default="",
        help="Comma-separated runtime case names; empty runs all cases",
    )
    parser.add_argument("--repetitions", type=int, default=30)
    args = parser.parse_args()
    root = args.output.resolve()
    root.mkdir(parents=True, exist_ok=True)
    if args.target != pgo.rustc_host():
        raise RuntimeError("Benchmarks require a native target")
    environment = os.environ.copy()
    for variable in (
        "RUSTC_WRAPPER",
        "RUSTC_WORKSPACE_WRAPPER",
        "CARGO_ENCODED_RUSTFLAGS",
        "CARGO_PROFILE_RELEASE_CODEGEN_UNITS",
    ):
        environment.pop(variable, None)
    environment.update({"CARGO_INCREMENTAL": "0", "CARGO_NET_RETRY": "10"})
    if args.target.endswith("-apple-darwin"):
        environment.update(
            {
                "MACOSX_DEPLOYMENT_TARGET": "11.0",
                "RUSTFLAGS": "-C linker=rust-lld -C linker-flavor=ld64.lld -C link-arg=--icf=safe",
                "CFLAGS": "-fno-profile-generate -fno-profile-use",
                "CXXFLAGS": "-fno-profile-generate -fno-profile-use",
            }
        )
    elif "windows" in args.target:
        environment["RUSTFLAGS"] = "-C target-feature=+crt-static"
    else:
        environment["RUSTFLAGS"] = ""
    save(
        root
        / "evidence"
        / ("context-runtime-only.json" if args.runtime_only else "context.json"),
        {
            "host": measure.host_context(),
            "target": args.target,
            "source_revision": capture(
                ["git", "rev-parse", "HEAD"], pgo.RUST_WORKSPACE_ROOT, environment
            ),
            "experiment_revision": capture(
                ["git", "rev-parse", "HEAD"], pgo.REPOSITORY_ROOT, environment
            ),
            "rustc": capture(["rustc", "-Vv"], pgo.RUST_WORKSPACE_ROOT, environment),
            "cargo": capture(["cargo", "-V"], pgo.RUST_WORKSPACE_ROOT, environment),
            "flags": {
                key: value
                for key, value in environment.items()
                if key in ("RUSTFLAGS", "CARGO_INCREMENTAL", "MACOSX_DEPLOYMENT_TARGET")
            },
            "limitations": [
                "One clean build per configuration in order 16 then 1; OS page-cache and build-order effects are not controlled.",
                "Native Linux cargo builds use the runner's glibc rather than the release manylinux packaging container.",
                "Runtime: two rounds of alternating pairs on an idle host; corpus and environments are shared unchanged between binaries.",
            ],
        },
    )
    interpreters, corpus_size = prepare_corpus(
        root, environment, runtime_only=args.runtime_only
    )
    executable = "ty.exe" if "windows" in args.target else "ty"
    if args.runtime_only:
        binaries = {
            units: root / "binaries" / f"cgu{units}" / executable for units in (16, 1)
        }
        for units, binary in binaries.items():
            metadata = json.loads(
                (root / "evidence" / f"cgu{units}-build.json").read_text()
            )
            with binary.open("rb") as stream:
                actual = hashlib.file_digest(stream, "sha256").hexdigest()
            if actual != metadata["binary"]["sha256"]:
                raise RuntimeError(
                    f"Downloaded CGU{units} binary digest differs from build evidence"
                )
            if os.name != "nt":
                binary.chmod(binary.stat().st_mode | 0o111)
    else:
        pgo.run(
            ["cargo", "fetch", "--locked", "--target", args.target],
            environment=environment,
        )
        binaries = {
            units: build(
                units, args.target, root, environment, interpreters, corpus_size
            )
            for units in (16, 1)
        }
    if (
        describe_binary(binaries[16], environment)["version"]
        != describe_binary(binaries[1], environment)["version"]
    ):
        raise RuntimeError("Binary versions differ")
    evidence = root / "evidence"
    if args.runtime_only:
        evidence /= "runtime-only-" + os.environ.get(
            "GITHUB_RUN_ID", str(time.time_ns())
        )
    evidence.mkdir(parents=True, exist_ok=True)
    compare_runtime(
        binaries,
        root,
        environment,
        interpreters,
        args.repetitions,
        evidence,
        {name for name in args.cases.split(",") if name},
    )


if __name__ == "__main__":
    main()
