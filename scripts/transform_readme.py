"""Transform the README.md to support a specific deployment target.

By default, we assume that our README.md will be rendered on GitHub. However,
PyPI includes the README with different rendering.
"""

from __future__ import annotations

import re
import urllib.parse
from pathlib import Path

import tomllib


def main() -> None:
    """Modify the README.md to support PyPI."""
    # Read the current version from the `dist-workspace.toml`.
    with Path("dist-workspace.toml").open(mode="rb") as fp:
        # Parse the TOML.
        dist_workspace = tomllib.load(fp)
        if "workspace" in dist_workspace and "version" in dist_workspace["workspace"]:
            version = dist_workspace["workspace"]["version"]
        else:
            raise ValueError("Version not found in dist-workspace.toml")

    content = Path("README.md").read_text(encoding="utf8")

    # Replace any relative URLs (e.g., `[CONTRIBUTING.md`) with absolute URLs.
    def replace(match: re.Match) -> str:
        url = match.group(1)
        if not url.startswith("http"):
            url = urllib.parse.urljoin(
                f"https://github.com/astral-sh/ty/blob/{version}/README.md", url
            )
        return f"]({url})"

    content = re.sub(r"]\(([^)]+)\)", replace, content)

    # Replace any GitHub admonitions
    def replace(match: re.Match) -> str:
        name = match.group(1)
        return f"> {name}:"

    content = re.sub(r"> \[\!(\w*)\]", replace, content)

    with Path("README.md").open("w", encoding="utf8") as fp:
        fp.write(content)


if __name__ == "__main__":
    main()
