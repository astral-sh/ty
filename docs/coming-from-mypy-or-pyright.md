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
- Unlike mypy, ty checks the bodies of unannotated functions unconditionally, so there is no ty rule
    corresponding to mypy's `check_untyped_defs` setting. The equivalent pyright setting is
    `analyzeUnannotatedFunctions = true`.

## How to read this table

- **ty or Ruff rule**: the canonical name, as listed in [Rules](reference/rules.md) if it is a ty
    rule. Configure ty rules under `[tool.ty.rules]`. Where Ruff provides equivalent coverage for a
    check that has no ty rule, the relevant Ruff rule or rule group is linked instead.
- **mypy error code**: the value passed to `# type: ignore[<code>]` or `disable_error_code`. Some ty
    rules surface as one of mypy's catch-all codes (`misc`, `assignment`, `valid-type`); these
    mappings are deliberately broad.
- **pyright diagnostic**: the `report*` setting in `pyrightconfig.json` or `[tool.pyright]`.

A blank cell means no direct equivalent exists in that checker (the diagnostic is either not
emitted, or is folded into a broader category that already appears for another ty rule).

## Mapping table

| ty or Ruff rule                                                                                                              | mypy error code                                         | pyright diagnostic                                           |
| ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------ |
| `call-abstract-method`                                                                                                       |                                                         | `reportAbstractUsage`                                        |
| `call-non-callable`                                                                                                          | `operator`                                              | `reportCallIssue`                                            |
| `conflicting-declarations`                                                                                                   | `no-redef`                                              | `reportRedeclaration`                                        |
| `conflicting-metaclass`                                                                                                      | `metaclass`                                             | `reportGeneralTypeIssues`                                    |
| `cyclic-class-definition`                                                                                                    | `misc`                                                  | `reportGeneralTypeIssues`                                    |
| `deprecated`                                                                                                                 | `deprecated`                                            | `reportDeprecated`                                           |
| `division-by-zero`                                                                                                           |                                                         |                                                              |
| `duplicate-base`                                                                                                             | `misc`                                                  | `reportGeneralTypeIssues`                                    |
| `empty-body`                                                                                                                 | `empty-body`                                            |                                                              |
| `inconsistent-mro`                                                                                                           | `misc`                                                  | `reportGeneralTypeIssues`                                    |
| `index-out-of-bounds`                                                                                                        | `misc`                                                  | `reportGeneralTypeIssues`                                    |
| `invalid-argument-type`                                                                                                      | `arg-type`<br>`index`<br>`type-var`<br>`typeddict-item` | `reportArgumentType`<br>`reportAssignmentType`               |
| `invalid-assignment`                                                                                                         | `assignment`                                            | `reportAssignmentType`                                       |
| `invalid-attribute-access`                                                                                                   | `misc`                                                  | `reportAttributeAccessIssue`                                 |
| `invalid-await`                                                                                                              | `misc`                                                  | `reportGeneralTypeIssues`                                    |
| `invalid-base`                                                                                                               | `valid-type`                                            | `reportGeneralTypeIssues`                                    |
| `invalid-context-manager`                                                                                                    | `misc`<br>`attr-defined`                                | `reportGeneralTypeIssues`                                    |
| `invalid-exception-caught`                                                                                                   | `misc`                                                  | `reportGeneralTypeIssues`                                    |
| `invalid-key`                                                                                                                | `typeddict-item`<br>`typeddict-unknown-key`             | `reportAssignmentType`                                       |
| `invalid-metaclass`                                                                                                          | `metaclass`                                             |                                                              |
| `invalid-method-override`                                                                                                    | `override`                                              | `reportIncompatibleMethodOverride`                           |
| `invalid-overload`                                                                                                           | `no-overload-impl`                                      | `reportNoOverloadImplementation`                             |
| `invalid-parameter-default`                                                                                                  | `assignment`                                            | `reportArgumentType`                                         |
| `invalid-raise`                                                                                                              | `misc`                                                  | `reportGeneralTypeIssues`                                    |
| `invalid-return-type`                                                                                                        | `return-value`                                          | `reportReturnType`                                           |
| `invalid-type-arguments`                                                                                                     | `misc`<br>`type-var`                                    | `reportInvalidTypeArguments`                                 |
| `invalid-type-form`                                                                                                          | `valid-type`                                            | `reportInvalidTypeForm`                                      |
| `missing-argument`                                                                                                           | `call-arg`                                              | `reportCallIssue`                                            |
| `missing-override-decorator`                                                                                                 | `explicit-override`                                     | `reportImplicitOverride`                                     |
| `missing-type-argument`                                                                                                      | `type-arg`                                              | `reportMissingTypeArgument`                                  |
| `missing-typed-dict-key`                                                                                                     | `typeddict-item`                                        | `reportAssignmentType`                                       |
| `no-matching-overload`                                                                                                       | `call-overload`                                         | `reportCallIssue`                                            |
| `not-iterable`                                                                                                               | `misc`<br>`attr-defined`                                | `reportGeneralTypeIssues`                                    |
| `not-subscriptable`                                                                                                          | `index`                                                 | `reportIndexIssue`                                           |
| `parameter-already-assigned`                                                                                                 | `misc`<br>`call-arg`                                    | `reportCallIssue`                                            |
| `possibly-missing-attribute`                                                                                                 | `union-attr`                                            | `reportOptionalMemberAccess`<br>`reportAttributeAccessIssue` |
| `possibly-unresolved-reference`                                                                                              | `possibly-undefined`                                    | `reportPossiblyUnboundVariable`                              |
| `redundant-cast`                                                                                                             | `redundant-cast`                                        | `reportUnnecessaryCast`                                      |
| `too-many-positional-arguments`                                                                                              | `call-arg`                                              | `reportCallIssue`                                            |
| `type-assertion-failure`                                                                                                     | `assert-type`                                           | `reportAssertTypeFailure`                                    |
| `undefined-reveal`                                                                                                           | `unimported-reveal`                                     |                                                              |
| `unknown-argument`                                                                                                           | `call-arg`                                              | `reportCallIssue`                                            |
| `unresolved-attribute`                                                                                                       | `attr-defined`                                          | `reportAttributeAccessIssue`                                 |
| `unresolved-import`                                                                                                          | `import-not-found`                                      | `reportMissingImports`                                       |
| `unresolved-reference`                                                                                                       | `name-defined`                                          | `reportUndefinedVariable`                                    |
| `unsupported-operator`                                                                                                       | `operator`                                              | `reportOperatorIssue`                                        |
| `unused-awaitable`                                                                                                           | `unused-coroutine`<br>`unused-awaitable`                | `reportUnusedCoroutine`                                      |
| `unused-ignore-comment`                                                                                                      | `unused-ignore`                                         | `reportUnnecessaryTypeIgnoreComment`                         |
| None yet (tracked in [Ruff #10137][ruff-10137])                                                                              |                                                         | `reportConstantRedefinition`                                 |
| [Ruff `F811`][ruff-f811]<br>[Ruff `I001`][ruff-i001]                                                                         |                                                         | `reportDuplicateImport`                                      |
| None yet (tracked in [#3647][ty-3647])                                                                                       |                                                         | `reportImportCycles`                                         |
| None yet                                                                                                                     |                                                         | `reportIncompleteStub`                                       |
| None yet (tracked in [#3651][ty-3651])                                                                                       |                                                         | `reportInconsistentConstructor`                              |
| [Ruff `W605`][ruff-w605]                                                                                                     |                                                         | `reportInvalidStringEscapeSequence`                          |
| [Ruff `PYI010`][ruff-pyi010]<br>[Ruff `PYI017`][ruff-pyi017]<br>[Ruff `PYI048`][ruff-pyi048]<br>[Ruff `PYI052`][ruff-pyi052] |                                                         | `reportInvalidStubStatement`                                 |
| None yet (tracked in [#1017][ty-1017], [#3636][ty-3636], and [#3637][ty-3637])                                               | `type-var`                                              | `reportInvalidTypeVarUse`                                    |
| None yet (tracked in [#1060][ty-1060])                                                                                       | `exhaustive-match`                                      | `reportMatchNotExhaustive`                                   |
| None yet (tracked in [#1577][ty-1577])                                                                                       |                                                         | `reportMissingModuleSource`                                  |
| None yet (tracked in [#3652][ty-3652])                                                                                       |                                                         | `reportMissingSuperCall`                                     |
| None yet (tracked in [#3638][ty-3638])                                                                                       | `import-untyped`                                        | `reportMissingTypeStubs`                                     |
| None yet (tracked in [#103][ty-103])                                                                                         | `overload-overlap`                                      | `reportOverlappingOverload`                                  |
| None yet (tracked in [#200][ty-200])                                                                                         | `attr-defined` (extended by `--no-implicit-reexport`)   | `reportPrivateImportUsage`                                   |
| None yet (tracked in [#3633][ty-3633])                                                                                       |                                                         | `reportPropertyTypeMismatch`                                 |
| [Ruff `N804`][ruff-n804]<br>[Ruff `N805`][ruff-n805]                                                                         |                                                         | `reportSelfClsParameterName`                                 |
| [Ruff `PYI033`][ruff-pyi033] (stubs only)                                                                                    |                                                         | `reportTypeCommentUsage`                                     |
| None yet (tracked in [#2810][ty-2810])                                                                                       |                                                         | `reportTypedDictNotRequiredAccess`                           |
| None yet (tracked in [#2954][ty-2954])                                                                                       |                                                         | `reportUninitializedInstanceVariable`                        |
| None yet (tracked in [#576][ty-576])                                                                                         | `comparison-overlap`                                    | `reportUnnecessaryComparison`<br>`reportUnnecessaryContains` |
| None yet (tracked in [#1948][ty-1948])                                                                                       | `unreachable`                                           | `reportUnreachable`                                          |
| [Ruff `F822`][ruff-f822]<br>[Ruff `PLE0604`][ruff-ple0604]<br>[Ruff `PLE0605`][ruff-ple0605]<br>[Ruff `PYI056`][ruff-pyi056] |                                                         | `reportUnsupportedDunderAll`                                 |
| [Ruff `PYI024`][ruff-pyi024]                                                                                                 |                                                         | `reportUntypedNamedTuple`                                    |
| [Ruff `B018`][ruff-b018]                                                                                                     |                                                         | `reportUnusedExpression`                                     |
| [Ruff `F403`][ruff-f403]                                                                                                     |                                                         | `reportWildcardImportFromLibrary`                            |
| None yet                                                                                                                     | `no-any-return`                                         |                                                              |
| None yet                                                                                                                     | `no-untyped-call`                                       |                                                              |
| [Ruff `ANN` rules][ruff-ann]                                                                                                 | `no-untyped-def`                                        | `reportMissingParameterType`<br>`reportUnknownParameterType` |
| None yet                                                                                                                     | `untyped-decorator`                                     | `reportUntypedFunctionDecorator`                             |

The full list of ty rules — including those without a direct equivalent above — is in
[Rules](reference/rules.md). Contributions to extend this mapping are welcome via pull request to the
[`ty` repository](https://github.com/astral-sh/ty); see issue
[#2111](https://github.com/astral-sh/ty/issues/2111) for context.

[ruff-10137]: https://github.com/astral-sh/ruff/issues/10137
[ruff-ann]: https://docs.astral.sh/ruff/rules/#flake8-annotations-ann
[ruff-b018]: https://docs.astral.sh/ruff/rules/useless-expression/
[ruff-f403]: https://docs.astral.sh/ruff/rules/undefined-local-with-import-star/
[ruff-f811]: https://docs.astral.sh/ruff/rules/redefined-while-unused/
[ruff-f822]: https://docs.astral.sh/ruff/rules/undefined-export/
[ruff-i001]: https://docs.astral.sh/ruff/rules/unsorted-imports/
[ruff-n804]: https://docs.astral.sh/ruff/rules/invalid-first-argument-name-for-class-method/
[ruff-n805]: https://docs.astral.sh/ruff/rules/invalid-first-argument-name-for-method/
[ruff-ple0604]: https://docs.astral.sh/ruff/rules/invalid-all-object/
[ruff-ple0605]: https://docs.astral.sh/ruff/rules/invalid-all-format/
[ruff-pyi010]: https://docs.astral.sh/ruff/rules/non-empty-stub-body/
[ruff-pyi017]: https://docs.astral.sh/ruff/rules/complex-assignment-in-stub/
[ruff-pyi024]: https://docs.astral.sh/ruff/rules/collections-named-tuple/
[ruff-pyi033]: https://docs.astral.sh/ruff/rules/type-comment-in-stub/
[ruff-pyi048]: https://docs.astral.sh/ruff/rules/stub-body-multiple-statements/
[ruff-pyi052]: https://docs.astral.sh/ruff/rules/unannotated-assignment-in-stub/
[ruff-pyi056]: https://docs.astral.sh/ruff/rules/unsupported-method-call-on-all/
[ruff-w605]: https://docs.astral.sh/ruff/rules/invalid-escape-sequence/
[ty-1017]: https://github.com/astral-sh/ty/issues/1017
[ty-103]: https://github.com/astral-sh/ty/issues/103
[ty-1060]: https://github.com/astral-sh/ty/issues/1060
[ty-1577]: https://github.com/astral-sh/ty/issues/1577
[ty-1948]: https://github.com/astral-sh/ty/issues/1948
[ty-200]: https://github.com/astral-sh/ty/issues/200
[ty-2810]: https://github.com/astral-sh/ty/issues/2810
[ty-2954]: https://github.com/astral-sh/ty/issues/2954
[ty-3633]: https://github.com/astral-sh/ty/issues/3633
[ty-3636]: https://github.com/astral-sh/ty/issues/3636
[ty-3637]: https://github.com/astral-sh/ty/issues/3637
[ty-3638]: https://github.com/astral-sh/ty/issues/3638
[ty-3647]: https://github.com/astral-sh/ty/issues/3647
[ty-3651]: https://github.com/astral-sh/ty/issues/3651
[ty-3652]: https://github.com/astral-sh/ty/issues/3652
[ty-576]: https://github.com/astral-sh/ty/issues/576
