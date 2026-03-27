from __future__ import annotations

import os
import sys

from ty import find_ty_bin


def _run() -> None:
    ty_bin_env = os.environ.get("TY_BIN")
    if ty_bin_env:
        ty = ty_bin_env
    else:
        ty = find_ty_bin()

    if sys.platform == "win32":
        import subprocess

        # Avoid emitting a traceback on interrupt
        try:
            completed_process = subprocess.run([ty, *sys.argv[1:]])
        except KeyboardInterrupt:
            sys.exit(2)

        sys.exit(completed_process.returncode)
    else:
        os.execvp(ty, [ty, *sys.argv[1:]])


if __name__ == "__main__":
    _run()
