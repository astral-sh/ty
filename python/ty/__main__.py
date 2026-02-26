from __future__ import annotations

import os
import sys

from ty import find_ty_bin


def _detect_virtualenv() -> str:
    """
    Find the virtual environment path for the current Python executable.
    """

    # If it's already set, then just use it
    value = os.getenv("VIRTUAL_ENV")
    if value:
        return value

    # Otherwise, check if we're in a venv
    venv_marker = os.path.join(sys.prefix, "pyvenv.cfg")

    if os.path.exists(venv_marker):
        return sys.prefix

    return ""


def _run() -> None:
    ty = find_ty_bin()

    env = os.environ.copy()
    venv = _detect_virtualenv()
    if venv:
        env.setdefault("VIRTUAL_ENV", venv)

    # Let `ty` know that it was spawned by this Python interpreter
    env["TY__PARENT_INTERPRETER"] = sys.executable

    if sys.platform == "win32":
        import subprocess

        # Avoid emitting a traceback on interrupt
        try:
            completed_process = subprocess.run([ty, *sys.argv[1:]], env=env)
        except KeyboardInterrupt:
            sys.exit(2)

        sys.exit(completed_process.returncode)
    else:
        os.execvpe(ty, [ty, *sys.argv[1:]], env=env)


if __name__ == "__main__":
    _run()
