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
[tool.ty.rules]
dynamic-function-decorator-return = "error"
missing-type-argument = "error"
possibly-unresolved-reference = "warn"
unsound-return-statement = "error"

[tool.ruff.lint]
extend-select = ["ANN", "PYI"]
preview = true
```

This configuration:

- Enables ty's disabled-by-default [`dynamic-function-decorator-return`](https://docs.astral.sh/ty/reference/rules/#dynamic-function-decorator-return), [`missing-type-argument`](https://docs.astral.sh/ty/reference/rules/#missing-type-argument), [`possibly-unresolved-reference`](https://docs.astral.sh/ty/reference/rules/#possibly-unresolved-reference), and [`unsound-return-statement`](https://docs.astral.sh/ty/reference/rules/#unsound-return-statement) rules
- Extends Ruff's default rules with the [`ANN`](https://docs.astral.sh/ruff/rules/#flake8-annotations-ann) and [`PYI`](https://docs.astral.sh/ruff/rules/#flake8-pyi-pyi) rule categories, both of which are focussed on type-annotating your code more effectively
- Enables Ruff's preview mode so that `PYI033` also checks `.py` files

An even stricter configuration -- that goes beyond what mypy and pyright check for in their default
`--strict` mode in several respects -- might look like this:

```toml
[tool.ty.rules]
blanket-ignore-comment = "error"
dynamic-function-decorator-return = "error"
missing-type-argument = "error"
possibly-unresolved-reference = "warn"
unsound-return-statement = "error"
unsound-yield = "error"
unsupported-dynamic-base = "warn"

# NOTE: the following rules are known to have a significant number of false positives,
# which is mostly unavoidable. Enable them at your own risk!
division-by-zero = "warn"
possibly-missing-attribute = "warn"
possibly-missing-import = "warn"

[tool.ty.analysis]
strict-literal-narrowing = true
strict-generic-narrowing = true

[tool.ruff.lint]
extend-select = ["ANN", "PYI", "PGH003"]
preview = true
```

Note that several checks in mypy and pyright are not yet implemented in ty. See the rule mapping
table below for more details.

## Mapping pyright/mypy rules to ty/Ruff rules

### How to read this table

- **ty or Ruff rule**: the canonical name, as listed in [Rules](reference/rules.md) if it is a ty
    rule. Configure ty rules under `[tool.ty.rules]`. Where Ruff provides equivalent coverage for a
    check that has no ty rule, the relevant Ruff rule or rule group is linked instead.
- **Mypy error code**: the value passed to `# type: ignore[<code>]` or `disable_error_code`. Some ty
    rules surface as one of mypy's catch-all codes (`misc`, `assignment`, `valid-type`); these
    mappings are deliberately broad.
- **Pyright diagnostic**: the `report*` setting in `pyrightconfig.json` or `[tool.pyright]`.

A blank cell means no direct equivalent exists in that checker (the diagnostic is either not
emitted, or is folded into a broader category that already appears for another ty rule).

### Rules

| ty or Ruff rule                                                                                                              | Mypy error code                                                                                                                                                      | Pyright or basedpyright diagnostic                                                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`abstract-and-final-method`][ty-abstract-and-final-method]                                                                  | [`misc`][mypy-misc]                                                                                                                                                  |                                                                                                                                                                                        |
| [`abstract-method-in-final-class`][ty-abstract-method-in-final-class]                                                        | [`misc`][mypy-misc]                                                                                                                                                  | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`call-abstract-method`][ty-call-abstract-method]                                                                            |                                                                                                                                                                      | [`reportAbstractUsage`][reportabstractusage]                                                                                                                                           |
| [`call-non-callable`][ty-call-non-callable]                                                                                  | [`operator`][mypy-operator]<br>[`misc`][mypy-misc]                                                                                                                   | [`reportCallIssue`][reportcallissue]<br>[`reportOptionalCall`][reportoptionalcall]                                                                                                     |
| [`conflicting-declarations`][ty-conflicting-declarations]                                                                    | [`no-redef`][mypy-no-redef]                                                                                                                                          | [`reportRedeclaration`][reportredeclaration]                                                                                                                                           |
| [`conflicting-metaclass`][ty-conflicting-metaclass]                                                                          | [`metaclass`][mypy-metaclass]                                                                                                                                        | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`cyclic-class-definition`][ty-cyclic-class-definition]                                                                      | [`misc`][mypy-misc]                                                                                                                                                  | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`dataclass-field-order`][ty-dataclass-field-order]                                                                          | [`misc`][mypy-misc]                                                                                                                                                  | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`deprecated`][ty-deprecated]                                                                                                | [`deprecated`][mypy-deprecated]                                                                                                                                      | [`reportDeprecated`][reportdeprecated]                                                                                                                                                 |
| [`division-by-zero`][ty-division-by-zero]                                                                                    |                                                                                                                                                                      |                                                                                                                                                                                        |
| [`duplicate-base`][ty-duplicate-base]                                                                                        | [`misc`][mypy-misc]                                                                                                                                                  | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`duplicate-kw-only`][ty-duplicate-kw-only]                                                                                  | [`misc`][mypy-misc]                                                                                                                                                  |                                                                                                                                                                                        |
| [`dynamic-function-decorator-return`][ty-dynamic-function-decorator-return]                                                  | [`untyped-decorator`][mypy-untyped-decorator]                                                                                                                        | [`reportUntypedFunctionDecorator`][reportuntypedfunctiondecorator] (`Unknown` returns only)                                                                                            |
| [`empty-body`][ty-empty-body]                                                                                                | [`empty-body`][mypy-empty-body]                                                                                                                                      |                                                                                                                                                                                        |
| [`final-on-non-method`][ty-final-on-non-method]                                                                              | [`misc`][mypy-misc]                                                                                                                                                  | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`final-without-value`][ty-final-without-value]                                                                              | [`misc`][mypy-misc]                                                                                                                                                  | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`inconsistent-mro`][ty-inconsistent-mro]                                                                                    | [`misc`][mypy-misc]                                                                                                                                                  | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`index-out-of-bounds`][ty-index-out-of-bounds]                                                                              | [`misc`][mypy-misc]                                                                                                                                                  | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`invalid-argument-type`][ty-invalid-argument-type]                                                                          | [`arg-type`][mypy-arg-type]<br>[`index`][mypy-index]<br>[`type-var`][mypy-type-var]<br>[`typeddict-item`][mypy-typeddict-item]                                       | [`reportArgumentType`][reportargumenttype]<br>[`reportAssignmentType`][reportassignmenttype]                                                                                           |
| [`invalid-assignment`][ty-invalid-assignment]                                                                                | [`assignment`][mypy-assignment]<br>[`list-item`][mypy-list-item]<br>[`dict-item`][mypy-dict-item]<br>[`typeddict-readonly-mutated`][mypy-typeddict-readonly-mutated] | [`reportAssignmentType`][reportassignmenttype]                                                                                                                                         |
| [`invalid-assignment`][ty-invalid-assignment] (method assignments)                                                           | [`method-assign`][mypy-method-assign]                                                                                                                                |                                                                                                                                                                                        |
| [`invalid-attribute-access`][ty-invalid-attribute-access]                                                                    | [`misc`][mypy-misc]                                                                                                                                                  | [`reportAttributeAccessIssue`][reportattributeaccessissue]                                                                                                                             |
| [`invalid-attribute-override`][ty-invalid-attribute-override]                                                                | [`misc`][mypy-misc]                                                                                                                                                  | [`reportIncompatibleVariableOverride`][reportincompatiblevariableoverride] (class/instance variables only)                                                                             |
| [`invalid-await`][ty-invalid-await]                                                                                          | [`misc`][mypy-misc]                                                                                                                                                  | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`invalid-base`][ty-invalid-base]                                                                                            | [`valid-type`][mypy-valid-type]                                                                                                                                      | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`invalid-context-manager`][ty-invalid-context-manager]                                                                      | [`misc`][mypy-misc]<br>[`attr-defined`][mypy-attr-defined]<br>[`union-attr`][mypy-union-attr]                                                                        | [`reportGeneralTypeIssues`][reportgeneraltypeissues]<br>[`reportOptionalContextManager`][reportoptionalcontextmanager]                                                                 |
| [`invalid-dataclass`][ty-invalid-dataclass]                                                                                  | [`misc`][mypy-misc]                                                                                                                                                  |                                                                                                                                                                                        |
| [`invalid-exception-caught`][ty-invalid-exception-caught]                                                                    | [`misc`][mypy-misc]                                                                                                                                                  | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`invalid-explicit-override`][ty-invalid-explicit-override]                                                                  | [`misc`][mypy-misc]                                                                                                                                                  | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`invalid-frozen-dataclass-subclass`][ty-invalid-frozen-dataclass-subclass]                                                  | [`misc`][mypy-misc]                                                                                                                                                  | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`invalid-key`][ty-invalid-key]                                                                                              | [`typeddict-item`][mypy-typeddict-item]<br>[`typeddict-unknown-key`][mypy-typeddict-unknown-key]                                                                     | [`reportAssignmentType`][reportassignmenttype]                                                                                                                                         |
| [`invalid-legacy-type-variable`][ty-invalid-legacy-type-variable]                                                            | [`misc`][mypy-misc]                                                                                                                                                  | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`invalid-metaclass`][ty-invalid-metaclass]                                                                                  | [`metaclass`][mypy-metaclass]                                                                                                                                        |                                                                                                                                                                                        |
| [`invalid-method-override`][ty-invalid-method-override]                                                                      | [`override`][mypy-override]                                                                                                                                          | [`reportIncompatibleMethodOverride`][reportincompatiblemethodoverride]                                                                                                                 |
| [`invalid-module-getattr-call`][ty-invalid-module-getattr-call]                                                              |                                                                                                                                                                      |                                                                                                                                                                                        |
| [`invalid-newtype`][ty-invalid-newtype]                                                                                      | [`valid-newtype`][mypy-valid-newtype]                                                                                                                                | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`invalid-overload`][ty-invalid-overload]                                                                                    | [`no-overload-impl`][mypy-no-overload-impl]<br>[`misc`][mypy-misc]                                                                                                   | [`reportNoOverloadImplementation`][reportnooverloadimplementation]<br>[`reportInconsistentOverload`][reportinconsistentoverload]                                                       |
| [`invalid-parameter-default`][ty-invalid-parameter-default]                                                                  | [`assignment`][mypy-assignment]                                                                                                                                      | [`reportArgumentType`][reportargumenttype]                                                                                                                                             |
| [`invalid-protocol`][ty-invalid-protocol]                                                                                    | [`misc`][mypy-misc]                                                                                                                                                  | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`invalid-raise`][ty-invalid-raise]                                                                                          | [`misc`][mypy-misc]                                                                                                                                                  | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`invalid-return-type`][ty-invalid-return-type]                                                                              | [`return`][mypy-return]<br>[`return-value`][mypy-return-value]                                                                                                       | [`reportReturnType`][reportreturntype]                                                                                                                                                 |
| [`invalid-type-arguments`][ty-invalid-type-arguments]                                                                        | [`misc`][mypy-misc]<br>[`type-var`][mypy-type-var]                                                                                                                   | [`reportInvalidTypeArguments`][reportinvalidtypearguments]                                                                                                                             |
| [`invalid-type-form`][ty-invalid-type-form]                                                                                  | [`valid-type`][mypy-valid-type]                                                                                                                                      | [`reportInvalidTypeForm`][reportinvalidtypeform]                                                                                                                                       |
| [`invalid-type-guard-definition`][ty-invalid-type-guard-definition]                                                          | [`narrowed-type-not-subtype`][mypy-narrowed-type-not-subtype]<br>[`valid-type`][mypy-valid-type]                                                                     | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`invalid-type-variable-bound`][ty-invalid-type-variable-bound]                                                              | [`valid-type`][mypy-valid-type]                                                                                                                                      | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`invalid-type-variable-constraints`][ty-invalid-type-variable-constraints]                                                  | [`valid-type`][mypy-valid-type]                                                                                                                                      | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`invalid-type-variable-default`][ty-invalid-type-variable-default]                                                          | [`misc`][mypy-misc]                                                                                                                                                  | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`invalid-typed-dict-field`][ty-invalid-typed-dict-field]                                                                    | [`misc`][mypy-misc]                                                                                                                                                  | [`reportIncompatibleVariableOverride`][reportincompatiblevariableoverride]                                                                                                             |
| [`invalid-yield`][ty-invalid-yield]                                                                                          | [`misc`][mypy-misc]                                                                                                                                                  | [`reportReturnType`][reportreturntype]                                                                                                                                                 |
| [`isinstance-against-protocol`][ty-isinstance-against-protocol]                                                              | [`misc`][mypy-misc]                                                                                                                                                  | [`reportArgumentType`][reportargumenttype]                                                                                                                                             |
| [`isinstance-against-typed-dict`][ty-isinstance-against-typed-dict]                                                          | [`misc`][mypy-misc]                                                                                                                                                  | [`reportArgumentType`][reportargumenttype]                                                                                                                                             |
| [`mismatched-type-name`][ty-mismatched-type-name]                                                                            | [`name-match`][mypy-name-match]<br>[`misc`][mypy-misc]                                                                                                               | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`missing-argument`][ty-missing-argument]                                                                                    | [`call-arg`][mypy-call-arg]                                                                                                                                          | [`reportCallIssue`][reportcallissue]                                                                                                                                                   |
| [`missing-override-decorator`][ty-missing-override-decorator]                                                                | [`explicit-override`][mypy-explicit-override]                                                                                                                        | [`reportImplicitOverride`][reportimplicitoverride]                                                                                                                                     |
| [`missing-type-argument`][ty-missing-type-argument]                                                                          | [`type-arg`][mypy-type-arg]                                                                                                                                          | [`reportMissingTypeArgument`][reportmissingtypeargument]                                                                                                                               |
| [`missing-typed-dict-key`][ty-missing-typed-dict-key]                                                                        | [`typeddict-item`][mypy-typeddict-item]                                                                                                                              | [`reportAssignmentType`][reportassignmenttype]                                                                                                                                         |
| [`no-matching-overload`][ty-no-matching-overload]                                                                            | [`call-overload`][mypy-call-overload]                                                                                                                                | [`reportCallIssue`][reportcallissue]                                                                                                                                                   |
| [`not-iterable`][ty-not-iterable]                                                                                            | [`misc`][mypy-misc]<br>[`attr-defined`][mypy-attr-defined]<br>[`union-attr`][mypy-union-attr]                                                                        | [`reportGeneralTypeIssues`][reportgeneraltypeissues]<br>[`reportOptionalIterable`][reportoptionaliterable]                                                                             |
| [`not-subscriptable`][ty-not-subscriptable]                                                                                  | [`index`][mypy-index]                                                                                                                                                | [`reportIndexIssue`][reportindexissue]<br>[`reportOptionalSubscript`][reportoptionalsubscript]                                                                                         |
| [`override-of-final-method`][ty-override-of-final-method]                                                                    | [`misc`][mypy-misc]                                                                                                                                                  | [`reportIncompatibleMethodOverride`][reportincompatiblemethodoverride]                                                                                                                 |
| [`override-of-final-variable`][ty-override-of-final-variable]                                                                | [`misc`][mypy-misc]                                                                                                                                                  | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`parameter-already-assigned`][ty-parameter-already-assigned]                                                                | [`misc`][mypy-misc]<br>[`call-arg`][mypy-call-arg]                                                                                                                   | [`reportCallIssue`][reportcallissue]                                                                                                                                                   |
| [`positional-only-parameter-as-kwarg`][ty-positional-only-parameter-as-kwarg]                                                | [`call-arg`][mypy-call-arg]                                                                                                                                          | [`reportCallIssue`][reportcallissue]                                                                                                                                                   |
| [`possibly-missing-attribute`][ty-possibly-missing-attribute]                                                                |                                                                                                                                                                      |                                                                                                                                                                                        |
| [`possibly-unresolved-reference`][ty-possibly-unresolved-reference]                                                          | [`possibly-undefined`][mypy-possibly-undefined]                                                                                                                      | [`reportPossiblyUnboundVariable`][reportpossiblyunboundvariable]                                                                                                                       |
| [`redundant-cast`][ty-redundant-cast]                                                                                        | [`redundant-cast`][mypy-redundant-cast]                                                                                                                              | [`reportUnnecessaryCast`][reportunnecessarycast]                                                                                                                                       |
| [`subclass-of-final-class`][ty-subclass-of-final-class]                                                                      | [`misc`][mypy-misc]                                                                                                                                                  | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`too-many-positional-arguments`][ty-too-many-positional-arguments]                                                          | [`call-arg`][mypy-call-arg]                                                                                                                                          | [`reportCallIssue`][reportcallissue]                                                                                                                                                   |
| [`type-assertion-failure`][ty-type-assertion-failure]                                                                        | [`assert-type`][mypy-assert-type]                                                                                                                                    | [`reportAssertTypeFailure`][reportasserttypefailure]                                                                                                                                   |
| [`unbound-type-variable`][ty-unbound-type-variable]                                                                          | [`valid-type`][mypy-valid-type]                                                                                                                                      | [`reportGeneralTypeIssues`][reportgeneraltypeissues]                                                                                                                                   |
| [`undefined-reveal`][ty-undefined-reveal]                                                                                    | [`unimported-reveal`][mypy-unimported-reveal]                                                                                                                        |                                                                                                                                                                                        |
| [`unknown-argument`][ty-unknown-argument]                                                                                    | [`call-arg`][mypy-call-arg]                                                                                                                                          | [`reportCallIssue`][reportcallissue]                                                                                                                                                   |
| [`unresolved-attribute`][ty-unresolved-attribute]                                                                            | [`attr-defined`][mypy-attr-defined]<br>[`union-attr`][mypy-union-attr]                                                                                               | [`reportAttributeAccessIssue`][reportattributeaccessissue]<br>[`reportFunctionMemberAccess`][reportfunctionmemberaccess]<br>[`reportOptionalMemberAccess`][reportoptionalmemberaccess] |
| [`unresolved-import`][ty-unresolved-import]                                                                                  | [`import-not-found`][mypy-import-not-found]                                                                                                                          | [`reportMissingImports`][reportmissingimports]                                                                                                                                         |
| [`unresolved-reference`][ty-unresolved-reference], [Ruff `F823`][ruff-f823]                                                  | [`name-defined`][mypy-name-defined]<br>[`used-before-def`][mypy-used-before-def]                                                                                     | [`reportUndefinedVariable`][reportundefinedvariable]<br>[`reportUnboundVariable`][reportunboundvariable]                                                                               |
| [`unsound-return-statement`][ty-unsound-return-statement]                                                                    | [`no-any-return`][mypy-no-any-return]                                                                                                                                |                                                                                                                                                                                        |
| [`unsound-yield`][ty-unsound-yield]                                                                                          |                                                                                                                                                                      |                                                                                                                                                                                        |
| [`unsupported-operator`][ty-unsupported-operator]                                                                            | [`operator`][mypy-operator]                                                                                                                                          | [`reportOperatorIssue`][reportoperatorissue]<br>[`reportOptionalOperand`][reportoptionaloperand]                                                                                       |
| [`unused-awaitable`][ty-unused-awaitable]                                                                                    | [`unused-coroutine`][mypy-unused-coroutine]<br>[`unused-awaitable`][mypy-unused-awaitable]                                                                           | [`reportUnusedCoroutine`][reportunusedcoroutine]                                                                                                                                       |
| [`unused-ignore-comment`][ty-unused-ignore-comment]                                                                          | [`unused-ignore`][mypy-unused-ignore]                                                                                                                                | [`reportUnnecessaryTypeIgnoreComment`][reportunnecessarytypeignorecomment]                                                                                                             |
| [`unused-type-ignore-comment`][ty-unused-type-ignore-comment]                                                                | [`unused-ignore`][mypy-unused-ignore]                                                                                                                                | [`reportUnnecessaryTypeIgnoreComment`][reportunnecessarytypeignorecomment]                                                                                                             |
| [`blanket-ignore-comment`][ty-blanket-ignore-comment], [Ruff `PGH003`][ruff-pgh003]                                          | [`ignore-without-code`][mypy-ignore-without-code]                                                                                                                    | [`reportIgnoreCommentWithoutRule`][reportignorecommentwithoutrule] (basedpyright only)                                                                                                 |
| None yet for instantiating abstract classes                                                                                  | [`abstract`][mypy-abstract]                                                                                                                                          | [`reportAbstractUsage`][reportabstractusage]                                                                                                                                           |
| None yet for passing abstract classes where concrete classes are required                                                    | [`type-abstract`][mypy-type-abstract]                                                                                                                                |                                                                                                                                                                                        |
| None yet for calling abstract methods through `super()`                                                                      | [`safe-super`][mypy-safe-super]                                                                                                                                      | [`reportAbstractUsage`][reportabstractusage]                                                                                                                                           |
| [Ruff `F631`][ruff-f631]                                                                                                     |                                                                                                                                                                      | [`reportAssertAlwaysTrue`][reportassertalwaystrue]                                                                                                                                     |
| [Ruff `B006`][ruff-b006]<br>[Ruff `B008`][ruff-b008] (partial coverage; immutable annotations and calls are excluded)        |                                                                                                                                                                      | [`reportCallInDefaultInitializer`][reportcallindefaultinitializer]                                                                                                                     |
| None yet (tracked in [Ruff #10137][ruff-10137])                                                                              |                                                                                                                                                                      | [`reportConstantRedefinition`][reportconstantredefinition]                                                                                                                             |
| [Ruff `F811`][ruff-f811]<br>[Ruff `I001`][ruff-i001]                                                                         |                                                                                                                                                                      | [`reportDuplicateImport`][reportduplicateimport]                                                                                                                                       |
| [Ruff `ISC001`][ruff-isc001]<br>[Ruff `ISC002`][ruff-isc002]                                                                 |                                                                                                                                                                      | [`reportImplicitStringConcatenation`][reportimplicitstringconcatenation]                                                                                                               |
| None yet (tracked in [#3647][ty-3647])                                                                                       |                                                                                                                                                                      | [`reportImportCycles`][reportimportcycles]                                                                                                                                             |
| None yet for mutable attribute types (tracked in [#2158][ty-2158])                                                           | [`mutable-override`][mypy-mutable-override]                                                                                                                          | [`reportIncompatibleVariableOverride`][reportincompatiblevariableoverride]                                                                                                             |
| None yet                                                                                                                     |                                                                                                                                                                      | [`reportIncompleteStub`][reportincompletestub]                                                                                                                                         |
| None yet (tracked in [#3651][ty-3651])                                                                                       |                                                                                                                                                                      | [`reportInconsistentConstructor`][reportinconsistentconstructor]                                                                                                                       |
| [Ruff `W605`][ruff-w605]                                                                                                     |                                                                                                                                                                      | [`reportInvalidStringEscapeSequence`][reportinvalidstringescapesequence]                                                                                                               |
| [Ruff `PYI010`][ruff-pyi010]<br>[Ruff `PYI017`][ruff-pyi017]<br>[Ruff `PYI048`][ruff-pyi048]<br>[Ruff `PYI052`][ruff-pyi052] |                                                                                                                                                                      | [`reportInvalidStubStatement`][reportinvalidstubstatement]                                                                                                                             |
| None yet (tracked in [#1017][ty-1017], [#3636][ty-3636], [#3637][ty-3637])                                                   | [`type-var`][mypy-type-var]                                                                                                                                          | [`reportInvalidTypeVarUse`][reportinvalidtypevaruse]                                                                                                                                   |
| None yet (tracked in [#1060][ty-1060])                                                                                       | [`exhaustive-match`][mypy-exhaustive-match]                                                                                                                          | [`reportMatchNotExhaustive`][reportmatchnotexhaustive]                                                                                                                                 |
| None yet (tracked in [#1577][ty-1577])                                                                                       |                                                                                                                                                                      | [`reportMissingModuleSource`][reportmissingmodulesource]                                                                                                                               |
| None yet (tracked in [#3652][ty-3652])                                                                                       |                                                                                                                                                                      | [`reportMissingSuperCall`][reportmissingsupercall]                                                                                                                                     |
| None yet (tracked in [#3638][ty-3638])                                                                                       | [`import-untyped`][mypy-import-untyped]                                                                                                                              | [`reportMissingTypeStubs`][reportmissingtypestubs]                                                                                                                                     |
| None yet (tracked in [#103][ty-103])                                                                                         | [`overload-cannot-match`][mypy-overload-cannot-match]<br>[`overload-overlap`][mypy-overload-overlap]                                                                 | [`reportOverlappingOverload`][reportoverlappingoverload]                                                                                                                               |
| None yet (tracked in [#200][ty-200])                                                                                         | [`attr-defined`][mypy-attr-defined]<br>(extended by [`--no-implicit-reexport`][mypy-no-implicit-reexport])                                                           | [`reportPrivateImportUsage`][reportprivateimportusage]<br>[`reportPrivateLocalImportUsage`][reportprivatelocalimportusage] (basedpyright only)                                         |
| [Ruff `SLF001`][ruff-slf001]<br>[Ruff `PLC2701`][ruff-plc2701] (partial coverage; `PLC2701` requires preview)                |                                                                                                                                                                      | [`reportPrivateUsage`][reportprivateusage]                                                                                                                                             |
| None yet (tracked in [#3633][ty-3633])                                                                                       |                                                                                                                                                                      | [`reportPropertyTypeMismatch`][reportpropertytypemismatch]                                                                                                                             |
| [Ruff `N804`][ruff-n804]<br>[Ruff `N805`][ruff-n805]                                                                         |                                                                                                                                                                      | [`reportSelfClsParameterName`][reportselfclsparametername]                                                                                                                             |
| [Ruff `PYI033`][ruff-pyi033] (preview only)                                                                                  |                                                                                                                                                                      | [`reportTypeCommentUsage`][reporttypecommentusage]                                                                                                                                     |
| None yet for accessing non-required keys (tracked in [#2810][ty-2810])                                                       |                                                                                                                                                                      | [`reportTypedDictNotRequiredAccess`][reporttypeddictnotrequiredaccess]                                                                                                                 |
| None yet (tracked in [#3781][ty-3781])                                                                                       |                                                                                                                                                                      | [`reportUnhashable`][reportunhashable]                                                                                                                                                 |
| None yet (tracked in [#2954][ty-2954])                                                                                       |                                                                                                                                                                      | [`reportUninitializedInstanceVariable`][reportuninitializedinstancevariable]                                                                                                           |
| None yet                                                                                                                     |                                                                                                                                                                      | [`reportUnknownArgumentType`][reportunknownargumenttype]<br>[`reportUnknownLambdaType`][reportunknownlambdatype]<br>[`reportUnknownMemberType`][reportunknownmembertype]               |
| None yet                                                                                                                     | [`var-annotated`][mypy-var-annotated]                                                                                                                                |                                                                                                                                                                                        |
| None yet                                                                                                                     |                                                                                                                                                                      | [`reportUnknownVariableType`][reportunknownvariabletype]                                                                                                                               |
| None yet (tracked in [#576][ty-576])                                                                                         | [`comparison-overlap`][mypy-comparison-overlap]                                                                                                                      | [`reportUnnecessaryComparison`][reportunnecessarycomparison]<br>[`reportUnnecessaryContains`][reportunnecessarycontains]                                                               |
| None yet                                                                                                                     |                                                                                                                                                                      | [`reportUnnecessaryIsInstance`][reportunnecessaryisinstance]                                                                                                                           |
| None yet (tracked in [#1948][ty-1948])                                                                                       | [`unreachable`][mypy-unreachable]                                                                                                                                    | [`reportUnreachable`][reportunreachable]                                                                                                                                               |
| [Ruff `F822`][ruff-f822]<br>[Ruff `PLE0604`][ruff-ple0604]<br>[Ruff `PLE0605`][ruff-ple0605]<br>[Ruff `PYI056`][ruff-pyi056] |                                                                                                                                                                      | [`reportUnsupportedDunderAll`][reportunsupporteddunderall]                                                                                                                             |
| None yet                                                                                                                     |                                                                                                                                                                      | [`reportUntypedBaseClass`][reportuntypedbaseclass]<br>[`reportUntypedClassDecorator`][reportuntypedclassdecorator]                                                                     |
| [Ruff `PYI024`][ruff-pyi024]                                                                                                 |                                                                                                                                                                      | [`reportUntypedNamedTuple`][reportuntypednamedtuple]                                                                                                                                   |
| None yet                                                                                                                     |                                                                                                                                                                      | [`reportUnusedClass`][reportunusedclass]<br>[`reportUnusedFunction`][reportunusedfunction]                                                                                             |
| None yet                                                                                                                     |                                                                                                                                                                      | [`reportUnusedCallResult`][reportunusedcallresult]                                                                                                                                     |
| [Ruff `ARG` rules][ruff-arg]                                                                                                 |                                                                                                                                                                      | [`reportUnusedParameter`][reportunusedparameter] (basedpyright only)                                                                                                                   |
| [Ruff `B025`][ruff-b025] (duplicate exception handlers only; other cases tracked in [#3701][ty-3701])                        |                                                                                                                                                                      | [`reportUnusedExcept`][reportunusedexcept]                                                                                                                                             |
| [Ruff `B018`][ruff-b018]                                                                                                     |                                                                                                                                                                      | [`reportUnusedExpression`][reportunusedexpression]                                                                                                                                     |
| [Ruff `F401`][ruff-f401]                                                                                                     |                                                                                                                                                                      | [`reportUnusedImport`][reportunusedimport]                                                                                                                                             |
| [Ruff `F841`][ruff-f841] (function-local variables only)                                                                     |                                                                                                                                                                      | [`reportUnusedVariable`][reportunusedvariable]                                                                                                                                         |
| [Ruff `F403`][ruff-f403]                                                                                                     |                                                                                                                                                                      | [`reportWildcardImportFromLibrary`][reportwildcardimportfromlibrary]                                                                                                                   |
| [Ruff `ANN401`][ruff-ann401] (function annotations only)                                                                     | [`explicit-any`][mypy-explicit-any]                                                                                                                                  | [`reportExplicitAny`][reportexplicitany] (basedpyright only)                                                                                                                           |
| None yet                                                                                                                     | [`func-returns-value`][mypy-func-returns-value]                                                                                                                      |                                                                                                                                                                                        |
| None yet                                                                                                                     | [`no-any-unimported`][mypy-no-any-unimported]                                                                                                                        |                                                                                                                                                                                        |
| None yet                                                                                                                     | [`no-untyped-call`][mypy-no-untyped-call]                                                                                                                            |                                                                                                                                                                                        |
| None yet                                                                                                                     | [`truthy-function`][mypy-truthy-function]                                                                                                                            | [`reportUnnecessaryComparison`][reportunnecessarycomparison]                                                                                                                           |
| None yet                                                                                                                     | [`truthy-iterable`][mypy-truthy-iterable]                                                                                                                            |                                                                                                                                                                                        |
| [Ruff `ANN` rules][ruff-ann]                                                                                                 | [`no-untyped-def`][mypy-no-untyped-def]                                                                                                                              | [`reportMissingParameterType`][reportmissingparametertype]<br>[`reportUnknownParameterType`][reportunknownparametertype]                                                               |

The full list of ty rules — including those without a direct equivalent above — is in
[Rules](reference/rules.md). Contributions to extend this mapping are welcome via pull request to the
[`ty` repository](https://github.com/astral-sh/ty); see issue
[#2111](https://github.com/astral-sh/ty/issues/2111) for context.

[mypy-abstract]: https://mypy.readthedocs.io/en/stable/_refs.html#code-abstract
[mypy-arg-type]: https://mypy.readthedocs.io/en/stable/_refs.html#code-arg-type
[mypy-assert-type]: https://mypy.readthedocs.io/en/stable/_refs.html#code-assert-type
[mypy-assignment]: https://mypy.readthedocs.io/en/stable/_refs.html#code-assignment
[mypy-attr-defined]: https://mypy.readthedocs.io/en/stable/_refs.html#code-attr-defined
[mypy-call-arg]: https://mypy.readthedocs.io/en/stable/_refs.html#code-call-arg
[mypy-call-overload]: https://mypy.readthedocs.io/en/stable/_refs.html#code-call-overload
[mypy-comparison-overlap]: https://mypy.readthedocs.io/en/stable/_refs.html#code-comparison-overlap
[mypy-deprecated]: https://mypy.readthedocs.io/en/stable/_refs.html#code-deprecated
[mypy-dict-item]: https://mypy.readthedocs.io/en/stable/_refs.html#code-dict-item
[mypy-empty-body]: https://mypy.readthedocs.io/en/stable/_refs.html#code-empty-body
[mypy-exhaustive-match]: https://mypy.readthedocs.io/en/stable/_refs.html#code-exhaustive-match
[mypy-explicit-any]: https://mypy.readthedocs.io/en/stable/_refs.html#code-explicit-any
[mypy-explicit-override]: https://mypy.readthedocs.io/en/stable/_refs.html#code-explicit-override
[mypy-func-returns-value]: https://mypy.readthedocs.io/en/stable/_refs.html#code-func-returns-value
[mypy-ignore-without-code]: https://mypy.readthedocs.io/en/stable/_refs.html#code-ignore-without-code
[mypy-import-not-found]: https://mypy.readthedocs.io/en/stable/_refs.html#code-import-not-found
[mypy-import-untyped]: https://mypy.readthedocs.io/en/stable/_refs.html#code-import-untyped
[mypy-index]: https://mypy.readthedocs.io/en/stable/_refs.html#code-index
[mypy-list-item]: https://mypy.readthedocs.io/en/stable/_refs.html#code-list-item
[mypy-metaclass]: https://mypy.readthedocs.io/en/stable/_refs.html#code-metaclass
[mypy-method-assign]: https://mypy.readthedocs.io/en/stable/_refs.html#code-method-assign
[mypy-misc]: https://mypy.readthedocs.io/en/stable/_refs.html#code-misc
[mypy-mutable-override]: https://mypy.readthedocs.io/en/stable/_refs.html#code-mutable-override
[mypy-name-defined]: https://mypy.readthedocs.io/en/stable/_refs.html#code-name-defined
[mypy-name-match]: https://mypy.readthedocs.io/en/stable/_refs.html#code-name-match
[mypy-narrowed-type-not-subtype]: https://mypy.readthedocs.io/en/stable/_refs.html#code-narrowed-type-not-subtype
[mypy-no-any-return]: https://mypy.readthedocs.io/en/stable/_refs.html#code-no-any-return
[mypy-no-any-unimported]: https://mypy.readthedocs.io/en/stable/_refs.html#code-no-any-unimported
[mypy-no-implicit-reexport]: https://mypy.readthedocs.io/en/stable/_refs.html#cmdoption-mypy-no-implicit-reexport
[mypy-no-overload-impl]: https://mypy.readthedocs.io/en/stable/_refs.html#code-no-overload-impl
[mypy-no-redef]: https://mypy.readthedocs.io/en/stable/_refs.html#code-no-redef
[mypy-no-untyped-call]: https://mypy.readthedocs.io/en/stable/_refs.html#code-no-untyped-call
[mypy-no-untyped-def]: https://mypy.readthedocs.io/en/stable/_refs.html#code-no-untyped-def
[mypy-operator]: https://mypy.readthedocs.io/en/stable/_refs.html#code-operator
[mypy-overload-cannot-match]: https://mypy.readthedocs.io/en/stable/_refs.html#code-overload-cannot-match
[mypy-overload-overlap]: https://mypy.readthedocs.io/en/stable/_refs.html#code-overload-overlap
[mypy-override]: https://mypy.readthedocs.io/en/stable/_refs.html#code-override
[mypy-possibly-undefined]: https://mypy.readthedocs.io/en/stable/_refs.html#code-possibly-undefined
[mypy-redundant-cast]: https://mypy.readthedocs.io/en/stable/_refs.html#code-redundant-cast
[mypy-return]: https://mypy.readthedocs.io/en/stable/_refs.html#code-return
[mypy-return-value]: https://mypy.readthedocs.io/en/stable/_refs.html#code-return-value
[mypy-safe-super]: https://mypy.readthedocs.io/en/stable/_refs.html#code-safe-super
[mypy-truthy-function]: https://mypy.readthedocs.io/en/stable/_refs.html#code-truthy-function
[mypy-truthy-iterable]: https://mypy.readthedocs.io/en/stable/_refs.html#code-truthy-iterable
[mypy-type-abstract]: https://mypy.readthedocs.io/en/stable/_refs.html#code-type-abstract
[mypy-type-arg]: https://mypy.readthedocs.io/en/stable/_refs.html#code-type-arg
[mypy-type-var]: https://mypy.readthedocs.io/en/stable/_refs.html#code-type-var
[mypy-typeddict-item]: https://mypy.readthedocs.io/en/stable/_refs.html#code-typeddict-item
[mypy-typeddict-readonly-mutated]: https://mypy.readthedocs.io/en/stable/_refs.html#code-typeddict-readonly-mutated
[mypy-typeddict-unknown-key]: https://mypy.readthedocs.io/en/stable/_refs.html#code-typeddict-unknown-key
[mypy-unimported-reveal]: https://mypy.readthedocs.io/en/stable/_refs.html#code-unimported-reveal
[mypy-union-attr]: https://mypy.readthedocs.io/en/stable/_refs.html#code-union-attr
[mypy-unreachable]: https://mypy.readthedocs.io/en/stable/_refs.html#code-unreachable
[mypy-untyped-decorator]: https://mypy.readthedocs.io/en/stable/_refs.html#code-untyped-decorator
[mypy-unused-awaitable]: https://mypy.readthedocs.io/en/stable/_refs.html#code-unused-awaitable
[mypy-unused-coroutine]: https://mypy.readthedocs.io/en/stable/_refs.html#code-unused-coroutine
[mypy-unused-ignore]: https://mypy.readthedocs.io/en/stable/_refs.html#code-unused-ignore
[mypy-used-before-def]: https://mypy.readthedocs.io/en/stable/_refs.html#code-used-before-def
[mypy-valid-newtype]: https://mypy.readthedocs.io/en/stable/_refs.html#code-valid-newtype
[mypy-valid-type]: https://mypy.readthedocs.io/en/stable/_refs.html#code-valid-type
[mypy-var-annotated]: https://mypy.readthedocs.io/en/stable/_refs.html#code-var-annotated
[reportabstractusage]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportAbstractUsage
[reportargumenttype]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportArgumentType
[reportassertalwaystrue]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportAssertAlwaysTrue
[reportasserttypefailure]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportAssertTypeFailure
[reportassignmenttype]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportAssignmentType
[reportattributeaccessissue]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportAttributeAccessIssue
[reportcallindefaultinitializer]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportCallInDefaultInitializer
[reportcallissue]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportCallIssue
[reportconstantredefinition]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportConstantRedefinition
[reportdeprecated]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportDeprecated
[reportduplicateimport]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportDuplicateImport
[reportexplicitany]: https://docs.basedpyright.com/latest/benefits-over-pyright/new-diagnostic-rules/#reportexplicitany
[reportfunctionmemberaccess]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportFunctionMemberAccess
[reportgeneraltypeissues]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportGeneralTypeIssues
[reportignorecommentwithoutrule]: https://docs.basedpyright.com/latest/benefits-over-pyright/new-diagnostic-rules/#reportignorecommentwithoutrule
[reportimplicitoverride]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportImplicitOverride
[reportimplicitstringconcatenation]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportImplicitStringConcatenation
[reportimportcycles]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportImportCycles
[reportincompatiblemethodoverride]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportIncompatibleMethodOverride
[reportincompatiblevariableoverride]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportIncompatibleVariableOverride
[reportincompletestub]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportIncompleteStub
[reportinconsistentconstructor]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportInconsistentConstructor
[reportinconsistentoverload]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportInconsistentOverload
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
[reportoptionalcall]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportOptionalCall
[reportoptionalcontextmanager]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportOptionalContextManager
[reportoptionaliterable]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportOptionalIterable
[reportoptionalmemberaccess]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportOptionalMemberAccess
[reportoptionaloperand]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportOptionalOperand
[reportoptionalsubscript]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportOptionalSubscript
[reportoverlappingoverload]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportOverlappingOverload
[reportpossiblyunboundvariable]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportPossiblyUnboundVariable
[reportprivateimportusage]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportPrivateImportUsage
[reportprivatelocalimportusage]: https://docs.basedpyright.com/latest/benefits-over-pyright/new-diagnostic-rules/#reportprivatelocalimportusage
[reportprivateusage]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportPrivateUsage
[reportpropertytypemismatch]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportPropertyTypeMismatch
[reportredeclaration]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportRedeclaration
[reportreturntype]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportReturnType
[reportselfclsparametername]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportSelfClsParameterName
[reporttypecommentusage]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportTypeCommentUsage
[reporttypeddictnotrequiredaccess]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportTypedDictNotRequiredAccess
[reportunboundvariable]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnboundVariable
[reportundefinedvariable]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUndefinedVariable
[reportunhashable]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnhashable
[reportuninitializedinstancevariable]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUninitializedInstanceVariable
[reportunknownargumenttype]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnknownArgumentType
[reportunknownlambdatype]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnknownLambdaType
[reportunknownmembertype]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnknownMemberType
[reportunknownparametertype]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnknownParameterType
[reportunknownvariabletype]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnknownVariableType
[reportunnecessarycast]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnnecessaryCast
[reportunnecessarycomparison]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnnecessaryComparison
[reportunnecessarycontains]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnnecessaryContains
[reportunnecessaryisinstance]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnnecessaryIsInstance
[reportunnecessarytypeignorecomment]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnnecessaryTypeIgnoreComment
[reportunreachable]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnreachable
[reportunsupporteddunderall]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnsupportedDunderAll
[reportuntypedbaseclass]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUntypedBaseClass
[reportuntypedclassdecorator]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUntypedClassDecorator
[reportuntypedfunctiondecorator]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUntypedFunctionDecorator
[reportuntypednamedtuple]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUntypedNamedTuple
[reportunusedcallresult]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnusedCallResult
[reportunusedclass]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnusedClass
[reportunusedcoroutine]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnusedCoroutine
[reportunusedexcept]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnusedExcept
[reportunusedexpression]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnusedExpression
[reportunusedfunction]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnusedFunction
[reportunusedimport]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnusedImport
[reportunusedparameter]: https://docs.basedpyright.com/latest/benefits-over-pyright/new-diagnostic-rules/#reportunusedparameter
[reportunusedvariable]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportUnusedVariable
[reportwildcardimportfromlibrary]: https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportWildcardImportFromLibrary
[ruff-10137]: https://github.com/astral-sh/ruff/issues/10137
[ruff-ann]: https://docs.astral.sh/ruff/rules/#flake8-annotations-ann
[ruff-ann401]: https://docs.astral.sh/ruff/rules/any-type/
[ruff-arg]: https://docs.astral.sh/ruff/rules/#flake8-unused-arguments-arg
[ruff-b006]: https://docs.astral.sh/ruff/rules/mutable-argument-default/
[ruff-b008]: https://docs.astral.sh/ruff/rules/function-call-in-default-argument/
[ruff-b018]: https://docs.astral.sh/ruff/rules/useless-expression/
[ruff-b025]: https://docs.astral.sh/ruff/rules/duplicate-try-block-exception/
[ruff-f401]: https://docs.astral.sh/ruff/rules/unused-import/
[ruff-f403]: https://docs.astral.sh/ruff/rules/undefined-local-with-import-star/
[ruff-f631]: https://docs.astral.sh/ruff/rules/assert-tuple/
[ruff-f811]: https://docs.astral.sh/ruff/rules/redefined-while-unused/
[ruff-f822]: https://docs.astral.sh/ruff/rules/undefined-export/
[ruff-f823]: https://docs.astral.sh/ruff/rules/undefined-local/
[ruff-f841]: https://docs.astral.sh/ruff/rules/unused-variable/
[ruff-i001]: https://docs.astral.sh/ruff/rules/unsorted-imports/
[ruff-isc001]: https://docs.astral.sh/ruff/rules/single-line-implicit-string-concatenation/
[ruff-isc002]: https://docs.astral.sh/ruff/rules/multi-line-implicit-string-concatenation/
[ruff-n804]: https://docs.astral.sh/ruff/rules/invalid-first-argument-name-for-class-method/
[ruff-n805]: https://docs.astral.sh/ruff/rules/invalid-first-argument-name-for-method/
[ruff-pgh003]: https://docs.astral.sh/ruff/rules/blanket-type-ignore/
[ruff-plc2701]: https://docs.astral.sh/ruff/rules/import-private-name/
[ruff-ple0604]: https://docs.astral.sh/ruff/rules/invalid-all-object/
[ruff-ple0605]: https://docs.astral.sh/ruff/rules/invalid-all-format/
[ruff-pyi010]: https://docs.astral.sh/ruff/rules/non-empty-stub-body/
[ruff-pyi017]: https://docs.astral.sh/ruff/rules/complex-assignment-in-stub/
[ruff-pyi024]: https://docs.astral.sh/ruff/rules/collections-named-tuple/
[ruff-pyi033]: https://docs.astral.sh/ruff/rules/type-comment-in-stub/
[ruff-pyi048]: https://docs.astral.sh/ruff/rules/stub-body-multiple-statements/
[ruff-pyi052]: https://docs.astral.sh/ruff/rules/unannotated-assignment-in-stub/
[ruff-pyi056]: https://docs.astral.sh/ruff/rules/unsupported-method-call-on-all/
[ruff-slf001]: https://docs.astral.sh/ruff/rules/private-member-access/
[ruff-w605]: https://docs.astral.sh/ruff/rules/invalid-escape-sequence/
[ty-1017]: https://github.com/astral-sh/ty/issues/1017
[ty-103]: https://github.com/astral-sh/ty/issues/103
[ty-1060]: https://github.com/astral-sh/ty/issues/1060
[ty-1577]: https://github.com/astral-sh/ty/issues/1577
[ty-1948]: https://github.com/astral-sh/ty/issues/1948
[ty-200]: https://github.com/astral-sh/ty/issues/200
[ty-2158]: https://github.com/astral-sh/ty/issues/2158
[ty-2810]: https://github.com/astral-sh/ty/issues/2810
[ty-2954]: https://github.com/astral-sh/ty/issues/2954
[ty-3633]: https://github.com/astral-sh/ty/issues/3633
[ty-3636]: https://github.com/astral-sh/ty/issues/3636
[ty-3637]: https://github.com/astral-sh/ty/issues/3637
[ty-3638]: https://github.com/astral-sh/ty/issues/3638
[ty-3647]: https://github.com/astral-sh/ty/issues/3647
[ty-3651]: https://github.com/astral-sh/ty/issues/3651
[ty-3652]: https://github.com/astral-sh/ty/issues/3652
[ty-3701]: https://github.com/astral-sh/ty/issues/3701
[ty-3781]: https://github.com/astral-sh/ty/issues/3781
[ty-576]: https://github.com/astral-sh/ty/issues/576
[ty-abstract-and-final-method]: reference/rules.md#abstract-and-final-method
[ty-abstract-method-in-final-class]: reference/rules.md#abstract-method-in-final-class
[ty-blanket-ignore-comment]: reference/rules.md#blanket-ignore-comment
[ty-call-abstract-method]: reference/rules.md#call-abstract-method
[ty-call-non-callable]: reference/rules.md#call-non-callable
[ty-conflicting-declarations]: reference/rules.md#conflicting-declarations
[ty-conflicting-metaclass]: reference/rules.md#conflicting-metaclass
[ty-cyclic-class-definition]: reference/rules.md#cyclic-class-definition
[ty-dataclass-field-order]: reference/rules.md#dataclass-field-order
[ty-deprecated]: reference/rules.md#deprecated
[ty-division-by-zero]: reference/rules.md#division-by-zero
[ty-duplicate-base]: reference/rules.md#duplicate-base
[ty-duplicate-kw-only]: reference/rules.md#duplicate-kw-only
[ty-dynamic-function-decorator-return]: reference/rules.md#dynamic-function-decorator-return
[ty-empty-body]: reference/rules.md#empty-body
[ty-final-on-non-method]: reference/rules.md#final-on-non-method
[ty-final-without-value]: reference/rules.md#final-without-value
[ty-inconsistent-mro]: reference/rules.md#inconsistent-mro
[ty-index-out-of-bounds]: reference/rules.md#index-out-of-bounds
[ty-invalid-argument-type]: reference/rules.md#invalid-argument-type
[ty-invalid-assignment]: reference/rules.md#invalid-assignment
[ty-invalid-attribute-access]: reference/rules.md#invalid-attribute-access
[ty-invalid-attribute-override]: reference/rules.md#invalid-attribute-override
[ty-invalid-await]: reference/rules.md#invalid-await
[ty-invalid-base]: reference/rules.md#invalid-base
[ty-invalid-context-manager]: reference/rules.md#invalid-context-manager
[ty-invalid-dataclass]: reference/rules.md#invalid-dataclass
[ty-invalid-exception-caught]: reference/rules.md#invalid-exception-caught
[ty-invalid-explicit-override]: reference/rules.md#invalid-explicit-override
[ty-invalid-frozen-dataclass-subclass]: reference/rules.md#invalid-frozen-dataclass-subclass
[ty-invalid-key]: reference/rules.md#invalid-key
[ty-invalid-legacy-type-variable]: reference/rules.md#invalid-legacy-type-variable
[ty-invalid-metaclass]: reference/rules.md#invalid-metaclass
[ty-invalid-method-override]: reference/rules.md#invalid-method-override
[ty-invalid-module-getattr-call]: reference/rules.md#invalid-module-getattr-call
[ty-invalid-newtype]: reference/rules.md#invalid-newtype
[ty-invalid-overload]: reference/rules.md#invalid-overload
[ty-invalid-parameter-default]: reference/rules.md#invalid-parameter-default
[ty-invalid-protocol]: reference/rules.md#invalid-protocol
[ty-invalid-raise]: reference/rules.md#invalid-raise
[ty-invalid-return-type]: reference/rules.md#invalid-return-type
[ty-invalid-type-arguments]: reference/rules.md#invalid-type-arguments
[ty-invalid-type-form]: reference/rules.md#invalid-type-form
[ty-invalid-type-guard-definition]: reference/rules.md#invalid-type-guard-definition
[ty-invalid-type-variable-bound]: reference/rules.md#invalid-type-variable-bound
[ty-invalid-type-variable-constraints]: reference/rules.md#invalid-type-variable-constraints
[ty-invalid-type-variable-default]: reference/rules.md#invalid-type-variable-default
[ty-invalid-typed-dict-field]: reference/rules.md#invalid-typed-dict-field
[ty-invalid-yield]: reference/rules.md#invalid-yield
[ty-isinstance-against-protocol]: reference/rules.md#isinstance-against-protocol
[ty-isinstance-against-typed-dict]: reference/rules.md#isinstance-against-typed-dict
[ty-mismatched-type-name]: reference/rules.md#mismatched-type-name
[ty-missing-argument]: reference/rules.md#missing-argument
[ty-missing-override-decorator]: reference/rules.md#missing-override-decorator
[ty-missing-type-argument]: reference/rules.md#missing-type-argument
[ty-missing-typed-dict-key]: reference/rules.md#missing-typed-dict-key
[ty-no-matching-overload]: reference/rules.md#no-matching-overload
[ty-not-iterable]: reference/rules.md#not-iterable
[ty-not-subscriptable]: reference/rules.md#not-subscriptable
[ty-override-of-final-method]: reference/rules.md#override-of-final-method
[ty-override-of-final-variable]: reference/rules.md#override-of-final-variable
[ty-parameter-already-assigned]: reference/rules.md#parameter-already-assigned
[ty-positional-only-parameter-as-kwarg]: reference/rules.md#positional-only-parameter-as-kwarg
[ty-possibly-missing-attribute]: reference/rules.md#possibly-missing-attribute
[ty-possibly-unresolved-reference]: reference/rules.md#possibly-unresolved-reference
[ty-redundant-cast]: reference/rules.md#redundant-cast
[ty-subclass-of-final-class]: reference/rules.md#subclass-of-final-class
[ty-too-many-positional-arguments]: reference/rules.md#too-many-positional-arguments
[ty-type-assertion-failure]: reference/rules.md#type-assertion-failure
[ty-unbound-type-variable]: reference/rules.md#unbound-type-variable
[ty-undefined-reveal]: reference/rules.md#undefined-reveal
[ty-unknown-argument]: reference/rules.md#unknown-argument
[ty-unresolved-attribute]: reference/rules.md#unresolved-attribute
[ty-unresolved-import]: reference/rules.md#unresolved-import
[ty-unresolved-reference]: reference/rules.md#unresolved-reference
[ty-unsound-return-statement]: reference/rules.md#unsound-return-statement
[ty-unsound-yield]: reference/rules.md#unsound-yield
[ty-unsupported-operator]: reference/rules.md#unsupported-operator
[ty-unused-awaitable]: reference/rules.md#unused-awaitable
[ty-unused-ignore-comment]: reference/rules.md#unused-ignore-comment
[ty-unused-type-ignore-comment]: reference/rules.md#unused-type-ignore-comment
