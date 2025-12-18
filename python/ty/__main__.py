from __future__ import annotations

import os
import sys
import sysconfig


def find_ty_bin() -> str:
    """Return the ty binary path."""

    ty_exe = "ty" + sysconfig.get_config_var("EXE")

    scripts_path = os.path.join(sysconfig.get_path("scripts"), ty_exe)
    if os.path.isfile(scripts_path):
        return scripts_path

    if sys.version_info >= (3, 10):
        user_scheme = sysconfig.get_preferred_scheme("user")
    elif os.name == "nt":
        user_scheme = "nt_user"
    elif sys.platform == "darwin" and sys._framework:
        user_scheme = "osx_framework_user"
    else:
        user_scheme = "posix_user"

    user_path = os.path.join(sysconfig.get_path("scripts", scheme=user_scheme), ty_exe)
    if os.path.isfile(user_path):
        return user_path

    # Search in `bin` adjacent to package root (as created by `pip install --target`).
    pkg_root = os.path.dirname(os.path.dirname(__file__))
    target_path = os.path.join(pkg_root, "bin", ty_exe)
    if os.path.isfile(target_path):
        return target_path

    # Search for pip-specific build environments.
    #
    # Expect to find ty in <prefix>/pip-build-env-<rand>/overlay/bin/ty
    # Expect to find a "normal" folder at <prefix>/pip-build-env-<rand>/normal
    #
    # See: https://github.com/pypa/pip/blob/102d8187a1f5a4cd5de7a549fd8a9af34e89a54f/src/pip/_internal/build_env.py#L87
    paths = os.environ.get("PATH", "").split(os.pathsep)
    if len(paths) >= 2:

        def get_last_three_path_parts(path: str) -> list[str]:
            """Return a list of up to the last three parts of a path."""
            parts = []

            while len(parts) < 3:
                head, tail = os.path.split(path)
                if tail or head != path:
                    parts.append(tail)
                    path = head
                else:
                    parts.append(path)
                    break

            return parts

        maybe_overlay = get_last_three_path_parts(paths[0])
        maybe_normal = get_last_three_path_parts(paths[1])
        if (
            len(maybe_normal) >= 3
            and maybe_normal[-1].startswith("pip-build-env-")
            and maybe_normal[-2] == "normal"
            and len(maybe_overlay) >= 3
            and maybe_overlay[-1].startswith("pip-build-env-")
            and maybe_overlay[-2] == "overlay"
        ):
            # The overlay must contain the ty binary.
            candidate = os.path.join(paths[0], ty_exe)
            if os.path.isfile(candidate):
                return candidate

    raise FileNotFoundError(scripts_path)


def main() -> None:
    """Main entry point that forwards arguments to the ty executable."""
    try:
        ty = os.fsdecode(find_ty_bin())
        # Validate that the ty binary exists and is executable
        if not os.path.isfile(ty) or not os.access(ty, os.X_OK):
            sys.stderr.write("Error: ty executable not found or not executable\n")
            sys.exit(1)
        
        # Use -- separator to safely separate wrapper args from ty command args
        # This prevents argument injection by treating everything after -- as literal arguments
        wrapper_args = []
        ty_args = []
        separator_found = False
        
        for arg in sys.argv[1:]:
            if arg == "--" and not separator_found:
                separator_found = True
            elif separator_found:
ty_args.append(arg)
            else:
                wrapper_args.append(arg)
        
        # If no separator found, treat all args as ty arguments (backward compatibility)
        if not separator_found:
            ty_args = wrapper_args
            wrapper_args = []
        
        # Build final argument list for execution
        args = [ty, *ty_args]
        
        if sys.platform == "win32":
            import subprocess

            completed_process = subprocess.run(args)
            sys.exit(completed_process.returncode)
        else:
            os.execvp(ty, args)
    except FileNotFoundError:
        sys.stderr.write("Error: ty executable not found\n")
        sys.exit(1)
    except Exception as e:
        sys.stderr.write(f"Error: {type(e).__name__}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
