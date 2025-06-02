# /// script
# requires-python = ">=3.13"
# dependencies = ["markdown", "mkdocs"]
# ///

"""Update `docs/README.md`'s table of contents.

This script generates a list of links to level-2 headers and writes that back
to `docs/README.md`. It is run in CI via `autogenerate_files.sh`.
"""

from __future__ import annotations

import re
from collections.abc import Generator
from pathlib import Path

from markdown import Markdown
from mkdocs.structure.toc import AnchorLink, TableOfContents, get_toc

THIS_FILE = Path(__file__)
REPO_ROOT = THIS_FILE.parent.parent
DOCS_README = REPO_ROOT / "docs" / "README.md"

TOC_START_MARKER = "<!-- Generated table of contents start -->\n\n"
TOC_END_MARKER = "\n\n<!-- Generated table of contents end -->"
TOC_SEPARATOR = " |\n"

CODE_BLOCK = re.compile(
    r"""(?xm)
        ^(```+).*\n
        (?>(?!\1).*\n)*?
        \1$
    """
)


def iter_links(toc: TableOfContents) -> Generator[AnchorLink]:
    """Yield all links in the given table of contents recursively."""

    def visit_link(link: AnchorLink) -> Generator[AnchorLink]:
        yield link

        for child in link.children:
            yield from visit_link(child)

    for link in toc:
        yield from visit_link(link)


def get_new_toc(contents: str) -> str:
    """Generate new table of contents."""

    # markdown's parser does not differentiate between
    # Python comments in code blocks and actual headers.
    contents_without_code_blocks = CODE_BLOCK.sub("", contents)

    parser = Markdown(extensions=["toc"])
    parser.convert(contents_without_code_blocks)

    # `toc_tokens` is dynamically set
    toc = get_toc(parser.toc_tokens)  # type: ignore  # noqa: PGH003

    links = [
        f"**[{link.title}]({link.url})**" for link in iter_links(toc) if link.level == 2
    ]

    return TOC_SEPARATOR.join(links)


def replace_toc(original: str, new_toc: str) -> str:
    """Replace the existing table of contents with the new one.

    The table of contents is separated from the rest of the file
    using `TOC_START_MARKER` and `TOC_END_MARKER`.
    """

    try:
        start_marker_index = original.index(TOC_START_MARKER)
        end_marker_index = original.index(TOC_END_MARKER)
    except ValueError as error:
        raise RuntimeError(f"No table of contents found in {DOCS_README}") from error

    prefix = original[:start_marker_index]
    suffix = original[end_marker_index + len(TOC_END_MARKER) :]

    return f"{prefix}{TOC_START_MARKER}{new_toc}{TOC_END_MARKER}{suffix}"


def main() -> None:
    contents = DOCS_README.read_text()
    new_toc = get_new_toc(contents)
    new_contents = replace_toc(contents, new_toc)

    DOCS_README.write_text(new_contents)


if __name__ == "__main__":
    main()
