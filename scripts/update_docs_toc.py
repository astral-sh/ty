# /// script
# requires-python = ">=3.13"
# dependencies = ["markdown~=3.8", "mkdocs~=1.6.1"]
# ///

"""Update `docs/README.md`'s TOC."""

from __future__ import annotations

import re
from collections.abc import Generator
from pathlib import Path

from markdown import Markdown
from mkdocs.structure.toc import AnchorLink, TableOfContents, get_toc

_THIS_FILE = Path(__file__)
_REPO_ROOT = _THIS_FILE.parent.parent
_DOCS_README = _REPO_ROOT / "docs" / "README.md"

_TOC_START_MARKER = "<!-- TOC start -->\n"
_TOC_END_MARKER = "\n<!-- TOC end -->"
_TOC_SEPARATOR = " |\n"

_CODE_BLOCK = re.compile(
    r"""(?xm)
        ^(```+).*\n
        (?>(?!\1).*\n)*?
        \1$
    """
)


def _iter_links(toc: TableOfContents) -> Generator[AnchorLink]:
    for link in toc:
        yield link
        yield from link.children


def _get_new_toc(sanitized_contents: str) -> str:
    parser = Markdown(extensions=["toc"])
    parser.convert(sanitized_contents)
    toc = get_toc(parser.toc_tokens)  # type: ignore  # noqa: PGH003

    links = [
        f"**[{link.title}]({link.url})**"
        for link in _iter_links(toc)
        if link.level == 2
    ]

    return _TOC_SEPARATOR.join(links)


def _replace_toc(original: str, new_toc: str) -> str:
    start_marker_index = original.find(_TOC_START_MARKER)
    end_marker_index = original.find(_TOC_END_MARKER)

    if start_marker_index == -1 or end_marker_index == -1:
        raise RuntimeError(f"TOC not found in {_DOCS_README}")

    prefix = original[:start_marker_index]
    suffix = original[end_marker_index + len(_TOC_END_MARKER) :]

    return f"{prefix}{_TOC_START_MARKER}{new_toc}{_TOC_END_MARKER}{suffix}"


def main() -> None:
    contents = _DOCS_README.read_text()
    # markdown's parser does not differentiate between
    # comments in code blocks and actual headers.
    contents_without_code_blocks = _CODE_BLOCK.sub("", contents)

    new_toc = _get_new_toc(contents_without_code_blocks)
    new_contents = _replace_toc(contents, new_toc)
    _DOCS_README.write_text(new_contents)


if __name__ == "__main__":
    main()
