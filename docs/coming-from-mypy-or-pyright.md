# Coming from mypy or pyright

This guide helps you migrate a project from
[mypy](https://mypy.readthedocs.io/en/stable/) or
[pyright](https://microsoft.github.io/pyright/) to ty.

## Migration tips

- mypy disables an error code with `# type: ignore[code]`; pyright suppresses a single line with
    `# pyright: ignore[reportXyz]`; ty's equivalent is `# ty: ignore[rule]`.
    See [this page](suppression.md) for more information about suppression comments.
- mypy's `disable_error_code` and pyright's `reportXyz = "none"` both correspond to setting
    `<rule> = "ignore"` under `[tool.ty.rules]`. See [this section](reference/configuration.md#rules) for
    details.
- Severities in ty are `ignore`, `warn`, `error`. Pyright's `"information"` and `"hint"` levels have
    no direct ty equivalent — use `warn` for both.
- If you are looking for the equivalent of `disallow_untyped_defs` / `no-untyped-def` (mypy) or `reportMissingParameterType`,
    `reportUnknownParameterType` (pyright), check out this
    [FAQ entry](reference/typing-faq.md#why-doesnt-ty-warn-about-missing-type-annotations).

## How to read this table

- **ty rule**: the canonical name, as listed in [Rules](reference/rules.md). Configure under
    `[tool.ty.rules]`.
- **mypy error code**: the value passed to `# type: ignore[<code>]` or `disable_error_code`. Some ty
    rules surface as one of mypy's catch-all codes (`misc`, `assignment`, `valid-type`); these
    mappings are deliberately broad.
- **pyright diagnostic**: the `report*` setting in `pyrightconfig.json` or `[tool.pyright]`.

A blank cell means no direct equivalent exists in that checker (the diagnostic is either not
emitted, or is folded into a broader category that already appears for another ty rule).

## Mapping table

| ty rule                         | mypy error code                                         | pyright diagnostic                                           |
| ------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------ |
| `call-abstract-method`          |                                                         | `reportAbstractUsage`                                        |
| `call-non-callable`             | `operator`                                              | `reportCallIssue`                                            |
| `conflicting-declarations`      | `no-redef`                                              | `reportRedeclaration`                                        |
| `conflicting-metaclass`         | `metaclass`                                             | `reportGeneralTypeIssues`                                    |
| `cyclic-class-definition`       | `misc`                                                  | `reportGeneralTypeIssues`                                    |
| `deprecated`                    | `deprecated`                                            | `reportDeprecated`                                           |
| `division-by-zero`              |                                                         |                                                              |
| `duplicate-base`                | `misc`                                                  | `reportGeneralTypeIssues`                                    |
| `empty-body`                    | `empty-body`                                            |                                                              |
| `inconsistent-mro`              | `misc`                                                  | `reportGeneralTypeIssues`                                    |
| `index-out-of-bounds`           | `misc`                                                  | `reportGeneralTypeIssues`                                    |
| `invalid-argument-type`         | `arg-type`<br>`index`<br>`type-var`<br>`typeddict-item` | `reportArgumentType`<br>`reportAssignmentType`               |
| `invalid-assignment`            | `assignment`                                            | `reportAssignmentType`                                       |
| `invalid-attribute-access`      | `misc`                                                  | `reportAttributeAccessIssue`                                 |
| `invalid-await`                 | `misc`                                                  | `reportGeneralTypeIssues`                                    |
| `invalid-base`                  | `valid-type`                                            | `reportGeneralTypeIssues`                                    |
| `invalid-context-manager`       | `misc`<br>`attr-defined`                                | `reportGeneralTypeIssues`                                    |
| `invalid-exception-caught`      | `misc`                                                  | `reportGeneralTypeIssues`                                    |
| `invalid-key`                   | `typeddict-item`<br>`typeddict-unknown-key`             | `reportAssignmentType`                                       |
| `invalid-metaclass`             | `metaclass`                                             |                                                              |
| `invalid-method-override`       | `override`                                              | `reportIncompatibleMethodOverride`                           |
| `invalid-overload`              | `no-overload-impl`                                      | `reportNoOverloadImplementation`                             |
| `invalid-parameter-default`     | `assignment`                                            | `reportArgumentType`                                         |
| `invalid-raise`                 | `misc`                                                  | `reportGeneralTypeIssues`                                    |
| `invalid-return-type`           | `return-value`                                          | `reportReturnType`                                           |
| `invalid-type-arguments`        | `misc`<br>`type-var`                                    | `reportInvalidTypeArguments`                                 |
| `invalid-type-form`             | `valid-type`                                            | `reportInvalidTypeForm`                                      |
| `missing-argument`              | `call-arg`                                              | `reportCallIssue`                                            |
| `missing-override-decorator`    | `explicit-override`                                     | `reportImplicitOverride`                                     |
| `missing-typed-dict-key`        | `typeddict-item`                                        | `reportAssignmentType`                                       |
| `no-matching-overload`          | `call-overload`                                         | `reportCallIssue`                                            |
| `not-iterable`                  | `misc`<br>`attr-defined`                                | `reportGeneralTypeIssues`                                    |
| `not-subscriptable`             | `index`                                                 | `reportIndexIssue`                                           |
| `parameter-already-assigned`    | `misc`<br>`call-arg`                                    | `reportCallIssue`                                            |
| `possibly-missing-attribute`    | `union-attr`                                            | `reportOptionalMemberAccess`<br>`reportAttributeAccessIssue` |
| `possibly-unresolved-reference` | `possibly-undefined`                                    | `reportPossiblyUnboundVariable`                              |
| `redundant-cast`                | `redundant-cast`                                        | `reportUnnecessaryCast`                                      |
| `too-many-positional-arguments` | `call-arg`                                              | `reportCallIssue`                                            |
| `type-assertion-failure`        | `assert-type`                                           | `reportAssertTypeFailure`                                    |
| `undefined-reveal`              | `unimported-reveal`                                     |                                                              |
| `unknown-argument`              | `call-arg`                                              | `reportCallIssue`                                            |
| `unresolved-attribute`          | `attr-defined`                                          | `reportAttributeAccessIssue`                                 |
| `unresolved-import`             | `import-not-found`                                      | `reportMissingImports`                                       |
| `unresolved-reference`          | `name-defined`                                          | `reportUndefinedVariable`                                    |
| `unsupported-operator`          | `operator`                                              | `reportOperatorIssue`                                        |
| `unused-awaitable`              | `unused-coroutine`<br>`unused-awaitable`                | `reportUnusedCoroutine`                                      |
| `unused-ignore-comment`         | `unused-ignore`                                         | `reportUnnecessaryTypeIgnoreComment`                         |

The full list of ty rules — including those without a direct equivalent above — is in
[Rules](reference/rules.md). Contributions to extend this mapping are welcome via pull request to the
[`ty` repository](https://github.com/astral-sh/ty); see issue
[#2111](https://github.com/astral-sh/ty/issues/2111) for context.
