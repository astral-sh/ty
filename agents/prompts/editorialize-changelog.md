- For `astral-sh/ruff` entries, get the old and new submodule commits with `git rev-parse HEAD^:ruff`
    and `git rev-parse HEAD:ruff` in the ty checkout. Use `git -C ruff log` and `git -C ruff show`
    to inspect changes in that range. Use ty's own history for `astral-sh/ty` entries.
- Follow ty's section names and order as defined by `[tool.rooster.section-labels]` in
    `pyproject.toml`. Keep explicitly categorized entries in their generated sections.
- Lead with the observable effect on type checking or editor behavior. Preserve diagnostic names,
    configuration keys, and the conditions under which a diagnostic, inference result, or editor
    feature changes.
- When an entry names a feature of the language server or of a third-party library, link the
    feature name to the relevant section of the published docs if you can establish the URL from
    local sources.
    For language server features, prefer Microsoft's official Language Server Protocol specification.
    Use the feature reference table in `docs/features/language-server.md` to find the specification URL.
    For third-party library features, look for links to the library's own docs in ty's docs and
    previous changelog entries. For example, link
    [signature help](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_signatureHelp)
    and Pydantic's
    [field validators](https://pydantic.dev/docs/validation/latest/concepts/validators/#field-validators).
- Keep updates to bundled Typeshed stubs, including any attached comparison link. Keep references to
    Ruff and ty PRs distinct when they have the same number.
