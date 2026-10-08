"""Compare ty diagnostics and language-server replies for two release binaries."""

from __future__ import annotations

import json
import os
import queue
import subprocess
import threading
import time
from pathlib import Path

MODELS = """from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

def load_user() -> User:
    return User("Ada", 37)
"""
INVALID_MODELS = """from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: str

def load_user() -> User:
    return User("Ada", 37)
"""
SERVICE = """from models import User, load_user

def describe(user: User) -> str:
    return user.name.upper()

user = load_user()
result = describe(user)
next_age = user.age + 1
"""


def prepare_language_server(root: Path) -> None:
    root.mkdir(parents=True, exist_ok=True)
    (root / "pyproject.toml").write_text(
        '[project]\nname = "ty-codegen-benchmark"\nversion = "0.0.0"\n',
        encoding="utf-8",
    )
    (root / "models.py").write_text(MODELS, encoding="utf-8")
    (root / "service.py").write_text(SERVICE, encoding="utf-8")


def language_server(binary: Path, root: Path, environment: dict[str, str]) -> dict:
    """Measure a full session and edits, retaining semantic replies for comparison."""
    started = time.perf_counter()
    process = subprocess.Popen(
        [str(binary), "server"],
        cwd=root,
        env=environment,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=0,
    )
    if process.stdin is None or process.stdout is None or process.stderr is None:
        process.kill()
        process.wait()
        raise RuntimeError("Could not open language-server pipes")

    messages: queue.Queue = queue.Queue()
    stderr_chunks = []
    replies = []
    request_id = 0

    def read_messages():
        try:
            while True:
                headers = {}
                while True:
                    line = process.stdout.readline()
                    if not line:
                        raise RuntimeError("Language server closed its output")
                    if line in (b"\r\n", b"\n"):
                        break
                    name, _, value = line.decode("ascii").partition(":")
                    headers[name.lower()] = value.strip()
                remaining = int(headers["content-length"])
                chunks = []
                while remaining:
                    chunk = process.stdout.read(remaining)
                    if not chunk:
                        raise RuntimeError("Language server closed its output")
                    chunks.append(chunk)
                    remaining -= len(chunk)
                messages.put(json.loads(b"".join(chunks)))
        except Exception as error:
            messages.put(error)

    def read_stderr():
        while chunk := process.stderr.read(4096):
            stderr_chunks.append(chunk)

    reader = threading.Thread(target=read_messages, daemon=True)
    errors = threading.Thread(target=read_stderr, daemon=True)
    reader.start()
    errors.start()

    def send(message):
        payload = json.dumps(message, separators=(",", ":")).encode("utf-8")
        process.stdin.write(f"Content-Length: {len(payload)}\r\n\r\n".encode("ascii"))
        process.stdin.write(payload)

    def request(method, params=None):
        nonlocal request_id
        request_id += 1
        identifier = request_id
        send({"jsonrpc": "2.0", "id": identifier, "method": method, "params": params})
        deadline = time.monotonic() + 30
        while True:
            response = messages.get(timeout=max(0, deadline - time.monotonic()))
            if isinstance(response, Exception):
                raise RuntimeError(
                    "Could not read language-server output"
                ) from response
            if "method" in response and "id" in response:
                result = [] if response["method"] == "workspace/configuration" else None
                send({"jsonrpc": "2.0", "id": response["id"], "result": result})
            elif response.get("id") == identifier:
                if "error" in response:
                    raise RuntimeError(f"{method} failed: {response['error']}")
                result = response.get("result")
                # resultId is an opaque cache token; diagnostic contents are the contract.
                if method == "textDocument/diagnostic":
                    if not isinstance(result, dict) or result.get("kind") != "full":
                        raise RuntimeError("Expected a full diagnostic response")
                    result = {
                        key: value for key, value in result.items() if key != "resultId"
                    }
                replies.append({"method": method, "result": result})
                return result

    def notify(method, params=None):
        send({"jsonrpc": "2.0", "method": method, "params": params or {}})

    def diagnostics(path):
        result = request(
            "textDocument/diagnostic", {"textDocument": {"uri": path.as_uri()}}
        )
        return result["items"]

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
        if not initialized.get("capabilities", {}).get("diagnosticProvider"):
            raise RuntimeError("Language server does not support pull diagnostics")
        notify("initialized")
        models = root / "models.py"
        service = root / "service.py"
        for path, text in ((models, MODELS), (service, SERVICE)):
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
            raise RuntimeError("Expected clean initial diagnostics")
        for method, position in (
            ("textDocument/hover", {"line": 5, "character": 10}),
            ("textDocument/definition", {"line": 5, "character": 8}),
            ("textDocument/completion", {"line": 5, "character": 16}),
        ):
            result = request(
                method,
                {"textDocument": {"uri": service.as_uri()}, "position": position},
            )
            if not result:
                raise RuntimeError(f"Expected a nonempty {method} result")
        edit_seconds = []
        for index in range(12):
            invalid = index % 2 == 0
            edit_started = time.perf_counter()
            notify(
                "textDocument/didChange",
                {
                    "textDocument": {"uri": models.as_uri(), "version": index + 2},
                    "contentChanges": [{"text": INVALID_MODELS if invalid else MODELS}],
                },
            )
            models_diagnostics = diagnostics(models)
            service_diagnostics = diagnostics(service)
            edit_seconds.append(time.perf_counter() - edit_started)
            if (
                bool(models_diagnostics) != invalid
                or bool(service_diagnostics) != invalid
            ):
                raise RuntimeError("Incremental cross-file diagnostics did not update")
        request("shutdown")
        notify("exit")
        process.stdin.close()
        returncode = process.wait(timeout=15)
        elapsed = time.perf_counter() - started
        if returncode:
            raise RuntimeError(
                b"".join(stderr_chunks).decode("utf-8", errors="replace")
            )
        return {
            "elapsed_seconds": elapsed,
            "edit_seconds": edit_seconds,
            "replies": replies,
        }
    finally:
        if process.poll() is None:
            process.kill()
            process.wait()
        reader.join(timeout=1)
        errors.join(timeout=1)
