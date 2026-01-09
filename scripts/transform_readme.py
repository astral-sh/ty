"""Transform the README.md to support a specific deployment target.

By default, we assume that our README.md will be rendered on GitHub. However,
PyPI includes the README with different rendering.
"""

from __future__ import annotations

import re
import tomllib
import urllib.parse
from pathlib import Path

# The benchmark SVG includes a CSS media query that adapts to light/dark mode.
# PyPI doesn't support this, so we replace it with a light-only version.
# See: https://github.com/pypi/warehouse/issues/11251
BENCHMARK_URL = "https://raw.githubusercontent.com/astral-sh/ty/main/docs/assets/ty-benchmark-cli.svg"
BENCHMARK_URL_LIGHT = "https://raw.githubusercontent.com/astral-sh/ty/main/docs/assets/ty-benchmark-cli-light.svg"


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

    # Replace the benchmark image URL with the light-only version for PyPI.
    if BENCHMARK_URL not in content:
        msg = "README.md is not in the expected format (benchmark image not found)."
        raise ValueError(msg)
    content = content.replace(BENCHMARK_URL, BENCHMARK_URL_LIGHT)

    # Replace relative src="./..." attributes with absolute GitHub raw URLs.
    def replace_src(match: re.Match) -> str:
        path = match.group(1).lstrip("./")
        return f'src="https://raw.githubusercontent.com/astral-sh/ty/{version}/{path}"'

    content = re.sub(r'src="(\./[^"]+)"', replace_src, content)

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
