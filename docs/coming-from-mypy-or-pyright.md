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

## Stricter checking with ty

For both mypy and pyright, "strict" mode enables several error codes that are otherwise disabled by
default, but also makes fundamental changes to the way type inference and type checking works.
Mypy's strict mode includes `--check-untyped-defs`, for example, without which unannotated
functions are left unchecked; pyright's strict mode includes `strictListInference`, without which
`[1, "foo"]` will be inferred as having type `list[Unknown]` rather than `list[int | str]` or
similar.

ty's default mode is currently stricter by default than either mypy or pyright in many ways. ty
does not have flags such as `--check-untyped-defs` or `strictListInference`, because these are
ty's default behaviour and are not currently configurable. Meanwhile, nearly all ty rules are
enabled by default, and the ones that are disabled by default are usually in that category because
they are either very opinionated or have many false positives.

### Recommended configuration

To enable all ty rules at once with the `error` severity, you can simply use `--error=all`, but we
wouldn't recommend it. Instead, you can currently approximate something similar to the `--strict`
mode of other type checkers with the following configuration:

```toml
[tool.ty.terminal]
error-on-warning = true

[tool.ty.rules]
missing-type-argument = "error"
possibly-unresolved-reference = "warn"

[tool.ruff.lint]
extend-select = ["ANN", "PYI"]
preview = true
```

This configuration:

- Ensures ty exits with a non-zero status if it emits any warning-level diagnostics
- Enables ty's disabled-by-default [`missing-type-argument`](https://docs.astral.sh/ty/reference/rules/#missing-type-argument) and [`possibly-unresolved-reference`](https://docs.astral.sh/ty/reference/rules/#possibly-unresolved-reference) rules
- Extends Ruff's default rules with the [`ANN`](https://docs.astral.sh/ruff/rules/#flake8-annotations-ann) and [`PYI`](https://docs.astral.sh/ruff/rules/#flake8-pyi-pyi) rule categories, both of which are focussed on type-annotating your code more effectively
- Enables Ruff's preview mode so that `PYI033` also checks `.py` files

Note that several checks in mypy and pyright are not yet implemented in ty. See the rule mapping
table below for more details.

## Mapping pyright/mypy rules to ty/Ruff rules

### How to read this table

- **ty or Ruff rule**: the canonical name, as listed in [Rules](reference/rules.md) if it is a ty
    rule. Configure ty rules under `[tool.ty.rules]`. Where Ruff provides equivalent coverage for a
    check that has no ty rule, the relevant Ruff rule or rule group is linked instead.
- **mypy error code**: the value passed to `# type: ignore[<code>]` or `disable_error_code`. Some ty
    rules surface as one of mypy's catch-all codes (`misc`, `assignment`, `valid-type`); these
    mappings are deliberately broad.
- **pyright diagnostic**: the `report*` setting in `pyrightconfig.json` or `[tool.pyright]`.

A blank cell means no direct equivalent exists in that checker (the diagnostic is either not
emitted, or is folded into a broader category that already appears for another ty rule).

### Rules

| ty or Ruff rule                                                                                                              | mypy error code                                                                                                                | pyright diagnostic                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| [`call-abstract-method`][ty-call-abstract-method]                                                                            |                                                                                                                                | [`reportAbstractUsage`][reportabstractusage]                                                                             |
| [`call-non-callable`][ty-call-non-callable]                                                                                  | [`operator`][mypy-operator]                                                                                                    | [`reportCallIssue`][reportcallissue]                                                                                     |
| [`conflicting-declarations`][ty-conflicting-declarations]                                                                    | [`no-redef`][mypy-no-redef]                                                                                                    | [`reportRedeclaration`][reportredeclaration]                                                                             |
| [`conflicting-metaclass`][ty-conflicting-metaclass]                                                                          | [`metaclass`][mypy-metaclass]                                                                                                  | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                     |
| [`cyclic-class-definition`][ty-cyclic-class-definition]                                                                      | [`misc`][mypy-misc]                                                                                                            | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                     |
| [`deprecated`][ty-deprecated]                                                                                                | [`deprecated`][mypy-deprecated]                                                                                                | [`reportDeprecated`][reportdeprecated]                                                                                   |
| [`division-by-zero`][ty-division-by-zero]                                                                                    |                                                                                                                                |                                                                                                                          |
| [`duplicate-base`][ty-duplicate-base]                                                                                        | [`misc`][mypy-misc]                                                                                                            | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                     |
| [`empty-body`][ty-empty-body]                                                                                                | [`empty-body`][mypy-empty-body]                                                                                                |                                                                                                                          |
| [`inconsistent-mro`][ty-inconsistent-mro]                                                                                    | [`misc`][mypy-misc]                                                                                                            | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                     |
| [`index-out-of-bounds`][ty-index-out-of-bounds]                                                                              | [`misc`][mypy-misc]                                                                                                            | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                     |
| [`invalid-argument-type`][ty-invalid-argument-type]                                                                          | [`arg-type`][mypy-arg-type]<br>[`index`][mypy-index]<br>[`type-var`][mypy-type-var]<br>[`typeddict-item`][mypy-typeddict-item] | [`reportArgumentType`][reportargumenttype]<br>[`reportAssignmentType`][reportassignmenttype]                             |
| [`invalid-assignment`][ty-invalid-assignment]                                                                                | [`assignment`][mypy-assignment]                                                                                                | [`reportAssignmentType`][reportassignmenttype]                                                                           |
| [`invalid-attribute-access`][ty-invalid-attribute-access]                                                                    | [`misc`][mypy-misc]                                                                                                            | [`reportAttributeAccessIssue`][reportattributeaccessissue]                                                               |
| [`invalid-await`][ty-invalid-await]                                                                                          | [`misc`][mypy-misc]                                                                                                            | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                     |
| [`invalid-base`][ty-invalid-base]                                                                                            | [`valid-type`][mypy-valid-type]                                                                                                | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                     |
| [`invalid-context-manager`][ty-invalid-context-manager]                                                                      | [`misc`][mypy-misc]<br>[`attr-defined`][mypy-attr-defined]                                                                     | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                     |
| [`invalid-exception-caught`][ty-invalid-exception-caught]                                                                    | [`misc`][mypy-misc]                                                                                                            | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                     |
| [`invalid-key`][ty-invalid-key]                                                                                              | [`typeddict-item`][mypy-typeddict-item]<br>[`typeddict-unknown-key`][mypy-typeddict-unknown-key]                               | [`reportAssignmentType`][reportassignmenttype]                                                                           |
| [`invalid-metaclass`][ty-invalid-metaclass]                                                                                  | [`metaclass`][mypy-metaclass]                                                                                                  |                                                                                                                          |
| [`invalid-method-override`][ty-invalid-method-override]                                                                      | [`override`][mypy-override]                                                                                                    | [`reportIncompatibleMethodOverride`][reportincompatiblemethodoverride]                                                   |
| [`invalid-overload`][ty-invalid-overload]                                                                                    | [`no-overload-impl`][mypy-no-overload-impl]                                                                                    | [`reportNoOverloadImplementation`][reportnooverloadimplementation]                                                       |
| [`invalid-parameter-default`][ty-invalid-parameter-default]                                                                  | [`assignment`][mypy-assignment]                                                                                                | [`reportArgumentType`][reportargumenttype]                                                                               |
| [`invalid-raise`][ty-invalid-raise]                                                                                          | [`misc`][mypy-misc]                                                                                                            | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                     |
| [`invalid-return-type`][ty-invalid-return-type]                                                                              | [`return-value`][mypy-return-value]                                                                                            | [`reportReturnType`][reportreturntype]                                                                                   |
| [`invalid-type-arguments`][ty-invalid-type-arguments]                                                                        | [`misc`][mypy-misc]<br>[`type-var`][mypy-type-var]                                                                             | [`reportInvalidTypeArguments`][reportinvalidtypearguments]                                                               |
| [`invalid-type-form`][ty-invalid-type-form]                                                                                  | [`valid-type`][mypy-valid-type]                                                                                                | [`reportInvalidTypeForm`][reportinvalidtypeform]                                                                         |
| [`missing-argument`][ty-missing-argument]                                                                                    | [`call-arg`][mypy-call-arg]                                                                                                    | [`reportCallIssue`][reportcallissue]                                                                                     |
| [`missing-override-decorator`][ty-missing-override-decorator]                                                                | [`explicit-override`][mypy-explicit-override]                                                                                  | [`reportImplicitOverride`][reportimplicitoverride]                                                                       |
| [`missing-type-argument`][ty-missing-type-argument]                                                                          | [`type-arg`][mypy-type-arg]                                                                                                    | [`reportMissingTypeArgument`][reportmissingtypeargument]                                                                 |
| [`missing-typed-dict-key`][ty-missing-typed-dict-key]                                                                        | [`typeddict-item`][mypy-typeddict-item]                                                                                        | [`reportAssignmentType`][reportassignmenttype]                                                                           |
| [`no-matching-overload`][ty-no-matching-overload]                                                                            | [`call-overload`][mypy-call-overload]                                                                                          | [`reportCallIssue`][reportcallissue]                                                                                     |
| [`not-iterable`][ty-not-iterable]                                                                                            | [`misc`][mypy-misc]<br>[`attr-defined`][mypy-attr-defined]                                                                     | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                     |
| [`not-subscriptable`][ty-not-subscriptable]                                                                                  | [`index`][mypy-index]                                                                                                          | [`reportIndexIssue`][reportindexissue]                                                                                   |
| [`parameter-already-assigned`][ty-parameter-already-assigned]                                                                | [`misc`][mypy-misc]<br>[`call-arg`][mypy-call-arg]                                                                             | [`reportCallIssue`][reportcallissue]                                                                                     |
| [`possibly-missing-attribute`][ty-possibly-missing-attribute]                                                                |                                                                                                                                |                                                                                                                          |
| [`possibly-unresolved-reference`][ty-possibly-unresolved-reference]                                                          | [`possibly-undefined`][mypy-possibly-undefined]                                                                                | [`reportPossiblyUnboundVariable`][reportpossiblyunboundvariable]                                                         |
| [`redundant-cast`][ty-redundant-cast]                                                                                        | [`redundant-cast`][mypy-redundant-cast]                                                                                        | [`reportUnnecessaryCast`][reportunnecessarycast]                                                                         |
| [`too-many-positional-arguments`][ty-too-many-positional-arguments]                                                          | [`call-arg`][mypy-call-arg]                                                                                                    | [`reportCallIssue`][reportcallissue]                                                                                     |
| [`type-assertion-failure`][ty-type-assertion-failure]                                                                        | [`assert-type`][mypy-assert-type]                                                                                              | [`reportAssertTypeFailure`][reportasserttypefailure]                                                                     |
| [`undefined-reveal`][ty-undefined-reveal]                                                                                    | [`unimported-reveal`][mypy-unimported-reveal]                                                                                  |                                                                                                                          |
| [`unknown-argument`][ty-unknown-argument]                                                                                    | [`call-arg`][mypy-call-arg]                                                                                                    | [`reportCallIssue`][reportcallissue]                                                                                     |
| [`unresolved-attribute`][ty-unresolved-attribute]                                                                            | [`attr-defined`][mypy-attr-defined]<br>[`union-attr`][mypy-union-attr]                                                         | [`reportAttributeAccessIssue`][reportattributeaccessissue]<br>[`reportOptionalMemberAccess`][reportoptionalmemberaccess] |
| [`unresolved-import`][ty-unresolved-import]                                                                                  | [`import-not-found`][mypy-import-not-found]                                                                                    | [`reportMissingImports`][reportmissingimports]                                                                           |
| [`unresolved-reference`][ty-unresolved-reference]                                                                            | [`name-defined`][mypy-name-defined]                                                                                            | [`reportUndefinedVariable`][reportundefinedvariable]                                                                     |
| [`unsupported-operator`][ty-unsupported-operator]                                                                            | [`operator`][mypy-operator]                                                                                                    | [`reportOperatorIssue`][reportoperatorissue]                                                                             |
| [`unused-awaitable`][ty-unused-awaitable]                                                                                    | [`unused-coroutine`][mypy-unused-coroutine]<br>[`unused-awaitable`][mypy-unused-awaitable]                                     | [`reportUnusedCoroutine`][reportunusedcoroutine]                                                                         |
| [`unused-ignore-comment`][ty-unused-ignore-comment]                                                                          | [`unused-ignore`][mypy-unused-ignore]                                                                                          | [`reportUnnecessaryTypeIgnoreComment`][reportunnecessarytypeignorecomment]                                               |
| None yet (tracked in [Ruff #10137][ruff-10137])                                                                              |                                                                                                                                | [`reportConstantRedefinition`][reportconstantredefinition]                                                               |
| [Ruff `F811`][ruff-f811]<br>[Ruff `I001`][ruff-i001]                                                                         |                                                                                                                                | [`reportDuplicateImport`][reportduplicateimport]                                                                         |
| None yet (tracked in [#3647][ty-3647])                                                                                       |                                                                                                                                | [`reportImportCycles`][reportimportcycles]                                                                               |
| None yet                                                                                                                     |                                                                                                                                | [`reportIncompleteStub`][reportincompletestub]                                                                           |
| None yet (tracked in [#3651][ty-3651])                                                                                       |                                                                                                                                | [`reportInconsistentConstructor`][reportinconsistentconstructor]                                                         |
| [Ruff `W605`][ruff-w605]                                                                                                     |                                                                                                                                | [`reportInvalidStringEscapeSequence`][reportinvalidstringescapesequence]                                                 |
| [Ruff `PYI010`][ruff-pyi010]<br>[Ruff `PYI017`][ruff-pyi017]<br>[Ruff `PYI048`][ruff-pyi048]<br>[Ruff `PYI052`][ruff-pyi052] |                                                                                                                                | [`reportInvalidStubStatement`][reportinvalidstubstatement]                                                               |
| None yet (tracked in [#1017][ty-1017], [#3636][ty-3636], [#3637][ty-3637])                                                   | [`type-var`][mypy-type-var]                                                                                                    | [`reportInvalidTypeVarUse`][reportinvalidtypevaruse]                                                                     |
| None yet (tracked in [#1060][ty-1060])                                                                                       | [`exhaustive-match`][mypy-exhaustive-match]                                                                                    | [`reportMatchNotExhaustive`][reportmatchnotexhaustive]                                                                   |
| None yet (tracked in [#1577][ty-1577])                                                                                       |                                                                                                                                | [`reportMissingModuleSource`][reportmissingmodulesource]                                                                 |
| None yet (tracked in [#3652][ty-3652])                                                                                       |                                                                                                                                | [`reportMissingSuperCall`][reportmissingsupercall]                                                                       |
| None yet (tracked in [#3638][ty-3638])                                                                                       | [`import-untyped`][mypy-import-untyped]                                                                                        | [`reportMissingTypeStubs`][reportmissingtypestubs]                                                                       |
| None yet (tracked in [#103][ty-103])                                                                                         | [`overload-overlap`][mypy-overload-overlap]                                                                                    | [`reportOverlappingOverload`][reportoverlappingoverload]                                                                 |
| None yet (tracked in [#200][ty-200])                                                                                         | [`attr-defined`][mypy-attr-defined]<br>(extended by [`--no-implicit-reexport`][mypy-no-implicit-reexport])                     | [`reportPrivateImportUsage`][reportprivateimportusage]                                                                   |
| None yet (tracked in [#3633][ty-3633])                                                                                       |                                                                                                                                | [`reportPropertyTypeMismatch`][reportpropertytypemismatch]                                                               |
| [Ruff `N804`][ruff-n804]<br>[Ruff `N805`][ruff-n805]                                                                         |                                                                                                                                | [`reportSelfClsParameterName`][reportselfclsparametername]                                                               |
| [Ruff `PYI033`][ruff-pyi033] (preview only)                                                                                  |                                                                                                                                | [`reportTypeCommentUsage`][reporttypecommentusage]                                                                       |
| None yet (tracked in [#2810][ty-2810])                                                                                       |                                                                                                                                | [`reportTypedDictNotRequiredAccess`][reporttypeddictnotrequiredaccess]                                                   |
| None yet (tracked in [#2954][ty-2954])                                                                                       |                                                                                                                                | [`reportUninitializedInstanceVariable`][reportuninitializedinstancevariable]                                             |
| None yet (tracked in [#576][ty-576])                                                                                         | [`comparison-overlap`][mypy-comparison-overlap]                                                                                | [`reportUnnecessaryComparison`][reportunnecessarycomparison]<br>[`reportUnnecessaryContains`][reportunnecessarycontains] |
| None yet (tracked in [#1948][ty-1948])                                                                                       | [`unreachable`][mypy-unreachable]                                                                                              | [`reportUnreachable`][reportunreachable]                                                                                 |
| [Ruff `F822`][ruff-f822]<br>[Ruff `PLE0604`][ruff-ple0604]<br>[Ruff `PLE0605`][ruff-ple0605]<br>[Ruff `PYI056`][ruff-pyi056] |                                                                                                                                | [`reportUnsupportedDunderAll`][reportunsupporteddunderall]                                                               |
| [Ruff `PYI024`][ruff-pyi024]                                                                                                 |                                                                                                                                | [`reportUntypedNamedTuple`][reportuntypednamedtuple]                                                                     |
| [Ruff `B018`][ruff-b018]                                                                                                     |                                                                                                                                | [`reportUnusedExpression`][reportunusedexpression]                                                                       |
| [Ruff `F403`][ruff-f403]                                                                                                     |                                                                                                                                | [`reportWildcardImportFromLibrary`][reportwildcardimportfromlibrary]                                                     |
| None yet                                                                                                                     | [`no-any-return`][mypy-no-any-return]                                                                                          |                                                                                                                          |
| None yet                                                                                                                     | [`no-untyped-call`][mypy-no-untyped-call]                                                                                      |                                                                                                                          |
| [Ruff `ANN` rules][ruff-ann]                                                                                                 | [`no-untyped-def`][mypy-no-untyped-def]                                                                                        | [`reportMissingParameterType`][reportmissingparametertype]<br>[`reportUnknownParameterType`][reportunknownparametertype] |
| None yet                                                                                                                     | [`untyped-decorator`][mypy-untyped-decorator]                                                                                  | [`reportUntypedFunctionDecorator`][reportuntypedfunctiondecorator]                                                       |

The full list of ty rules — including those without a direct equivalent above — is in
[Rules](reference/rules.md). Contributions to extend this mapping are welcome via pull request to the
[`ty` repository](https://github.com/astral-sh/ty); see issue
[#2111](https://github.com/astral-sh/ty/issues/2111) for context.

[mypy-arg-type]: https://mypy.readthedocs.io/en/stable/_refs.html#code-arg-type
[mypy-assert-type]: https://mypy.readthedocs.io/en/stable/_refs.html#code-assert-type
[mypy-assignment]: https://mypy.readthedocs.io/en/stable/_refs.html#code-assignment
[mypy-attr-defined]: https://mypy.readthedocs.io/en/stable/_refs.html#code-attr-defined
[mypy-call-arg]: https://mypy.readthedocs.io/en/stable/_refs.html#code-call-arg
[mypy-call-overload]: https://mypy.readthedocs.io/en/stable/_refs.html#code-call-overload
[mypy-comparison-overlap]: https://mypy.readthedocs.io/en/stable/_refs.html#code-comparison-overlap
[mypy-deprecated]: https://mypy.readthedocs.io/en/stable/_refs.html#code-deprecated
[mypy-empty-body]: https://mypy.readthedocs.io/en/stable/_refs.html#code-empty-body
[mypy-exhaustive-match]: https://mypy.readthedocs.io/en/stable/_refs.html#code-exhaustive-match
[mypy-explicit-override]: https://mypy.readthedocs.io/en/stable/_refs.html#code-explicit-override
[mypy-import-not-found]: https://mypy.readthedocs.io/en/stable/_refs.html#code-import-not-found
[mypy-import-untyped]: https://mypy.readthedocs.io/en/stable/_refs.html#code-import-untyped
[mypy-index]: https://mypy.readthedocs.io/en/stable/_refs.html#code-index
[mypy-metaclass]: https://mypy.readthedocs.io/en/stable/_refs.html#code-metaclass
[mypy-misc]: https://mypy.readthedocs.io/en/stable/_refs.html#code-misc
[mypy-name-defined]: https://mypy.readthedocs.io/en/stable/_refs.html#code-name-defined
[mypy-no-any-return]: https://mypy.readthedocs.io/en/stable/_refs.html#code-no-any-return
[mypy-no-implicit-reexport]: https://mypy.readthedocs.io/en/stable/_refs.html#cmdoption-mypy-no-implicit-reexport
[mypy-no-overload-impl]: https://mypy.readthedocs.io/en/stable/_refs.html#code-no-overload-impl
[mypy-no-redef]: https://mypy.readthedocs.io/en/stable/_refs.html#code-no-redef
[mypy-no-untyped-call]: https://mypy.readthedocs.io/en/stable/_refs.html#code-no-untyped-call
[mypy-no-untyped-def]: https://mypy.readthedocs.io/en/stable/_refs.html#code-no-untyped-def
[mypy-operator]: https://mypy.readthedocs.io/en/stable/_refs.html#code-operator
[mypy-overload-overlap]: https://mypy.readthedocs.io/en/stable/_refs.html#code-overload-overlap
[mypy-override]: https://mypy.readthedocs.io/en/stable/_refs.html#code-override
[mypy-possibly-undefined]: https://mypy.readthedocs.io/en/stable/_refs.html#code-possibly-undefined
[mypy-redundant-cast]: https://mypy.readthedocs.io/en/stable/_refs.html#code-redundant-cast
[mypy-return-value]: https://mypy.readthedocs.io/en/stable/_refs.html#code-return-value
[mypy-type-arg]: https://mypy.readthedocs.io/en/stable/_refs.html#code-type-arg
[mypy-type-var]: https://mypy.readthedocs.io/en/stable/_refs.html#code-type-var
[mypy-typeddict-item]: https://mypy.readthedocs.io/en/stable/_refs.html#code-typeddict-item
[mypy-typeddict-unknown-key]: https://mypy.readthedocs.io/en/stable/_refs.html#code-typeddict-unknown-key
[mypy-unimported-reveal]: https://mypy.readthedocs.io/en/stable/_refs.html#code-unimported-reveal
[mypy-union-attr]: https://mypy.readthedocs.io/en/stable/_refs.html#code-union-attr
[mypy-unreachable]: https://mypy.readthedocs.io/en/stable/_refs.html#code-unreachable
[mypy-untyped-decorator]: https://mypy.readthedocs.io/en/stable/_refs.html#code-untyped-decorator
[mypy-unused-awaitable]: https://mypy.readthedocs.io/en/stable/_refs.html#code-unused-awaitable
[mypy-unused-coroutine]: https://mypy.readthedocs.io/en/stable/_refs.html#code-unused-coroutine
[mypy-unused-ignore]: https://mypy.readthedocs.io/en/stable/_refs.html#code-unused-ignore
[mypy-valid-type]: https://mypy.readthedocs.io/en/stable/_refs.html#code-valid-type
[reportabstractusage]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportAbstractUsage
[reportargumenttype]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportArgumentType
[reportasserttypefailure]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportAssertTypeFailure
[reportassignmenttype]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportAssignmentType
[reportattributeaccessissue]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportAttributeAccessIssue
[reportcallissue]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportCallIssue
[reportconstantredefinition]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportConstantRedefinition
[reportdeprecated]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportDeprecated
[reportduplicateimport]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportDuplicateImport
[reportgeneraltypeissues]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportGeneralTypeIssues
[reportimplicitoverride]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportImplicitOverride
[reportimportcycles]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportImportCycles
[reportincompatiblemethodoverride]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportIncompatibleMethodOverride
[reportincompletestub]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportIncompleteStub
[reportinconsistentconstructor]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportInconsistentConstructor
[reportindexissue]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportIndexIssue
[reportinvalidstringescapesequence]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportInvalidStringEscapeSequence
[reportinvalidstubstatement]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportInvalidStubStatement
[reportinvalidtypearguments]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportInvalidTypeArguments
[reportinvalidtypeform]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportInvalidTypeForm
[reportinvalidtypevaruse]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportInvalidTypeVarUse
[reportmatchnotexhaustive]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportMatchNotExhaustive
[reportmissingimports]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportMissingImports
[reportmissingmodulesource]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportMissingModuleSource
[reportmissingparametertype]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportMissingParameterType
[reportmissingsupercall]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportMissingSuperCall
[reportmissingtypeargument]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportMissingTypeArgument
[reportmissingtypestubs]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportMissingTypeStubs
[reportnooverloadimplementation]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportNoOverloadImplementation
[reportoperatorissue]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportOperatorIssue
[reportoptionalmemberaccess]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportOptionalMemberAccess
[reportoverlappingoverload]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportOverlappingOverload
[reportpossiblyunboundvariable]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportPossiblyUnboundVariable
[reportprivateimportusage]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportPrivateImportUsage
[reportpropertytypemismatch]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportPropertyTypeMismatch
[reportredeclaration]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportRedeclaration
[reportreturntype]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportReturnType
[reportselfclsparametername]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportSelfClsParameterName
[reporttypecommentusage]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportTypeCommentUsage
[reporttypeddictnotrequiredaccess]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportTypedDictNotRequiredAccess
[reportundefinedvariable]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUndefinedVariable
[reportuninitializedinstancevariable]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUninitializedInstanceVariable
[reportunknownparametertype]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnknownParameterType
[reportunnecessarycast]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnnecessaryCast
[reportunnecessarycomparison]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnnecessaryComparison
[reportunnecessarycontains]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnnecessaryContains
[reportunnecessarytypeignorecomment]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnnecessaryTypeIgnoreComment
[reportunreachable]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnreachable
[reportunsupporteddunderall]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnsupportedDunderAll
[reportuntypedfunctiondecorator]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUntypedFunctionDecorator
[reportuntypednamedtuple]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUntypedNamedTuple
[reportunusedcoroutine]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnusedCoroutine
[reportunusedexpression]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnusedExpression
[reportwildcardimportfromlibrary]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportWildcardImportFromLibrary
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
[ty-call-abstract-method]: reference/rules.md#call-abstract-method
[ty-call-non-callable]: reference/rules.md#call-non-callable
[ty-conflicting-declarations]: reference/rules.md#conflicting-declarations
[ty-conflicting-metaclass]: reference/rules.md#conflicting-metaclass
[ty-cyclic-class-definition]: reference/rules.md#cyclic-class-definition
[ty-deprecated]: reference/rules.md#deprecated
[ty-division-by-zero]: reference/rules.md#division-by-zero
[ty-duplicate-base]: reference/rules.md#duplicate-base
[ty-empty-body]: reference/rules.md#empty-body
[ty-inconsistent-mro]: reference/rules.md#inconsistent-mro
[ty-index-out-of-bounds]: reference/rules.md#index-out-of-bounds
[ty-invalid-argument-type]: reference/rules.md#invalid-argument-type
[ty-invalid-assignment]: reference/rules.md#invalid-assignment
[ty-invalid-attribute-access]: reference/rules.md#invalid-attribute-access
[ty-invalid-await]: reference/rules.md#invalid-await
[ty-invalid-base]: reference/rules.md#invalid-base
[ty-invalid-context-manager]: reference/rules.md#invalid-context-manager
[ty-invalid-exception-caught]: reference/rules.md#invalid-exception-caught
[ty-invalid-key]: reference/rules.md#invalid-key
[ty-invalid-metaclass]: reference/rules.md#invalid-metaclass
[ty-invalid-method-override]: reference/rules.md#invalid-method-override
[ty-invalid-overload]: reference/rules.md#invalid-overload
[ty-invalid-parameter-default]: reference/rules.md#invalid-parameter-default
[ty-invalid-raise]: reference/rules.md#invalid-raise
[ty-invalid-return-type]: reference/rules.md#invalid-return-type
[ty-invalid-type-arguments]: reference/rules.md#invalid-type-arguments
[ty-invalid-type-form]: reference/rules.md#invalid-type-form
[ty-missing-argument]: reference/rules.md#missing-argument
[ty-missing-override-decorator]: reference/rules.md#missing-override-decorator
[ty-missing-type-argument]: reference/rules.md#missing-type-argument
[ty-missing-typed-dict-key]: reference/rules.md#missing-typed-dict-key
[ty-no-matching-overload]: reference/rules.md#no-matching-overload
[ty-not-iterable]: reference/rules.md#not-iterable
[ty-not-subscriptable]: reference/rules.md#not-subscriptable
[ty-parameter-already-assigned]: reference/rules.md#parameter-already-assigned
[ty-possibly-missing-attribute]: reference/rules.md#possibly-missing-attribute
[ty-possibly-unresolved-reference]: reference/rules.md#possibly-unresolved-reference
[ty-redundant-cast]: reference/rules.md#redundant-cast
[ty-too-many-positional-arguments]: reference/rules.md#too-many-positional-arguments
[ty-type-assertion-failure]: reference/rules.md#type-assertion-failure
[ty-undefined-reveal]: reference/rules.md#undefined-reveal
[ty-unknown-argument]: reference/rules.md#unknown-argument
[ty-unresolved-attribute]: reference/rules.md#unresolved-attribute
[ty-unresolved-import]: reference/rules.md#unresolved-import
[ty-unresolved-reference]: reference/rules.md#unresolved-reference
[ty-unsupported-operator]: reference/rules.md#unsupported-operator
[ty-unused-awaitable]: reference/rules.md#unused-awaitable
[ty-unused-ignore-comment]: reference/rules.md#unused-ignore-comment
