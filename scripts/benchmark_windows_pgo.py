"""Compare production Windows ty binaries on independent, pinned projects."""

# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

from __future__ import annotations

import argparse
import ctypes
import hashlib
import itertools
import json
import os
import platform
import queue
import re
import shutil
import statistics
import subprocess
import sys
import threading
import time
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True, slots=True)
class IncrementalEdit:
    edited_file: str
    affected_files: tuple[str, ...]
    original: str
    replacement: str


@dataclass(frozen=True, slots=True)
class Project:
    name: str
    repository: str
    revision: str
    source: str
    edit: IncrementalEdit | None = None

    def __post_init__(self) -> None:
        if re.fullmatch(r"[0-9a-f]{40}", self.revision) is None:
            raise ValueError(f"{self.repository} is not pinned to a full commit SHA")


PROJECTS = (
    Project(
        "black",
        "psf/black",
        "ce1897a8f20d0f64844dd666d07f4003500d0e09",
        "src",
        IncrementalEdit(
            "src/black/nodes.py",
            ("src/black/linegen.py",),
            "LN = Union[Leaf, Node]",
            "LN = Union[Leaf, Node, int]",
        ),
    ),
    Project(
        "django",
        "django/django",
        "e2a424605ac2e7e6e799496542fb2997207e2f23",
        "django",
    ),
    Project(
        "isort",
        "pycqa/isort",
        "87adfe4732548abff5010336f2fc4b5e8237407d",
        "isort",
        IncrementalEdit(
            "isort/settings.py",
            ("isort/files.py",),
            "def is_skipped(self, file_path: Path) -> bool:",
            "def is_skipped(self, file_path: str) -> bool:",
        ),
    ),
    Project(
        "jinja",
        "pallets/jinja",
        "5ef70112a1ff19c05324ff889dd30405b1002044",
        "src",
        IncrementalEdit(
            "src/jinja2/nodes.py",
            (
                "src/jinja2/compiler.py",
                "src/jinja2/idtracking.py",
                "src/jinja2/visitor.py",
            ),
            (
                "def iter_child_nodes(\n"
                "        self,\n"
                "        exclude: t.Container[str] | None = None,\n"
                "        only: t.Container[str] | None = None,\n"
                '    ) -> t.Iterator["Node"]'
            ),
            (
                "def iter_child_nodes(\n"
                "        self,\n"
                "        exclude: t.Container[str] | None = None,\n"
                "        only: t.Container[str] | None = None,\n"
                "    ) -> t.Iterator[str]"
            ),
        ),
    ),
    Project(
        "pandas",
        "pandas-dev/pandas",
        "300a0cd8d3539fc9ca8539fbffd31809cc2f1fa5",
        "pandas",
    ),
    Project(
        "scikit-learn",
        "scikit-learn/scikit-learn",
        "1074736921eecc3ba84743404696bdcaf877c023",
        "sklearn",
    ),
    Project(
        "sympy",
        "sympy/sympy",
        "b16eebb5e19bc6a8d1da48f97ff1c8b87217c5b3",
        "sympy",
    ),
)

DEPENDENCIES = (
    "asgiref==3.12.1",
    "click==8.4.1",
    "colorama==0.4.6",
    "joblib==1.5.3",
    "markupsafe==3.0.3",
    "mpmath==1.4.1",
    "mypy-extensions==1.1.0",
    "numpy==2.5.1",
    "packaging==26.2",
    "pathspec==1.1.1",
    "platformdirs==4.10.0",
    "python-dateutil==2.9.0.post0",
    "pytokens==0.4.1",
    "pytz==2026.3.post1",
    "scipy==1.18.0",
    "six==1.17.0",
    "sqlparse==0.5.5",
    "threadpoolctl==3.6.0",
    "types-colorama==0.4.15.20260508",
    "tzdata==2026.3",
)

LABELS = ("baseline", "untuned", "tuned")


class FileTime(ctypes.Structure):
    _fields_ = [
        ("low", ctypes.c_uint32),
        ("high", ctypes.c_uint32),
    ]


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    for label in LABELS:
        parser.add_argument(f"--{label}", required=True, type=Path)
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--json-output", required=True, type=Path)
    parser.add_argument("--markdown-output", required=True, type=Path)
    parser.add_argument("--pairs", type=int, default=12)
    parser.add_argument("--warmups", type=int, default=2)
    parser.add_argument("--lsp-sessions", type=int, default=8)
    parser.add_argument("--timeout", type=float, default=90)
    args = parser.parse_args()
    if args.pairs < 6 or args.lsp_sessions < 1 or args.warmups < 1:
        parser.error("at least six pairs and one warmup/LSP session are required")
    return args


def command(arguments: list[str], *, environment: dict[str, str] | None = None) -> None:
    print(f"+ {' '.join(arguments)}", flush=True)
    subprocess.run(arguments, env=environment, check=True)


def prepare_projects(directory: Path) -> dict[str, Path]:
    directory.mkdir(parents=True, exist_ok=True)
    environment = os.environ | {
        "GIT_CONFIG_GLOBAL": os.devnull,
        "GIT_TERMINAL_PROMPT": "0",
        "GIT_LFS_SKIP_SMUDGE": "1",
    }
    checkouts: dict[str, Path] = {}
    for project in PROJECTS:
        checkout = directory / project.name
        checkout.mkdir(parents=True, exist_ok=True)
        git = [
            "git",
            "-c",
            f"core.hooksPath={os.devnull}",
            "-c",
            "core.longpaths=true",
            "-C",
            str(checkout),
        ]
        url = f"https://github.com/{project.repository}.git"
        if not (checkout / ".git").is_dir():
            command([*git, "init", "--quiet"], environment=environment)
            command([*git, "remote", "add", "origin", url], environment=environment)
        actual_url = subprocess.check_output(
            [*git, "config", "--local", "--get", "remote.origin.url"],
            text=True,
            env=environment,
        ).strip()
        if actual_url != url:
            raise RuntimeError(f"unexpected remote for {project.name}: {actual_url}")
        command(
            [*git, "sparse-checkout", "set", "--cone", project.source],
            environment=environment,
        )
        revision = subprocess.run(
            [*git, "rev-parse", "--verify", "HEAD"],
            capture_output=True,
            text=True,
            env=environment,
            check=False,
        )
        if revision.returncode or revision.stdout.strip() != project.revision:
            command(
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
                environment=environment,
            )
        command(
            [
                *git,
                "checkout",
                "--quiet",
                "--detach",
                "--force",
                "--no-recurse-submodules",
                project.revision,
            ],
            environment=environment,
        )
        actual_revision = subprocess.check_output(
            [*git, "rev-parse", "HEAD"], text=True, env=environment
        ).strip()
        if actual_revision != project.revision:
            raise RuntimeError(
                f"unexpected revision for {project.name}: {actual_revision}"
            )
        if not (checkout / project.source).is_dir():
            raise RuntimeError(f"missing held-out sources: {checkout / project.source}")
        checkouts[project.name] = checkout
    return checkouts


def prepare_environment(directory: Path) -> Path:
    if not directory.exists():
        command(["uv", "venv", "--python", "3.12", str(directory)])
    python = directory / "Scripts" / "python.exe"
    if not python.is_file():
        raise RuntimeError(f"missing Windows Python interpreter: {python}")
    command(
        [
            "uv",
            "pip",
            "install",
            "--python",
            str(python),
            "--only-binary",
            ":all:",
            *DEPENDENCIES,
        ]
    )
    return python


def extract_binary(source: Path, destination: Path) -> Path:
    source = source.resolve(strict=True)
    if source.is_file() and source.suffix.lower() == ".exe":
        return source
    executables = list(source.rglob("ty.exe")) if source.is_dir() else []
    if len(executables) == 1:
        return executables[0].resolve(strict=True)
    archives = list(source.rglob("ty-x86_64-pc-windows-msvc.zip"))
    if len(archives) != 1:
        raise RuntimeError(
            f"expected one Windows release archive in {source}: {archives}"
        )
    with zipfile.ZipFile(archives[0]) as archive:
        members = [
            member
            for member in archive.infolist()
            if not member.is_dir() and Path(member.filename).name.lower() == "ty.exe"
        ]
        if len(members) != 1:
            raise RuntimeError(f"expected one ty.exe in {archives[0]}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        with (
            archive.open(members[0]) as input_stream,
            destination.open("wb") as output_stream,
        ):
            shutil.copyfileobj(input_stream, output_stream)
    return destination.resolve(strict=True)


def kernel32() -> Any:
    library = ctypes.WinDLL("kernel32", use_last_error=True)  # type: ignore[attr-defined]
    library.GetCurrentProcess.restype = ctypes.c_void_p
    library.GetProcessAffinityMask.argtypes = [
        ctypes.c_void_p,
        ctypes.POINTER(ctypes.c_size_t),
        ctypes.POINTER(ctypes.c_size_t),
    ]
    library.SetProcessAffinityMask.argtypes = [ctypes.c_void_p, ctypes.c_size_t]
    library.GetProcessTimes.argtypes = [
        ctypes.c_void_p,
        ctypes.POINTER(FileTime),
        ctypes.POINTER(FileTime),
        ctypes.POINTER(FileTime),
        ctypes.POINTER(FileTime),
    ]
    library.QueryProcessCycleTime.argtypes = [
        ctypes.c_void_p,
        ctypes.POINTER(ctypes.c_uint64),
    ]
    return library


def pin_process(library: Any) -> tuple[int, int]:
    process_mask = ctypes.c_size_t()
    system_mask = ctypes.c_size_t()
    current_process = library.GetCurrentProcess()
    if not library.GetProcessAffinityMask(
        current_process, ctypes.byref(process_mask), ctypes.byref(system_mask)
    ):
        raise ctypes.WinError(ctypes.get_last_error())  # type: ignore[attr-defined]
    available = process_mask.value & system_mask.value
    if not available or not library.SetProcessAffinityMask(current_process, available):
        raise ctypes.WinError(ctypes.get_last_error())  # type: ignore[attr-defined]
    return available, available.bit_count()


def process_usage(library: Any, process: subprocess.Popen[bytes]) -> dict[str, int]:
    creation = FileTime()
    exit_time = FileTime()
    kernel = FileTime()
    user = FileTime()
    handle = ctypes.c_void_p(int(process._handle))  # type: ignore[attr-defined]
    if not library.GetProcessTimes(
        handle,
        ctypes.byref(creation),
        ctypes.byref(exit_time),
        ctypes.byref(kernel),
        ctypes.byref(user),
    ):
        raise ctypes.WinError(ctypes.get_last_error())  # type: ignore[attr-defined]
    cycles = ctypes.c_uint64()
    if not library.QueryProcessCycleTime(handle, ctypes.byref(cycles)):
        raise ctypes.WinError(ctypes.get_last_error())  # type: ignore[attr-defined]
    user_ns = ((user.high << 32) | user.low) * 100
    kernel_ns = ((kernel.high << 32) | kernel.low) * 100
    return {
        "cpu_ns": user_ns + kernel_ns,
        "user_ns": user_ns,
        "kernel_ns": kernel_ns,
        "cpu_cycles": cycles.value,
    }


def evaluation_environment(python: Path, parallelism: int) -> dict[str, str]:
    environment = os.environ.copy()
    for variable in (
        "CONDA_PREFIX",
        "LLVM_PROFILE_FILE",
        "PYTHONPATH",
        "RAYON_NUM_THREADS",
        "TY_CONFIG_FILE",
        "TY_LOG",
        "TY_LOG_PROFILE",
        "TY_OUTPUT_FORMAT",
        "TY_UV",
        "UV",
        "VIRTUAL_ENV",
    ):
        environment.pop(variable, None)
    environment.update(
        {
            "NO_COLOR": "1",
            "PYTHONDONTWRITEBYTECODE": "1",
            "TY_MAX_PARALLELISM": str(parallelism),
            "UV_OFFLINE": "1",
            "UV_PYTHON_DOWNLOADS": "never",
            "VIRTUAL_ENV": str(python.parent.parent),
            "PATH": f"{python.parent}{os.pathsep}{environment.get('PATH', '')}",
        }
    )
    return environment


def cli_arguments(project: Project, checkout: Path, python: Path) -> list[str]:
    return [
        "check",
        "--project",
        str(checkout),
        "--python",
        str(python),
        "--python-version",
        "3.12",
        "--python-platform",
        "win32",
        "--exit-zero",
        "--no-progress",
        "-qq",
        str(checkout / project.source),
    ]


def cli_once(
    library: Any,
    binary: Path,
    project: Project,
    checkout: Path,
    python: Path,
    parallelism: int,
    *,
    capture: bool = False,
) -> dict[str, Any]:
    arguments = cli_arguments(project, checkout, python)
    if capture:
        # Quiet mode suppresses diagnostics entirely, so validate real output
        # separately while retaining the production-like quiet timed workload.
        arguments.remove("-qq")
        arguments[-1:-1] = ["--output-format", "concise"]
    started = time.perf_counter_ns()
    process = subprocess.Popen(
        [str(binary), *arguments],
        cwd=checkout,
        env=evaluation_environment(python, parallelism),
        stdout=subprocess.PIPE if capture else subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate(timeout=180)
    wall_ns = time.perf_counter_ns() - started
    if process.returncode:
        raise RuntimeError(
            f"{project.name} failed ({process.returncode}): "
            f"{stderr.decode('utf-8', errors='replace')[:4000]}"
        )
    result = process_usage(library, process)
    result["wall_ns"] = wall_ns
    if capture:
        lines = (stdout or b"").replace(b"\r\n", b"\n").splitlines()
        error_lines = stderr.replace(b"\r\n", b"\n").splitlines()
        result["output_sha256"] = hashlib.sha256(b"\n".join(sorted(lines))).hexdigest()
        result["stderr_sha256"] = hashlib.sha256(
            b"\n".join(sorted(error_lines))
        ).hexdigest()
        result["output_lines"] = len(lines)
    return result


def ordered_labels(round_number: int) -> tuple[str, ...]:
    return tuple(itertools.permutations(LABELS))[round_number % 6]


def reduction(baseline: float, candidate: float) -> float:
    return round(100 * (1 - candidate / baseline), 4) if baseline else 0.0


def summarize_cli(samples: list[dict[str, Any]]) -> dict[str, Any]:
    summary: dict[str, Any] = {}
    for label in LABELS:
        measurements = [sample[label] for sample in samples]
        summary[label] = {
            "wall_median_ms": round(
                statistics.median(sample["wall_ns"] for sample in measurements) / 1e6, 4
            ),
            "cpu_median_ms": round(
                statistics.median(sample["cpu_ns"] for sample in measurements) / 1e6, 4
            ),
            "cpu_cycles_median": round(
                statistics.median(sample["cpu_cycles"] for sample in measurements)
            ),
        }
        for comparator in LABELS:
            if comparator == label:
                continue
            for metric in ("wall_ns", "cpu_ns", "cpu_cycles"):
                ratios = [
                    sample[label][metric] / sample[comparator][metric]
                    for sample in samples
                ]
                summary[label][f"{metric}_reduction_percent_vs_{comparator}"] = round(
                    100 * (1 - statistics.median(ratios)), 4
                )
    return summary


class LanguageServer:
    def __init__(
        self,
        binary: Path,
        checkout: Path,
        python: Path,
        parallelism: int,
        timeout: float,
    ):
        self.timeout = timeout
        self.identifier = 0
        self.responses: queue.Queue[dict[str, Any] | Exception] = queue.Queue()
        self.stderr_chunks: list[bytes] = []
        self.process = subprocess.Popen(
            [str(binary), "server"],
            cwd=checkout,
            env=evaluation_environment(python, parallelism),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=0,
        )
        if (
            self.process.stdin is None
            or self.process.stdout is None
            or self.process.stderr is None
        ):
            self.process.kill()
            self.process.wait()
            raise RuntimeError("could not open language-server pipes")

        def read_responses() -> None:
            try:
                if self.process.stdout is None:
                    raise RuntimeError("language-server stdout is unavailable")
                while True:
                    headers: dict[str, str] = {}
                    while True:
                        line = self.process.stdout.readline()
                        if not line:
                            raise RuntimeError("language server closed its output")
                        if line in (b"\r\n", b"\n"):
                            break
                        name, separator, value = line.decode("ascii").partition(":")
                        if not separator:
                            raise RuntimeError(
                                f"invalid language-server header: {line!r}"
                            )
                        headers[name.lower()] = value.strip()
                    remaining = int(headers["content-length"])
                    payload = bytearray()
                    while remaining:
                        chunk = self.process.stdout.read(remaining)
                        if not chunk:
                            raise RuntimeError("language server closed its output")
                        payload.extend(chunk)
                        remaining -= len(chunk)
                    response = json.loads(payload)
                    if not isinstance(response, dict):
                        raise RuntimeError("expected a JSON-RPC response object")
                    self.responses.put(response)
            except (OSError, RuntimeError, UnicodeError, ValueError, KeyError) as error:
                self.responses.put(error)

        def drain_stderr() -> None:
            if self.process.stderr is None:
                return
            while chunk := self.process.stderr.read(4096):
                if sum(map(len, self.stderr_chunks)) < 65536:
                    self.stderr_chunks.append(chunk)

        threading.Thread(target=read_responses, daemon=True).start()
        threading.Thread(target=drain_stderr, daemon=True).start()

    def send(self, message: dict[str, Any]) -> None:
        if self.process.stdin is None:
            raise RuntimeError("language-server stdin is unavailable")
        payload = json.dumps(message, separators=(",", ":")).encode("utf-8")
        self.process.stdin.write(
            f"Content-Length: {len(payload)}\r\n\r\n".encode("ascii") + payload
        )
        self.process.stdin.flush()

    def notify(self, method: str, params: dict[str, Any] | None = None) -> None:
        self.send({"jsonrpc": "2.0", "method": method, "params": params or {}})

    def request(self, method: str, params: dict[str, Any] | None = None) -> Any:
        self.identifier += 1
        identifier = self.identifier
        self.send(
            {"jsonrpc": "2.0", "id": identifier, "method": method, "params": params}
        )
        deadline = time.monotonic() + self.timeout
        while True:
            try:
                response = self.responses.get(
                    timeout=max(0, deadline - time.monotonic())
                )
            except queue.Empty as error:
                detail = b"".join(self.stderr_chunks).decode(errors="replace")
                raise TimeoutError(
                    f"{method} exceeded {self.timeout:g}s: {detail}"
                ) from error
            if isinstance(response, Exception):
                detail = b"".join(self.stderr_chunks).decode(errors="replace")
                raise RuntimeError(
                    f"could not read language-server output: {detail}"
                ) from response
            if "method" in response and "id" in response:
                items = response.get("params", {}).get("items", [])
                result = (
                    [{} for _ in items]
                    if response["method"] == "workspace/configuration"
                    else None
                )
                self.send({"jsonrpc": "2.0", "id": response["id"], "result": result})
                continue
            if response.get("id") != identifier:
                continue
            if "error" in response:
                raise RuntimeError(f"{method} failed: {response['error']}")
            return response.get("result")

    def shutdown(self) -> None:
        self.request("shutdown")
        self.notify("exit")
        if self.process.stdin is not None:
            self.process.stdin.close()
        if self.process.wait(timeout=self.timeout):
            detail = b"".join(self.stderr_chunks).decode(errors="replace")
            raise RuntimeError(f"language server exited unsuccessfully: {detail}")

    def close_if_running(self) -> None:
        if self.process.poll() is None:
            self.process.kill()
            self.process.wait()


def diagnostic_signature(items: list[dict[str, Any]]) -> tuple[str, ...]:
    return tuple(
        sorted(
            json.dumps(
                {
                    "code": item.get("code"),
                    "message": item.get("message"),
                    "range": item.get("range"),
                    "severity": item.get("severity"),
                },
                sort_keys=True,
                separators=(",", ":"),
            )
            for item in items
        )
    )


def lsp_session(
    library: Any,
    binary: Path,
    project: Project,
    checkout: Path,
    python: Path,
    parallelism: int,
    timeout: float,
) -> dict[str, Any]:
    edit = project.edit
    if edit is None:
        raise RuntimeError(f"{project.name} has no official held-out incremental edit")
    edited_path = checkout / edit.edited_file
    affected_paths = tuple(checkout / relative for relative in edit.affected_files)
    paths = (edited_path, *affected_paths)
    contents = {path: path.read_text(encoding="utf-8") for path in paths}
    if contents[edited_path].count(edit.original) != 1:
        raise RuntimeError(f"{project.name}: expected one official benchmark edit")
    replacement = contents[edited_path].replace(edit.original, edit.replacement, 1)
    launched = time.perf_counter_ns()
    client = LanguageServer(binary, checkout, python, parallelism, timeout)
    try:
        initialized = client.request(
            "initialize",
            {
                "processId": os.getpid(),
                "rootUri": checkout.as_uri(),
                "workspaceFolders": [{"uri": checkout.as_uri(), "name": project.name}],
                "clientInfo": {"name": "ty-windows-pgo-heldout", "version": "1"},
                "initializationOptions": {
                    "configuration": {
                        "environment": {"python": str(python.parent.parent)}
                    },
                    "diagnosticMode": "openFilesOnly",
                },
                "capabilities": {
                    "workspace": {"configuration": False},
                    "textDocument": {"diagnostic": {"dynamicRegistration": False}},
                },
            },
        )
        if not initialized.get("capabilities", {}).get("diagnosticProvider"):
            raise RuntimeError(
                f"{project.name}: server does not support pull diagnostics"
            )
        client.notify("initialized")
        initialize_ns = time.perf_counter_ns() - launched
        for path in paths:
            client.notify(
                "textDocument/didOpen",
                {
                    "textDocument": {
                        "uri": path.as_uri(),
                        "languageId": "python",
                        "version": 1,
                        "text": contents[path],
                    }
                },
            )

        def pull(path: Path) -> tuple[str, ...]:
            result = client.request(
                "textDocument/diagnostic", {"textDocument": {"uri": path.as_uri()}}
            )
            if result.get("kind") != "full":
                raise RuntimeError(
                    f"{project.name}: expected full diagnostics: {result}"
                )
            return diagnostic_signature(result.get("items", []))

        started = time.perf_counter_ns()
        initial = {path: pull(path) for path in paths}
        first_diagnostics_ns = time.perf_counter_ns() - started
        initial_digest = hashlib.sha256(
            json.dumps(
                {str(path.relative_to(checkout)): initial[path] for path in paths},
                sort_keys=True,
            ).encode()
        ).hexdigest()
        samples: list[int] = []
        edit_digests: list[str] = []
        mutation_changes = 0
        for index in range(6):
            apply_edit = index % 2 == 0
            started = time.perf_counter_ns()
            client.notify(
                "textDocument/didChange",
                {
                    "textDocument": {"uri": edited_path.as_uri(), "version": index + 2},
                    "contentChanges": [
                        {"text": replacement if apply_edit else contents[edited_path]}
                    ],
                },
            )
            diagnostics = {path: pull(path) for path in paths}
            samples.append(time.perf_counter_ns() - started)
            edit_digests.append(
                hashlib.sha256(
                    json.dumps(
                        {
                            str(path.relative_to(checkout)): diagnostics[path]
                            for path in paths
                        },
                        sort_keys=True,
                    ).encode()
                ).hexdigest()
            )
            changed = any(diagnostics[path] != initial[path] for path in paths)
            if apply_edit:
                mutation_changes += int(changed)
            elif changed:
                raise RuntimeError(
                    f"{project.name}: reverting edit did not restore diagnostics"
                )
        if not mutation_changes:
            raise RuntimeError(f"{project.name}: official edit changed no diagnostics")
        client.shutdown()
        usage = process_usage(library, client.process)
    finally:
        client.close_if_running()
    return {
        "initialize_ns": initialize_ns,
        "first_diagnostics_ns": first_diagnostics_ns,
        "edit_ns": samples,
        "initial_diagnostics_sha256": initial_digest,
        "edit_diagnostics_sha256": edit_digests,
        "mutation_changes": mutation_changes,
        **usage,
    }


def summarize_lsp(samples: list[dict[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for label in LABELS:
        sessions = [sample[label] for sample in samples]
        result[label] = {
            "sessions": len(sessions),
            "initial_diagnostics_median_ms": round(
                statistics.median(
                    session["first_diagnostics_ns"] for session in sessions
                )
                / 1e6,
                4,
            ),
            "edit_median_ms": round(
                statistics.median(
                    value for session in sessions for value in session["edit_ns"]
                )
                / 1e6,
                4,
            ),
            "cpu_median_ms": round(
                statistics.median(session["cpu_ns"] for session in sessions) / 1e6, 4
            ),
        }
    for label in LABELS:
        for comparator in LABELS:
            if label == comparator:
                continue
            result[label][f"edit_reduction_percent_vs_{comparator}"] = reduction(
                result[comparator]["edit_median_ms"], result[label]["edit_median_ms"]
            )
            result[label][f"initial_reduction_percent_vs_{comparator}"] = reduction(
                result[comparator]["initial_diagnostics_median_ms"],
                result[label]["initial_diagnostics_median_ms"],
            )
            result[label][f"cpu_reduction_percent_vs_{comparator}"] = reduction(
                result[comparator]["cpu_median_ms"], result[label]["cpu_median_ms"]
            )
    return result


def aggregate(report: dict[str, Any], category: str) -> dict[str, Any]:
    workloads = report.get(category, [])
    if not workloads:
        return {}
    metrics = (
        ("wall_ns", "cpu_ns", "cpu_cycles")
        if category == "cli"
        else ("edit", "initial", "cpu")
    )
    result: dict[str, Any] = {"projects": len(workloads)}
    for label in LABELS:
        comparisons: dict[str, float] = {}
        for comparator in LABELS:
            if label == comparator:
                continue
            for metric in metrics:
                key = f"{metric}_reduction_percent_vs_{comparator}"
                ratios = [
                    1 - workload["summary"][label][key] / 100 for workload in workloads
                ]
                comparisons[key] = round(
                    100 * (1 - statistics.geometric_mean(ratios)), 4
                )
        result[label] = comparisons
    return result


def markdown_report(report: dict[str, Any]) -> str:
    lines = [
        "# Windows x86-64 ty PGO benchmark",
        "",
        "Real production release executables, pinned held-out projects, "
        "and a shared Windows Python 3.12 environment.",
        "",
        "## CLI",
        "",
        "| Project | No PGO CPU | Untuned PGO CPU | Tuned PGO CPU | "
        "Tuned vs. no PGO | Tuned vs. untuned |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for workload in report.get("cli", []):
        summary = workload["summary"]
        lines.append(
            f"| {workload['project']} | {summary['baseline']['cpu_median_ms']:.2f} ms | "
            f"{summary['untuned']['cpu_median_ms']:.2f} ms | "
            f"{summary['tuned']['cpu_median_ms']:.2f} ms | "
            f"{summary['tuned']['cpu_ns_reduction_percent_vs_baseline']:+.2f}% | "
            f"{summary['tuned']['cpu_ns_reduction_percent_vs_untuned']:+.2f}% |"
        )
    if cli := aggregate(report, "cli"):
        lines.append(
            "| **Geometric mean** | — | — | — | "
            f"**{cli['tuned']['cpu_ns_reduction_percent_vs_baseline']:+.2f}%** | "
            f"**{cli['tuned']['cpu_ns_reduction_percent_vs_untuned']:+.2f}%** |"
        )
    lines.extend(
        [
            "",
            "## Language server",
            "",
            "| Project | No PGO edit | Untuned PGO edit | Tuned PGO edit | "
            "Tuned vs. no PGO | Tuned vs. untuned |",
            "| --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for workload in report.get("lsp", []):
        summary = workload["summary"]
        lines.append(
            f"| {workload['project']} | {summary['baseline']['edit_median_ms']:.2f} ms | "
            f"{summary['untuned']['edit_median_ms']:.2f} ms | "
            f"{summary['tuned']['edit_median_ms']:.2f} ms | "
            f"{summary['tuned']['edit_reduction_percent_vs_baseline']:+.2f}% | "
            f"{summary['tuned']['edit_reduction_percent_vs_untuned']:+.2f}% |"
        )
    if lsp := aggregate(report, "lsp"):
        lines.append(
            "| **Geometric mean** | — | — | — | "
            f"**{lsp['tuned']['edit_reduction_percent_vs_baseline']:+.2f}%** | "
            f"**{lsp['tuned']['edit_reduction_percent_vs_untuned']:+.2f}%** |"
        )
    if error := report.get("error"):
        lines.extend(["", f"**Incomplete:** {error}"])
    lines.extend(
        [
            "",
            "Positive percentages mean less CPU time or lower latency. "
            "The six possible execution orders rotate across paired rounds.",
        ]
    )
    return "\n".join(lines) + "\n"


def checkpoint(
    report: dict[str, Any], json_output: Path, markdown_output: Path
) -> None:
    json_output.parent.mkdir(parents=True, exist_ok=True)
    markdown_output.parent.mkdir(parents=True, exist_ok=True)
    report["aggregate"] = {
        "cli": aggregate(report, "cli"),
        "lsp": aggregate(report, "lsp"),
    }
    json_output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    markdown_output.write_text(markdown_report(report), encoding="utf-8")


def main() -> None:
    args = arguments()
    if os.name != "nt":
        raise RuntimeError("this benchmark requires a native Windows runner")
    workspace = args.workspace.resolve()
    workspace.mkdir(parents=True, exist_ok=True)
    report: dict[str, Any] = {
        "platform": platform.platform(),
        "python": sys.version,
        "pairs": args.pairs,
        "warmups": args.warmups,
        "lsp_sessions": args.lsp_sessions,
        "training_contamination": False,
        "projects": {},
        "binaries": {},
        "cli": [],
        "lsp": [],
    }
    checkpoint(report, args.json_output, args.markdown_output)
    try:
        library = kernel32()
        affinity, parallelism = pin_process(library)
        report["cpu_affinity_mask"] = hex(affinity)
        report["parallelism"] = parallelism
        binaries: dict[str, Path] = {}
        for label in LABELS:
            binary = extract_binary(
                getattr(args, label), workspace / "executables" / label / "ty.exe"
            )
            version = subprocess.check_output(
                [str(binary), "--version"], text=True
            ).strip()
            data = binary.read_bytes()
            binaries[label] = binary
            report["binaries"][label] = {
                "path": str(binary),
                "sha256": hashlib.sha256(data).hexdigest(),
                "bytes": len(data),
                "version": version,
            }
        checkouts = prepare_projects(workspace / "holdouts")
        python = prepare_environment(workspace / "evaluation-venv")
        report["python_environment"] = str(python)
        report["dependencies"] = list(DEPENDENCIES)
        for project in PROJECTS:
            report["projects"][project.name] = {
                "repository": f"https://github.com/{project.repository}",
                "revision": project.revision,
                "source": project.source,
                "python_files": sum(
                    1
                    for path in (checkouts[project.name] / project.source).rglob("*")
                    if path.is_file() and path.suffix in {".py", ".pyi"}
                ),
            }
        checkpoint(report, args.json_output, args.markdown_output)

        for project in PROJECTS:
            checkout = checkouts[project.name]
            print(f"Validating {project.name} diagnostic equivalence", flush=True)
            outputs = {
                label: cli_once(
                    library,
                    binary,
                    project,
                    checkout,
                    python,
                    parallelism,
                    capture=True,
                )
                for label, binary in binaries.items()
            }
            if (
                len(
                    {
                        (sample["output_sha256"], sample["stderr_sha256"])
                        for sample in outputs.values()
                    }
                )
                != 1
            ):
                print(
                    f"Retrying {project.name} equivalence single-threaded", flush=True
                )
                outputs = {
                    label: cli_once(
                        library, binary, project, checkout, python, 1, capture=True
                    )
                    for label, binary in binaries.items()
                }
                if (
                    len(
                        {
                            (sample["output_sha256"], sample["stderr_sha256"])
                            for sample in outputs.values()
                        }
                    )
                    != 1
                ):
                    raise RuntimeError(
                        f"{project.name}: variants produced different diagnostics"
                    )
            if not outputs["baseline"]["output_lines"]:
                raise RuntimeError(
                    f"{project.name}: diagnostic-equivalence check produced no output"
                )

            for index in range(args.warmups):
                for label in ordered_labels(index):
                    cli_once(
                        library, binaries[label], project, checkout, python, parallelism
                    )
            samples: list[dict[str, Any]] = []
            for index in range(args.pairs):
                order = ordered_labels(index)
                observation: dict[str, Any] = {"round": index, "order": list(order)}
                for label in order:
                    observation[label] = cli_once(
                        library, binaries[label], project, checkout, python, parallelism
                    )
                samples.append(observation)
            workload = {
                "project": project.name,
                "output_sha256": outputs["baseline"]["output_sha256"],
                "stderr_sha256": outputs["baseline"]["stderr_sha256"],
                "output_lines": outputs["baseline"]["output_lines"],
                "summary": summarize_cli(samples),
                "samples": samples,
            }
            report["cli"].append(workload)
            checkpoint(report, args.json_output, args.markdown_output)
            tuned = workload["summary"]["tuned"]
            print(
                f"{project.name}: tuned CPU vs no PGO "
                f"{tuned['cpu_ns_reduction_percent_vs_baseline']:+.2f}%, "
                f"vs untuned {tuned['cpu_ns_reduction_percent_vs_untuned']:+.2f}%",
                flush=True,
            )

        for project in (project for project in PROJECTS if project.edit is not None):
            checkout = checkouts[project.name]
            print(
                f"Benchmarking held-out language-server edits: {project.name}",
                flush=True,
            )
            samples = []
            for index in range(-1, args.lsp_sessions):
                order = ordered_labels(index)
                observation = {"round": index, "order": list(order)}
                for label in order:
                    observation[label] = lsp_session(
                        library,
                        binaries[label],
                        project,
                        checkout,
                        python,
                        parallelism,
                        args.timeout,
                    )
                if (
                    len(
                        {
                            (
                                observation[label]["initial_diagnostics_sha256"],
                                tuple(observation[label]["edit_diagnostics_sha256"]),
                            )
                            for label in LABELS
                        }
                    )
                    != 1
                ):
                    raise RuntimeError(
                        f"{project.name}: language-server diagnostics differ"
                    )
                if index >= 0:
                    samples.append(observation)
            report["lsp"].append(
                {
                    "project": project.name,
                    "summary": summarize_lsp(samples),
                    "samples": samples,
                }
            )
            checkpoint(report, args.json_output, args.markdown_output)
        print(markdown_report(report), flush=True)
    except Exception as error:
        report["error"] = f"{type(error).__name__}: {error}"
        checkpoint(report, args.json_output, args.markdown_output)
        raise


if __name__ == "__main__":
    main()
