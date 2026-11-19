Write a replacement for the newest ty release section in `CHANGELOG.md`. It starts at the first
`##` heading and ends immediately before the next `##` heading.

Read the generated section, several preceding releases, and the local Git history. For
`astral-sh/ruff` entries, inspect the commits in the supplied submodule range with `git -C ruff log`
and `git -C ruff show`. Use ty's own history for `astral-sh/ty` entries. Treat those sources as
evidence for the notes. Work from local files and history without editing files or using the
network.

- Keep the original release heading and date. Copy the `Contributors` section verbatim.
- Follow ty's section names and order as defined by `[tool.rooster.section-labels]` in
    `pyproject.toml`. Keep explicitly categorized entries in their generated sections, including
    `Breaking changes`, `Bug fixes`, `Diagnostic improvements`, `LSP server`, and
    `Memory usage improvements`. Move an `Other changes` entry when it clearly fits an established
    section.
- Lead with the observable effect on type checking or editor behavior. Preserve diagnostic names,
    configuration keys, and the conditions under which a diagnostic, inference result, or editor
    feature changes. For `Breaking changes`, preserve the impact and any supported migration guidance.
- Drop changes that clearly affect only CI, tests, or contributor tooling. Keep uncertain entries
    and changes visible to ty users, including updated bundled Typeshed stubs.
- Combine pull requests that implement one user-facing change. Split distinct changes when that
    improves clarity. Preserve the number and exact URL of every retained reference in the existing
    Markdown link format. Keep links to the repository they came from, including when a ty and Ruff
    pull request have the same number. Preserve any Typeshed comparison link attached to a retained
    entry.
- Keep each paragraph and list item on a single physical line. Use concise prose, preserve factual
    qualifiers, put significant changes first within each section, and remove empty sections.

Return only the complete replacement release section, starting with its `##` heading.
