# Rule mapping: mypy and pyright

This page maps ty's lint rules to their closest equivalents in
[mypy](https://mypy.readthedocs.io/en/stable/error_code_list.html) and
[pyright](https://microsoft.github.io/pyright/#/configuration?id=type-check-diagnostics-settings).
It is intended to help users migrating from another type checker translate their existing
configuration (rule disables, severity overrides) into a `pyproject.toml` `[tool.ty.rules]` table.

## How to read this table

- **ty rule**: the canonical name, as listed in [Rules](rules.md). Configure under
  `[tool.ty.rules]`.
- **mypy error code**: the value passed to `# type: ignore[<code>]` or `disable_error_code`. Some ty
  rules surface as one of mypy's catch-all codes (`misc`, `assignment`, `valid-type`); these
  mappings are deliberately broad.
- **pyright diagnostic**: the `report*` setting in `pyrightconfig.json` or `[tool.pyright]`.

A blank cell means no direct equivalent exists in that checker (the diagnostic is either not
emitted, or is folded into a broader category that already appears for another ty rule).

> **Note**: This mapping is best-effort and based on the public documentation of each checker as of
> the page's last update. Behavior at the edges (what triggers a diagnostic, severity defaults,
> suppression scope) differs between checkers. When in doubt, consult each project's own
> documentation:
>
> - mypy error codes: <https://mypy.readthedocs.io/en/stable/error_code_list.html>
> - pyright diagnostic settings:
>   <https://microsoft.github.io/pyright/#/configuration?id=type-check-diagnostics-settings>

## Migration tips

- mypy disables an error code with `# type: ignore[code]`; ty's equivalent is `# ty: ignore[rule]`.
  See [Suppression](../suppression.md).
- pyright suppresses a single line with `# pyright: ignore[reportName]`; ty's equivalent is
  `# ty: ignore[rule]`.
- mypy's `disable_error_code` and pyright's `reportXxx = "none"` both correspond to setting
  `<rule> = "ignore"` under `[tool.ty.rules]`.
- Severities in ty are `ignore`, `warn`, `error`. Pyright's `"information"` and `"hint"` levels have
  no direct ty equivalent — use `warn` for both.

## Mapping table

| ty rule                         | mypy error code      | pyright diagnostic                   |
| ------------------------------- | -------------------- | ------------------------------------ |
| `call-non-callable`             | `operator`           | `reportCallIssue`                    |
| `conflicting-declarations`      | `no-redef`           | `reportRedeclaration`                |
| `cyclic-class-definition`       | `misc`               | `reportGeneralTypeIssues`            |
| `division-by-zero`              |                      |                                      |
| `duplicate-base`                | `misc`               | `reportGeneralTypeIssues`            |
| `empty-body`                    | `empty-body`         | `reportGeneralTypeIssues`            |
| `inconsistent-mro`              | `misc`               | `reportGeneralTypeIssues`            |
| `index-out-of-bounds`           |                      |                                      |
| `invalid-argument-type`         | `arg-type`           | `reportArgumentType`                 |
| `invalid-assignment`            | `assignment`         | `reportAssignmentType`               |
| `invalid-attribute-access`      | `assignment`         | `reportAttributeAccessIssue`         |
| `invalid-await`                 | `misc`               | `reportGeneralTypeIssues`            |
| `invalid-base`                  | `misc`               | `reportGeneralTypeIssues`            |
| `invalid-context-manager`       | `misc`               | `reportGeneralTypeIssues`            |
| `invalid-exception-caught`      | `misc`               | `reportGeneralTypeIssues`            |
| `invalid-method-override`       | `override`           | `reportIncompatibleMethodOverride`   |
| `invalid-parameter-default`     | `assignment`         | `reportArgumentType`                 |
| `invalid-raise`                 | `misc`               | `reportGeneralTypeIssues`            |
| `invalid-return-type`           | `return-value`       | `reportReturnType`                   |
| `invalid-type-form`             | `valid-type`         | `reportInvalidTypeForm`              |
| `missing-argument`              | `call-arg`           | `reportCallIssue`                    |
| `no-matching-overload`          | `call-overload`      | `reportCallIssue`                    |
| `not-iterable`                  | `misc`               | `reportGeneralTypeIssues`            |
| `parameter-already-assigned`    | `call-arg`           | `reportCallIssue`                    |
| `possibly-missing-attribute`    | `union-attr`         | `reportOptionalMemberAccess`         |
| `possibly-unresolved-reference` | `possibly-undefined` | `reportPossiblyUnboundVariable`      |
| `redundant-cast`                | `redundant-cast`     |                                      |
| `too-many-positional-arguments` | `call-arg`           | `reportCallIssue`                    |
| `type-assertion-failure`        | `assert-type`        | `reportAssertTypeFailure`            |
| `undefined-reveal`              |                      |                                      |
| `unknown-argument`              | `call-arg`           | `reportCallIssue`                    |
| `unresolved-attribute`          | `attr-defined`       | `reportAttributeAccessIssue`         |
| `unresolved-import`             | `import-not-found`   | `reportMissingImports`               |
| `unresolved-reference`          | `name-defined`       | `reportUndefinedVariable`            |
| `unsupported-operator`          | `operator`           | `reportOperatorIssue`                |
| `unused-ignore-comment`         | `unused-ignore`      | `reportUnnecessaryTypeIgnoreComment` |

The full list of ty rules — including those without a direct equivalent above — is in
[Rules](rules.md). Contributions to extend this mapping are welcome via pull request to the
[`ty` repository](https://github.com/astral-sh/ty); see issue
[#2111](https://github.com/astral-sh/ty/issues/2111) for context.
