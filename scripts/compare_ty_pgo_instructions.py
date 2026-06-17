from __future__ import annotations

import argparse
import json
import logging
import os
import shlex
import shutil
import subprocess
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import median
from typing import Any

from ecosystem_analyzer.installed_project import InstalledProject
from ecosystem_analyzer.manager import Manager, get_ecosystem_projects

RUFF_DIR = Path("ruff")
TY_MAX_PARALLELISM = "8"
EXPECTED_TY_EXIT_CODES = {0, 1}


@dataclass(frozen=True)
class Comparison:
    name: str
    release: int
    pgo_release: int

    @property
    def delta_percent(self) -> float:
        return (self.pgo_release - self.release) / self.release * 100

    @property
    def speedup(self) -> float:
        return self.release / self.pgo_release


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compare release and PGO ty retired instructions with eight ty threads."
    )
    parser.add_argument(
        "--release-ty",
        type=Path,
        default=Path("ruff/target/ty-pgo-benchmark/release/release/ty"),
    )
    parser.add_argument(
        "--pgo-ty",
        type=Path,
        default=Path("ruff/target/ty-pgo-benchmark/pgo/release/ty"),
    )
    parser.add_argument(
        "--perf",
        type=Path,
        default=Path("perf"),
        help="Path to a perf binary with access to instructions:u.",
    )
    parser.add_argument(
        "--exclude-newer",
        default=subprocess.check_output(
            [
                "git",
                "-C",
                RUFF_DIR.as_posix(),
                "show",
                "--no-ext-diff",
                "--format=%cI",
                "--no-patch",
                "HEAD",
            ],
            text=True,
        ).strip(),
    )
    parser.add_argument(
        "--runs",
        type=int,
        default=1,
        help="Instruction counts are stable; increase only to take medians.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("ruff/target/ty-pgo-benchmark/instructions.json"),
    )
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    if args.runs < 1:
        parser.error("--runs must be at least one")

    release_ty = args.release_ty.resolve()
    pgo_ty = args.pgo_ty.resolve()
    for binary in (release_ty, pgo_ty):
        if not binary.is_file():
            parser.error(f"ty binary does not exist: {binary}")

    perf = resolve_perf(args.perf)
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    config_home = output.parent / "config"
    cache_home = output.parent / "cache"
    (config_home / "ty").mkdir(parents=True, exist_ok=True)
    (config_home / "ty" / "ty.toml").write_text(
        (RUFF_DIR / ".github/ty-ecosystem.toml").read_text()
    )

    env = os.environ.copy()
    env["TY_MAX_PARALLELISM"] = TY_MAX_PARALLELISM
    env["UV_EXCLUDE_NEWER"] = args.exclude_newer
    env["XDG_CACHE_HOME"] = cache_home.as_posix()
    env["XDG_CONFIG_HOME"] = config_home.as_posix()
    check_perf(perf, env)

    temporary_environment = {
        name: env[name]
        for name in ("UV_EXCLUDE_NEWER", "XDG_CACHE_HOME", "XDG_CONFIG_HOME")
    }
    previous_environment = {
        name: os.environ.get(name) for name in temporary_environment
    }
    os.environ.update(temporary_environment)
    try:
        ecosystem = compare_ecosystem(
            release_ty=release_ty,
            pgo_ty=pgo_ty,
            perf=perf,
            runs=args.runs,
            env=env,
        )
    finally:
        for name, value in previous_environment.items():
            if value is None:
                os.environ.pop(name, None)
            else:
                os.environ[name] = value

    payload = {
        "ty_max_parallelism": int(TY_MAX_PARALLELISM),
        "ecosystem": comparison_payload(ecosystem),
    }
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print_summary("ecosystem", ecosystem)
    print(f"Wrote {output}")


def resolve_perf(perf: Path) -> Path:
    if perf.is_file():
        return perf.resolve()

    resolved = shutil.which(perf.as_posix())
    if resolved is None:
        raise SystemExit(f"perf binary not found: {perf}")
    return Path(resolved).resolve()


def check_perf(perf: Path, env: dict[str, str]) -> None:
    try:
        measure_instructions(command=["true"], cwd=Path.cwd(), perf=perf, env=env)
    except RuntimeError as error:
        raise SystemExit(f"perf cannot count instructions:u:\n{error}") from error


def compare_ecosystem(
    *,
    release_ty: Path,
    pgo_ty: Path,
    perf: Path,
    runs: int,
    env: dict[str, str],
) -> list[Comparison]:
    projects = get_ecosystem_projects()
    manager = Manager(
        ty_repo=None,
        target_dir=None,
        project_names=sorted(projects),
        profile="release",
        flaky_runs=1,
        exclude_newer=None,
        ecosystem_projects=projects,
    )
    manager._ensure_installed()
    installed_projects = sorted(
        manager._installed_projects, key=lambda project: project.name
    )

    return [
        compare_command(
            name=project.name,
            release_command=ecosystem_command(release_ty, project),
            pgo_command=ecosystem_command(pgo_ty, project),
            cwd=project.root_directory,
            perf=perf,
            runs=runs,
            env=env,
        )
        for project in installed_projects
    ]


def ecosystem_command(binary: Path, project: InstalledProject) -> list[str]:
    standard_flags = [
        "--output-format=concise",
        "--python",
        str(project.venv_path),
    ]
    if project.ty_cmd:
        command = []
        for part in shlex.split(project.ty_cmd):
            if part == "{ty}":
                command.append(binary.as_posix())
            elif part == "{paths}":
                command.extend(project.paths)
            else:
                command.append(part)
        command.extend(standard_flags)
        return command

    return [binary.as_posix(), "check", *standard_flags, *project.paths]


def compare_command(
    *,
    name: str,
    release_command: list[str],
    pgo_command: list[str],
    cwd: Path,
    perf: Path,
    runs: int,
    env: dict[str, str],
) -> Comparison:
    logging.info("Counting instructions for %s", name)
    release = measure_median(
        command=release_command, cwd=cwd, perf=perf, runs=runs, env=env
    )
    pgo_release = measure_median(
        command=pgo_command, cwd=cwd, perf=perf, runs=runs, env=env
    )
    return Comparison(name=name, release=release, pgo_release=pgo_release)


def measure_median(
    *, command: list[str], cwd: Path, perf: Path, runs: int, env: dict[str, str]
) -> int:
    return int(
        median(
            measure_instructions(command=command, cwd=cwd, perf=perf, env=env)
            for _ in range(runs)
        )
    )


def measure_instructions(
    *, command: list[str], cwd: Path, perf: Path, env: dict[str, str]
) -> int:
    with tempfile.NamedTemporaryFile() as perf_output:
        result = subprocess.run(
            [
                perf.as_posix(),
                "stat",
                "--no-big-num",
                "-x",
                "\t",
                "-e",
                "instructions:u",
                "--output",
                perf_output.name,
                "--",
                *command,
            ],
            cwd=cwd,
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if result.returncode not in EXPECTED_TY_EXIT_CODES:
            raise RuntimeError(
                f"perf failed for {shlex.join(command)} with exit code {result.returncode}:\n"
                f"{result.stderr}"
            )

        for line in Path(perf_output.name).read_text().splitlines():
            fields = line.split("\t")
            if len(fields) >= 3 and fields[2] == "instructions:u":
                return int(fields[0])

    raise RuntimeError(f"perf did not report instructions for {shlex.join(command)}")


def comparison_payload(comparisons: list[Comparison]) -> dict[str, Any]:
    release = sum(comparison.release for comparison in comparisons)
    pgo_release = sum(comparison.pgo_release for comparison in comparisons)
    return {
        "summary": {
            "projects": len(comparisons),
            "release": release,
            "pgo_release": pgo_release,
            "delta_percent": (pgo_release - release) / release * 100,
            "speedup": release / pgo_release,
        },
        "projects": [
            asdict(comparison)
            | {
                "delta_percent": comparison.delta_percent,
                "speedup": comparison.speedup,
            }
            for comparison in comparisons
        ],
    }


def print_summary(name: str, comparisons: list[Comparison]) -> None:
    summary = comparison_payload(comparisons)["summary"]
    print(
        f"{name}: release={summary['release']:,} instructions, "
        f"pgo-release={summary['pgo_release']:,} instructions, "
        f"delta={summary['delta_percent']:+.2f}%, "
        f"speedup={summary['speedup']:.3f}x"
    )


if __name__ == "__main__":
    main()
