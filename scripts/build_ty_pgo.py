#!/usr/bin/env python3
"""Build ty with profile-guided optimization using pinned ecosystem projects."""

from __future__ import annotations

import argparse
import json
import os
import selectors
import shlex
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
RUST_WORKSPACE_ROOT = REPOSITORY_ROOT / "ruff"
EXCLUDED_DIRECTORIES = frozenset({"_tests", "_vendor", "test", "tests"})


@dataclass(frozen=True)
class EcosystemProject:
    name: str
    repository: str
    revision: str
    source_directories: tuple[str, ...]


CORPUS_PROJECTS = (
    EcosystemProject(
        name="pytest",
        repository="pytest-dev/pytest",
        revision="28e86a6c2ae0173831e4925a4af89b02a2936d09",
        source_directories=("src/_pytest",),
    ),
    EcosystemProject(
        name="httpx",
        repository="encode/httpx",
        revision="b5addb64f0161ff6bfe94c124ef76f6a1fba5254",
        source_directories=("httpx",),
    ),
    EcosystemProject(
        name="fastapi",
        repository="fastapi/fastapi",
        revision="a375f6b948b99fa4260129856bbf11d037f363ef",
        source_directories=("fastapi",),
    ),
    EcosystemProject(
        name="anyio",
        repository="agronholm/anyio",
        revision="ffe91331adb912c5d150f5d373f7cd28a0e96a62",
        source_directories=("src/anyio",),
    ),
    EcosystemProject(
        name="pip",
        repository="pypa/pip",
        revision="d1fd55753405fd728a0751a578e27c1054acdf48",
        source_directories=("src/pip/_internal",),
    ),
    EcosystemProject(
        name="sphinx",
        repository="sphinx-doc/sphinx",
        revision="b06d92e80eed130e1dd4e67cac4afa1267424f1a",
        source_directories=(
            "sphinx/builders",
            "sphinx/ext/autodoc",
            "sphinx/domains/python",
        ),
    ),
    EcosystemProject(
        name="astropy",
        repository="astropy/astropy",
        revision="b779108c7cec25c840c0f744fdf2a1550441e309",
        source_directories=("astropy/units",),
    ),
    EcosystemProject(
        name="typeshed",
        repository="python/typeshed",
        revision="e0efbeef901e9b6998d016e1ab9352678f09ae77",
        source_directories=(
            "stdlib/asyncio",
            "stdlib/collections",
            "stubs/requests",
        ),
    ),
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", help="Host-native Rust target triple")
    parser.add_argument(
        "--target-dir",
        type=Path,
        help="Cargo target directory (default: CARGO_TARGET_DIR or ruff/target/ty-pgo)",
    )
    parser.add_argument(
        "--profile-dir",
        type=Path,
        help="Raw profile directory (default: <target-dir>/profiles)",
    )
    parser.add_argument(
        "--llvm-profdata",
        type=Path,
        help="Override the active Rust toolchain's llvm-profdata executable",
    )
    parser.add_argument(
        "--train-only",
        action="store_true",
        help="Only produce <target-dir>/ty.profdata for a subsequent release build",
    )
    parser.add_argument(
        "--prepare-corpus",
        action="store_true",
        help="Only download and prepare the pinned ecosystem training corpus",
    )
    args = parser.parse_args()

    if args.prepare_corpus and args.train_only:
        parser.error("--prepare-corpus and --train-only cannot be used together")

    target_dir = (
        args.target_dir
        or Path(
            os.environ.get(
                "CARGO_TARGET_DIR", RUST_WORKSPACE_ROOT / "target" / "ty-pgo"
            )
        )
    ).resolve()
    profile_dir = (args.profile_dir or target_dir / "profiles").resolve()
    merged_profile = target_dir / "ty.profdata"

    environment = os.environ.copy()
    if args.prepare_corpus:
        corpus = ecosystem_python_files(target_dir / "corpus", environment=environment)
        print(f"Prepared {len(corpus)} ecosystem Python files", flush=True)
        return

    host = rustc_host()
    target = args.target or host
    if target != host:
        parser.error(
            f"PGO training requires the host-native target {host}, got {target}"
        )

    profiler = find_llvm_profdata(host, args.llvm_profdata)
    corpus = ecosystem_python_files(target_dir / "corpus", environment=environment)

    profile_dir.mkdir(parents=True, exist_ok=True)
    for profile in profile_dir.glob("ty-*.profraw"):
        profile.unlink()

    environment["CARGO_INCREMENTAL"] = "0"
    if target.endswith("-apple-darwin"):
        for variable in ("CFLAGS", "CXXFLAGS"):
            environment[variable] = append_flags(
                environment.get(variable), "-fno-profile-generate -fno-profile-use"
            )

    instrumented_target_dir = target_dir / "instrumented"
    instrumented_environment = environment | {
        "CARGO_TARGET_DIR": str(instrumented_target_dir),
        "RUSTFLAGS": append_flags(
            environment.get("RUSTFLAGS"), f"-Cprofile-generate={profile_dir}"
        ),
    }
    print("Building instrumented release ty", flush=True)
    run(cargo_command(target), environment=instrumented_environment)

    binary_name = "ty.exe" if "windows" in target else "ty"
    instrumented_binary = instrumented_target_dir / target / "release" / binary_name
    if not instrumented_binary.is_file():
        raise RuntimeError(f"Instrumented ty binary not found: {instrumented_binary}")

    print(f"Training on {len(corpus)} ecosystem Python files", flush=True)
    for project in CORPUS_PROJECTS:
        checkout = target_dir / "corpus" / project.name
        training_environment = instrumented_environment | {
            "LLVM_PROFILE_FILE": str(profile_dir / f"ty-{project.name}-%m-%p.profraw")
        }
        for variable in (
            "CONDA_PREFIX",
            "PYTHONPATH",
            "TY_CONFIG_FILE",
            "TY_LOG",
            "TY_OUTPUT_FORMAT",
            "VIRTUAL_ENV",
        ):
            training_environment.pop(variable, None)

        print(f"Profiling ty on {project.name}", flush=True)
        run(
            [
                str(instrumented_binary),
                "check",
                "--project",
                str(checkout),
                "--python-version",
                "3.13",
                "--python-platform",
                "linux",
                *(
                    argument
                    for directory in sorted(EXCLUDED_DIRECTORIES)
                    for argument in ("--exclude", f"{directory}/")
                ),
                "--exit-zero",
                "--no-progress",
                "-qq",
                *(str(checkout / source) for source in project.source_directories),
            ],
            environment=training_environment,
        )

    profile_language_server(instrumented_binary, profile_dir, instrumented_environment)

    profiles = sorted(profile_dir.glob("ty-*.profraw"))
    missing_workloads = [
        name
        for name in (*(project.name for project in CORPUS_PROJECTS), "language-server")
        if not list(profile_dir.glob(f"ty-{name}-*.profraw"))
    ]
    if missing_workloads or any(profile.stat().st_size == 0 for profile in profiles):
        raise RuntimeError(
            f"Incomplete ty profiling data in {profile_dir}; "
            f"missing workloads: {', '.join(missing_workloads) or 'none'}"
        )

    with tempfile.NamedTemporaryFile(
        dir=target_dir, prefix="ty-", suffix=".profdata", delete=False
    ) as temporary_file:
        temporary_profile = Path(temporary_file.name)
    try:
        run(
            [
                str(profiler),
                "merge",
                "--output",
                str(temporary_profile),
                *map(str, profiles),
            ],
            environment=environment,
        )
        temporary_profile.replace(merged_profile)
    finally:
        temporary_profile.unlink(missing_ok=True)
    print(f"Merged PGO profile: {merged_profile}", flush=True)

    if args.train_only:
        return

    optimized_environment = environment | {
        "CARGO_TARGET_DIR": str(target_dir),
        "RUSTFLAGS": append_flags(
            environment.get("RUSTFLAGS"), f"-Cprofile-use={merged_profile}"
        ),
    }
    print("Building optimized release ty", flush=True)
    run(cargo_command(target), environment=optimized_environment)
    print(f"Optimized ty: {target_dir / target / 'release' / binary_name}", flush=True)


def profile_language_server(
    binary: Path, profile_directory: Path, environment: dict[str, str]
) -> None:
    print("Profiling ty language-server incremental edits", flush=True)
    server_environment = environment | {
        "LLVM_PROFILE_FILE": str(profile_directory / "ty-language-server-%m-%p.profraw")
    }
    for variable in (
        "CONDA_PREFIX",
        "PYTHONPATH",
        "TY_CONFIG_FILE",
        "TY_LOG",
        "TY_LOG_PROFILE",
        "TY_OUTPUT_FORMAT",
        "TY_UV",
        "UV",
        "VIRTUAL_ENV",
    ):
        server_environment.pop(variable, None)

    with tempfile.TemporaryDirectory(
        prefix="ty-pgo-language-server-", dir=profile_directory.parent
    ) as temporary:
        root = Path(temporary)
        (root / "pyproject.toml").write_text(
            '[project]\nname = "ty-pgo"\nversion = "0.0.0"\n'
            'requires-python = ">=3.12"\n',
            encoding="utf-8",
        )
        models = root / "models.py"
        models_text = (
            "from dataclasses import dataclass\n\n"
            "@dataclass\nclass User:\n    name: str\n    age: int\n\n"
            'def load_user() -> User:\n    return User("Ada", 37)\n'
        )
        models.write_text(models_text, encoding="utf-8")
        service = root / "service.py"
        service_text = (
            "from models import User, load_user\n\n"
            "def describe(user: User) -> str:\n    return user.name.upper()\n\n"
            "user = load_user()\nresult = describe(user)\n"
            "next_age = user.age + 1\n"
        )
        service.write_text(service_text, encoding="utf-8")

        process = subprocess.Popen(
            [str(binary), "server"],
            cwd=root,
            env=server_environment,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=0,
        )
        if process.stdin is None or process.stdout is None or process.stderr is None:
            process.kill()
            process.wait()
            raise RuntimeError("Could not open language-server pipes")

        selector = selectors.DefaultSelector()
        selector.register(process.stdout, selectors.EVENT_READ)
        request_id = 0

        def send(message: dict[str, object]) -> None:
            payload = json.dumps(message, separators=(",", ":")).encode("utf-8")
            process.stdin.write(
                f"Content-Length: {len(payload)}\r\n\r\n".encode("ascii")
            )
            process.stdin.write(payload)

        def request(method: str, params: dict[str, object] | None = None) -> object:
            nonlocal request_id
            request_id += 1
            identifier = request_id
            send(
                {"jsonrpc": "2.0", "id": identifier, "method": method, "params": params}
            )
            deadline = time.monotonic() + 15
            while True:
                headers: dict[str, str] = {}
                while True:
                    if not selector.select(max(0, deadline - time.monotonic())):
                        raise TimeoutError(
                            f"Language-server request timed out: {method}"
                        )
                    line = process.stdout.readline()
                    if not line:
                        raise RuntimeError("Language server closed its output")
                    if line in (b"\r\n", b"\n"):
                        break
                    name, _, value = line.decode("ascii").partition(":")
                    headers[name.lower()] = value.strip()

                remaining = int(headers["content-length"])
                chunks: list[bytes] = []
                while remaining:
                    if not selector.select(max(0, deadline - time.monotonic())):
                        raise TimeoutError(
                            f"Language-server response timed out: {method}"
                        )
                    chunk = process.stdout.read(remaining)
                    if not chunk:
                        raise RuntimeError("Language server closed its output")
                    chunks.append(chunk)
                    remaining -= len(chunk)
                response = json.loads(b"".join(chunks))
                if "method" in response and "id" in response:
                    result = (
                        [] if response["method"] == "workspace/configuration" else None
                    )
                    send({"jsonrpc": "2.0", "id": response["id"], "result": result})
                elif response.get("id") == identifier:
                    if "error" in response:
                        raise RuntimeError(f"{method} failed: {response['error']}")
                    return response.get("result")

        def notify(method: str, params: dict[str, object] | None = None) -> None:
            send({"jsonrpc": "2.0", "method": method, "params": params or {}})

        def diagnostics(path: Path) -> list[object]:
            result = request(
                "textDocument/diagnostic", {"textDocument": {"uri": path.as_uri()}}
            )
            if not isinstance(result, dict):
                raise RuntimeError("Expected a full document diagnostic report")
            return result.get("items", [])

        try:
            initialized = request(
                "initialize",
                {
                    "processId": os.getpid(),
                    "rootUri": root.as_uri(),
                    "workspaceFolders": [{"uri": root.as_uri(), "name": root.name}],
                    "capabilities": {
                        "workspace": {"configuration": False},
                        "textDocument": {"diagnostic": {"dynamicRegistration": False}},
                    },
                },
            )
            if not isinstance(initialized, dict) or not initialized.get(
                "capabilities", {}
            ).get("diagnosticProvider"):
                raise RuntimeError("Language server does not support pull diagnostics")
            notify("initialized")

            for path, text in ((models, models_text), (service, service_text)):
                notify(
                    "textDocument/didOpen",
                    {
                        "textDocument": {
                            "uri": path.as_uri(),
                            "languageId": "python",
                            "version": 1,
                            "text": text,
                        }
                    },
                )
            if diagnostics(models) or diagnostics(service):
                raise RuntimeError("Expected clean initial language-server diagnostics")

            for method, position in (
                ("textDocument/hover", {"line": 7, "character": 17}),
                ("textDocument/definition", {"line": 5, "character": 8}),
                ("textDocument/completion", {"line": 5, "character": 16}),
            ):
                result = request(
                    method,
                    {"textDocument": {"uri": service.as_uri()}, "position": position},
                )
                if not result:
                    raise RuntimeError(f"Expected a nonempty {method} result")

            for index in range(12):
                invalid = index % 2 == 0
                changed = (
                    models_text.replace("age: int", "age: str")
                    if invalid
                    else models_text
                )
                notify(
                    "textDocument/didChange",
                    {
                        "textDocument": {
                            "uri": models.as_uri(),
                            "version": index + 2,
                        },
                        "contentChanges": [{"text": changed}],
                    },
                )
                if (
                    bool(diagnostics(models)) != invalid
                    or bool(diagnostics(service)) != invalid
                ):
                    raise RuntimeError(
                        "Incremental cross-file diagnostics did not update"
                    )

            request("shutdown")
            notify("exit")
            process.stdin.close()
            if process.wait(timeout=10):
                raise RuntimeError(
                    process.stderr.read().decode("utf-8", errors="replace")
                )
        finally:
            selector.close()
            if process.poll() is None:
                process.kill()
                process.wait()


def rustc_host() -> str:
    version = subprocess.run(
        ["rustc", "--version", "--verbose"],
        cwd=RUST_WORKSPACE_ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    for line in version.splitlines():
        if line.startswith("host: "):
            return line.removeprefix("host: ")
    raise RuntimeError("Could not determine the active Rust compiler's host target")


def find_llvm_profdata(host: str, override: Path | None) -> Path:
    if override is not None:
        profiler = override.resolve()
    else:
        sysroot = subprocess.run(
            ["rustc", "--print", "sysroot"],
            cwd=RUST_WORKSPACE_ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        binary_name = "llvm-profdata.exe" if "windows" in host else "llvm-profdata"
        profiler = Path(sysroot) / "lib" / "rustlib" / host / "bin" / binary_name

    if not profiler.is_file() or not os.access(profiler, os.X_OK):
        raise RuntimeError(
            f"Rust toolchain llvm-profdata not found: {profiler}; "
            "run `rustup component add llvm-tools-preview`"
        )
    return profiler


def ecosystem_python_files(
    corpus_directory: Path, *, environment: dict[str, str]
) -> list[str]:
    corpus_directory.mkdir(parents=True, exist_ok=True)
    git_environment = environment | {
        "GIT_CONFIG_GLOBAL": os.devnull,
        "GIT_TERMINAL_PROMPT": "0",
        "GIT_LFS_SKIP_SMUDGE": "1",
    }
    paths: list[str] = []

    for project in CORPUS_PROJECTS:
        checkout = corpus_directory / project.name
        checkout.mkdir(parents=True, exist_ok=True)
        git = ["git", "-c", f"core.hooksPath={os.devnull}", "-C", str(checkout)]

        if not (checkout / ".git").is_dir():
            print(f"Preparing {project.repository}@{project.revision}", flush=True)
            run([*git, "init", "--quiet"], environment=git_environment)
            run(
                [
                    *git,
                    "remote",
                    "add",
                    "origin",
                    f"https://github.com/{project.repository}.git",
                ],
                environment=git_environment,
            )

        run(
            [*git, "sparse-checkout", "set", "--cone", *project.source_directories],
            environment=git_environment,
        )

        current_revision = subprocess.run(
            [*git, "rev-parse", "--verify", "HEAD"],
            cwd=REPOSITORY_ROOT,
            env=git_environment,
            check=False,
            capture_output=True,
            text=True,
        )
        if (
            current_revision.returncode != 0
            or current_revision.stdout.strip() != project.revision
        ):
            run_git_with_retry(
                [
                    *git,
                    "fetch",
                    "--quiet",
                    "--no-tags",
                    "--no-recurse-submodules",
                    "--depth=1",
                    "--filter=blob:none",
                    "origin",
                    project.revision,
                ],
                environment=git_environment,
            )

        run_git_with_retry(
            [
                *git,
                "checkout",
                "--quiet",
                "--detach",
                "--force",
                "--no-recurse-submodules",
                project.revision,
            ],
            environment=git_environment,
        )

        for source_directory in project.source_directories:
            source = checkout / source_directory
            if not source.is_dir():
                raise RuntimeError(
                    f"Missing training source directory {source_directory!r} "
                    f"in {project.repository}@{project.revision}"
                )

        tracked_files = subprocess.run(
            [*git, "ls-files", "-z", "--", *project.source_directories],
            cwd=REPOSITORY_ROOT,
            env=git_environment,
            check=True,
            capture_output=True,
        ).stdout.split(b"\0")
        project_paths = [
            str(path)
            for tracked_file in tracked_files
            if tracked_file
            and (path := checkout / os.fsdecode(tracked_file)).suffix in {".py", ".pyi"}
            and path.is_file()
            and not path.is_symlink()
            and not EXCLUDED_DIRECTORIES.intersection(
                path.relative_to(checkout).parts[:-1]
            )
        ]

        if not project_paths:
            raise RuntimeError(
                f"No Python training files found in {project.repository}"
            )
        paths.extend(sorted(project_paths))
        print(f"  {project.name}: {len(project_paths)} Python files", flush=True)

    return paths


def run_git_with_retry(command: list[str], *, environment: dict[str, str]) -> None:
    for attempt in range(3):
        try:
            run(command, environment=environment)
            return
        except subprocess.CalledProcessError:
            if attempt == 2:
                raise
            delay = 2**attempt
            print(
                f"Git command failed; retrying in {delay}s (attempt {attempt + 2} of 3)",
                file=sys.stderr,
                flush=True,
            )
            time.sleep(delay)


def cargo_command(target: str) -> list[str]:
    return [
        "cargo",
        "rustc",
        "--release",
        "--locked",
        "--package",
        "ty",
        "--bin",
        "ty",
        "--target",
        target,
        "--",
        "-C",
        "strip=symbols",
    ]


def append_flags(existing: str | None, additional: str) -> str:
    return " ".join(flag for flag in (existing, additional) if flag)


def run(
    command: list[str],
    *,
    environment: dict[str, str],
    allowed_exit_codes: tuple[int, ...] = (0,),
) -> None:
    logged_arguments = 16
    displayed_command = shlex.join(command[:logged_arguments])
    if len(command) > logged_arguments:
        displayed_command += (
            f" ... ({len(command) - logged_arguments} arguments omitted)"
        )
    print(f"> {displayed_command}", flush=True)
    completed = subprocess.run(
        command, cwd=RUST_WORKSPACE_ROOT, env=environment, check=False
    )
    if completed.returncode not in allowed_exit_codes:
        raise subprocess.CalledProcessError(completed.returncode, command)


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1) from error
