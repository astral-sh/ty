- For `astral-sh/ruff` entries, get the old and new submodule commits with `git rev-parse HEAD^:ruff`
    and `git rev-parse HEAD:ruff` in the ty checkout. Use `git -C ruff log` and `git -C ruff show`
    to inspect changes in that range. Use ty's own history for `astral-sh/ty` entries.
- Follow ty's section names and order as defined by `[tool.rooster.section-labels]` in
    `pyproject.toml`. Keep explicitly categorized entries in their generated sections.
- Lead with the observable effect on type checking or editor behavior. Preserve diagnostic names,
    configuration keys, and the conditions under which a diagnostic, inference result, or editor
    feature changes.
- Link the names of language server and third-party library features to the relevant sections of
    their official documentation when you can verify the destination. Use web search when local
    references do not establish the URL.
    For language server features, prefer Microsoft's official Language Server Protocol specification.
    The feature reference table in `docs/features/language-server.md` lists specification URLs.
    For third-party library features, use the library's own documentation. For example, link
    [signature help](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_signatureHelp)
    and Pydantic's
    [field validators](https://pydantic.dev/docs/validation/latest/concepts/validators/#field-validators).
- Keep updates to bundled Typeshed stubs, including any attached comparison link. Keep references to
    Ruff and ty PRs distinct when they have the same number.
