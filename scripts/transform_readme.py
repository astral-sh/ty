"""Transform the README.md to support a specific deployment target.

By default, we assume that our README.md will be rendered on GitHub. However,
PyPI includes the README with different rendering.
"""

from __future__ import annotations

import re
import tomllib
import urllib.parse
from pathlib import Path

URL = "https://raw.githubusercontent.com/astral-sh/ty/main/docs/assets/{}.svg"
URL_LIGHT = URL.format("ty-benchmark-cli-light")
URL_DARK = URL.format("ty-benchmark-cli-dark")

# https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#specifying-the-theme-an-image-is-shown-to
GITHUB_BENCHMARK = f"""
<p align="center">
  <picture align="center">
    <source media="(prefers-color-scheme: dark)" srcset="{URL_DARK}">
    <source media="(prefers-color-scheme: light)" srcset="{URL_LIGHT}">
    <img alt="Shows a bar chart with benchmark results." src="{URL_LIGHT}">
  </picture>
</p>
"""

# https://github.com/pypi/warehouse/issues/11251
PYPI_BENCHMARK = f"""
<p align="center">
  <img alt="Shows a bar chart with benchmark results." src="{URL_LIGHT}">
</p>
"""


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

    # Replace the benchmark image with a PyPI-compatible version.
    # PyPI doesn't support the `<picture>` element for light/dark mode.
    if GITHUB_BENCHMARK not in content:
        msg = "README.md is not in the expected format (benchmark image not found)."
        raise ValueError(msg)
    content = content.replace(GITHUB_BENCHMARK, PYPI_BENCHMARK)

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
