# Changelog

## 0.0.1-alpha.12

### Bug fixes

- Avoid duplicate diagnostic when reporting errors in unpacked assignments ([#18897](https://github.com/astral-sh/ruff/pull/18897))
- Fix panics when "pulling types" for `ClassVar` or `Final` parameterized with >1 argument ([#18824](https://github.com/astral-sh/ruff/pull/18824)). These could cause issues when hovering over symbols in an IDE.

### Improved modeling of Python runtime semantics

- Add support for `@staticmethod`s ([#18809](https://github.com/astral-sh/ruff/pull/18809))
- Assignments in the body of a staticmethod are never instance attributes ([#18587](https://github.com/astral-sh/ruff/pull/18587))
- Report when a dataclass contains more than one `KW_ONLY` field ([#18731](https://github.com/astral-sh/ruff/pull/18731))

### Type narrowing improvements

- Ty will now perform `isinstance()` and `issubclass()` narrowing when the second argument is a union type, intersection type or `TypeVar` type ([#18900](https://github.com/astral-sh/ruff/pull/18900))
- Ty now narrows types in comprehensions and generator expressions ([#18934](https://github.com/astral-sh/ruff/pull/18934))
- Understand two `NominalInstanceType`s as disjoint types if attempting to use multiple inheritance with their underlying classes would result in an instance memory layout conflict ([#18864](https://github.com/astral-sh/ruff/pull/18864))

### Other typing semantics features

- Support "mixed" tuples such as `tuple[int, *tuple[str, ...]]` ([#18600](https://github.com/astral-sh/ruff/pull/18600), [#18901](https://github.com/astral-sh/ruff/pull/18901))
- Support type inference for subscript expressions on union types ([#18846](https://github.com/astral-sh/ruff/pull/18846))
- Introduce a new subtyping framework in which gradual types do participate, allowing for more advanced union type simplification ([#18799](https://github.com/astral-sh/ruff/pull/18799))
- Surface the matched overload diagnostic directly when reporting a diagnostic for an invalid call to an overloaded function ([#18452](https://github.com/astral-sh/ruff/pull/18452))

### Improvements to server autocompletions

- Add completions for `from module import <CURSOR>` ([#18830](https://github.com/astral-sh/ruff/pull/18830))
- Enforce sort order of completions ([#18917](https://github.com/astral-sh/ruff/pull/18917))
- Include imported sub-modules as attributes on modules for completions ([#18898](https://github.com/astral-sh/ruff/pull/18898))

### Configuration

- Anchor all `src.exclude` patterns, for consistency with `src.include` patterns ([#18685](https://github.com/astral-sh/ruff/pull/18685))
- Change `environment.root` to accept multiple paths ([#18913](https://github.com/astral-sh/ruff/pull/18913))
- Rename `src.root` setting to `environment.root` ([#18760](https://github.com/astral-sh/ruff/pull/18760))
- Support `--python=<symlink to executable>` ([#18827](https://github.com/astral-sh/ruff/pull/18827))

### Contributors

- [@BurntSushi](https://github.com/BurntSushi)
- [@InSyncWithFoo](https://github.com/InSyncWithFoo)
- [@suneettipirneni](https://github.com/suneettipirneni)
- [@AlexWaygood](https://github.com/AlexWaygood)
- [@dhruvmanila](https://github.com/dhruvmanila)
- [@sharkdp](https://github.com/sharkdp)
- [@MichaReiser](https://github.com/MichaReiser)
- [@med1844](https://github.com/med1844)
- [@dcreager](https://github.com/dcreager)
- [@carljm](https://github.com/carljm)

## 0.0.1-alpha.11

### Breaking changes

- Stabilize auto-complete; remove the opt-in experimental setting ([#18650](https://github.com/astral-sh/ruff/pull/18650))

### Bug fixes

- Fix binary expression inference between Boolean literals and `bool` instances ([#18663](https://github.com/astral-sh/ruff/pull/18663))
- Fix panic that could occur when printing a class's "header" in diagnostic messages ([#18670](https://github.com/astral-sh/ruff/pull/18670))
- Fix panic when attempting to provide autocompletions for an instance of a class that assigns attributes to `self[0]` ([#18707](https://github.com/astral-sh/ruff/pull/18707))
- Fix panics when "pulling types" for various special forms that have the wrong number of parameters. These could cause issues when hovering over symbols in an IDE. ([#18642](https://github.com/astral-sh/ruff/pull/18642))

### Typing semantics and features

- Support type narrowing for attribute and subscript expressions ([#17643](https://github.com/astral-sh/ruff/pull/17643))
- Add partial support for `TypeIs` ([#18589](https://github.com/astral-sh/ruff/pull/18589))
- Support `dataclasses.KW_ONLY` ([#18677](https://github.com/astral-sh/ruff/pull/18677))
- Filter overloads based on `Any` / `Unknown` ([#18607](https://github.com/astral-sh/ruff/pull/18607))
- Improve reachability analysis ([#18621](https://github.com/astral-sh/ruff/pull/18621))
- Model `T: Never` as a subtype of `Never` ([#18687](https://github.com/astral-sh/ruff/pull/18687))
- Update typeshed stubs ([#18679](https://github.com/astral-sh/ruff/pull/18679)): [typeshed diff](https://github.com/python/typeshed/compare/5a3c495d2f6fa9b68cd99f39feba4426e4d17ea9...ecd5141cc036366cc9e3ca371096d6a14b0ccd13)

### Configuration

- Allow overriding rules for specific files ([#18648](https://github.com/astral-sh/ruff/pull/18648))

### Server

- Add `python.ty.disableLanguageServices` config ([#18230](https://github.com/astral-sh/ruff/pull/18230))

### Contributors

- [@dhruvmanila](https://github.com/dhruvmanila)
- [@felixscherz](https://github.com/felixscherz)
- [@MichaReiser](https://github.com/MichaReiser)
- [@alpaylan](https://github.com/alpaylan)
- [@mtshiba](https://github.com/mtshiba)
- [@github-actions](https://github.com/github-actions)
- [@BurntSushi](https://github.com/BurntSushi)
- [@InSyncWithFoo](https://github.com/InSyncWithFoo)
- [@AlexWaygood](https://github.com/AlexWaygood)
- [@abhijeetbodas2001](https://github.com/abhijeetbodas2001)
- [@sharkdp](https://github.com/sharkdp)
- [@ibraheemdev](https://github.com/ibraheemdev)

## 0.0.1-alpha.10

### Server

- Improve support for `object.<CURSOR>` completions ([#18629](https://github.com/astral-sh/ruff/pull/18629))

### Configuration

- Add file inclusion and exclusion ([#18498](https://github.com/astral-sh/ruff/pull/18498))
- Infer the Python version from `--python=<system installation>` on Unix ([#18550](https://github.com/astral-sh/ruff/pull/18550))

### Bug fixes

- Delay computation of 'unbound' visibility for implicit instance attributes ([#18669](https://github.com/astral-sh/ruff/pull/18669)).
    This fixes a significant performance regression in version 0.0.1-alpha.9.

### Typing semantics and features

- Support the `del` statement; model implicit deletion of except handler names ([#18593](https://github.com/astral-sh/ruff/pull/18593))

### Release

- Include ruff/ directory in release source tarballs ([#617](https://github.com/astral-sh/ty/pull/617))

### Contributors

- [@AlexWaygood](https://github.com/AlexWaygood)
- [@BurntSushi](https://github.com/BurntSushi)
- [@Gankra](https://github.com/Gankra)
- [@mtshiba](https://github.com/mtshiba)
- [@sharkdp](https://github.com/sharkdp)
- [@dhruvmanila](https://github.com/dhruvmanila)
- [@MichaReiser](https://github.com/MichaReiser)

## 0.0.1-alpha.9

### Typing semantics and features

- Add generic inference for dataclasses ([#18443](https://github.com/astral-sh/ruff/pull/18443))
- Add support for global `__debug__` constant ([#18540](https://github.com/astral-sh/ruff/pull/18540))
- Argument type expansion for overload call evaluation ([#18382](https://github.com/astral-sh/ruff/pull/18382))
- Exclude members starting with `_abc_` from a protocol interface ([#18467](https://github.com/astral-sh/ruff/pull/18467))
- Infer `list[T]` for starred target in unpacking ([#18401](https://github.com/astral-sh/ruff/pull/18401))
- Infer `list[T]` when unpacking non-tuple type ([#18438](https://github.com/astral-sh/ruff/pull/18438))
- Support type annotation for legacy typing aliases for generic classes ([#18404](https://github.com/astral-sh/ruff/pull/18404))
- Allow using `dataclasses.dataclass` as a function ([#18440](https://github.com/astral-sh/ruff/pull/18440))
- Type narrowing for attribute/subscript assignments ([#18041](https://github.com/astral-sh/ruff/pull/18041))

### Diagnostics

- Add hints to `invalid-type-form` for common mistakes ([#18543](https://github.com/astral-sh/ruff/pull/18543))
- Add subdiagnostic suggestion to `unresolved-reference` diagnostic when variable exists on `self` ([#18444](https://github.com/astral-sh/ruff/pull/18444))
- Track the origin of the `environment.python` setting for better error messages ([#18483](https://github.com/astral-sh/ruff/pull/18483))

### CLI

- Fix `--python` argument for Windows, and improve error messages for bad `--python` arguments ([#18457](https://github.com/astral-sh/ruff/pull/18457))

### Bug fixes

- Meta-type of type variables should be `type[..]` ([#18439](https://github.com/astral-sh/ruff/pull/18439))
- Only consider a type `T` a subtype of a protocol `P` if all of `P`'s members are fully bound on `T` ([#18466](https://github.com/astral-sh/ruff/pull/18466))
- Fix false positives for legacy `ParamSpec`s inside `Callable` type expressions ([#18426](https://github.com/astral-sh/ruff/pull/18426))
- Fix panic when pulling types for `UnaryOp` expressions inside `Literal` slices ([#18536](https://github.com/astral-sh/ruff/pull/18536))
- Fix panic when trying to pull types for attribute expressions inside `Literal` type expressions ([#18535](https://github.com/astral-sh/ruff/pull/18535))
- Fix panic when trying to pull types for subscript expressions inside `Callable` type expressions ([#18534](https://github.com/astral-sh/ruff/pull/18534))
- Treat lambda functions as instances of `types.FunctionType` ([#18431](https://github.com/astral-sh/ruff/pull/18431))
- Implement disjointness between `Callable` and `SpecialForm` ([#18503](https://github.com/astral-sh/ruff/pull/18503))

### Server

- Fix stale diagnostics in documents on Windows ([#18544](https://github.com/astral-sh/ruff/pull/18544))
- Add support for `object.<CURSOR>` completions ([#18468](https://github.com/astral-sh/ruff/pull/18468))
- Only provide declarations and bindings as completions ([#18456](https://github.com/astral-sh/ruff/pull/18456))

### Documentation

- Add `CONDA_PREFIX` to `--python` documentation ([#18574](https://github.com/astral-sh/ruff/pull/18574))
- Update list of referenced environment variables ([#612](https://github.com/astral-sh/ty/pull/612))
- Document how the default value for `python-version` is determined ([#18549](https://github.com/astral-sh/ruff/pull/18549))
- Document the `"all"` option for `python-platform` ([#18548](https://github.com/astral-sh/ruff/pull/18548))

### Contributors

- [@AlexWaygood](https://github.com/AlexWaygood)
- [@charliermarsh](https://github.com/charliermarsh)
- [@mtshiba](https://github.com/mtshiba)
- [@benbaror](https://github.com/benbaror)
- [@sharkdp](https://github.com/sharkdp)
- [@carljm](https://github.com/carljm)
- [@MichaReiser](https://github.com/MichaReiser)
- [@lipefree](https://github.com/lipefree)
- [@BurntSushi](https://github.com/BurntSushi)
- [@DetachHead](https://github.com/DetachHead)
- [@MatthewMckee4](https://github.com/MatthewMckee4)
- [@suneettipirneni](https://github.com/suneettipirneni)
- [@abhijeetbodas2001](https://github.com/abhijeetbodas2001)
- [@ibraheemdev](https://github.com/ibraheemdev)
- [@dhruvmanila](https://github.com/dhruvmanila)

## 0.0.1-alpha.8

### Typing semantics and features

- Add subtyping between Callable types and class literals with `__init__` ([#17638](https://github.com/astral-sh/ruff/pull/17638))
- Implement implicit inheritance from `Generic[]` for PEP-695 generic classes ([#18283](https://github.com/astral-sh/ruff/pull/18283))
- Infer the Python version from the environment if feasible ([#18057](https://github.com/astral-sh/ruff/pull/18057))
- Support ephemeral uv virtual environments ([#18335](https://github.com/astral-sh/ruff/pull/18335))
- Model that some `Callable` types should have all `FunctionType` attributes available ([#18242](https://github.com/astral-sh/ruff/pull/18242))

### Diagnostics

- Add diagnostic hints for a function that has a non-`None` return-type annotation but no return statements ([#18359](https://github.com/astral-sh/ruff/pull/18359))
- Add hint if async context manager is used in non-async with statement ([#18299](https://github.com/astral-sh/ruff/pull/18299))
- Improve diagnostics if the user attempts to import a stdlib module that does not exist on their configured Python version ([#18403](https://github.com/astral-sh/ruff/pull/18403))
- Tell the user why we inferred a certain Python version when reporting version-specific syntax errors ([#18295](https://github.com/astral-sh/ruff/pull/18295))

### Bug fixes

- Fix multithreading related hangs and panics ([#18238](https://github.com/astral-sh/ruff/pull/18238))
- Ensure `Literal` types are considered assignable to anything their `Instance` supertypes are assignable to ([#18351](https://github.com/astral-sh/ruff/pull/18351))
- Callable types are disjoint from non-callable `@final` nominal instance types ([#18368](https://github.com/astral-sh/ruff/pull/18368))
- Support callability of bound/constrained typevars ([#18389](https://github.com/astral-sh/ruff/pull/18389))

### Server

- Fix server hang after shutdown request ([#18414](https://github.com/astral-sh/ruff/pull/18414))
- Improve completions by leveraging scopes ([#18281](https://github.com/astral-sh/ruff/pull/18281))
- Support cancellation and retry in the server ([#18273](https://github.com/astral-sh/ruff/pull/18273))
- Support publishing diagnostics in the server ([#18309](https://github.com/astral-sh/ruff/pull/18309))

### CLI

- Add `--config-file` CLI arg ([#18083](https://github.com/astral-sh/ruff/pull/18083))

### Contributors

- [@AlexWaygood](https://github.com/AlexWaygood)
- [@BurntSushi](https://github.com/BurntSushi)
- [@lipefree](https://github.com/lipefree)
- [@MatthewMckee4](https://github.com/MatthewMckee4)
- [@dhruvmanila](https://github.com/dhruvmanila)
- [@zanieb](https://github.com/zanieb)
- [@carljm](https://github.com/carljm)
- [@thejchap](https://github.com/thejchap)
- [@sharkdp](https://github.com/sharkdp)
- [@InSyncWithFoo](https://github.com/InSyncWithFoo)
- [@MichaReiser](https://github.com/MichaReiser)

## 0.0.1-alpha.7

### Bug fixes

- Implement Python's floor-division semantics for `Literal` `int`s ([#18249](https://github.com/astral-sh/ruff/pull/18249))
- Don't warn about a `yield` expression not being in a function if the `yield` expression is in a function ([#18008](https://github.com/astral-sh/ruff/pull/18008))
- Fix inference of attribute writes to unions/intersections that including module-literal types ([#18313](https://github.com/astral-sh/ruff/pull/18313))
- Fix false-positive diagnostics in binary comparison inference logic for intersection types ([#18266](https://github.com/astral-sh/ruff/pull/18266))
- Fix instance vs callable subtyping/assignability ([#18260](https://github.com/astral-sh/ruff/pull/18260))
- Ignore `ClassVar` declarations when resolving instance members ([#18241](https://github.com/astral-sh/ruff/pull/18241))
- Fix crash when hovering over a `ty_extensions.Intersection[A, B]` expression in an IDE context ([#18321](https://github.com/astral-sh/ruff/pull/18321))
- Respect `MRO_NO_OBJECT_FALLBACK` policy when looking up symbols on `type` instances ([#18312](https://github.com/astral-sh/ruff/pull/18312))
- `get_protocol_members` returns a frozenset, not a tuple ([#18284](https://github.com/astral-sh/ruff/pull/18284))

### Typing semantics and features

- Support `import <namespace>` and `from <namespace> import module` ([#18137](https://github.com/astral-sh/ruff/pull/18137))
- Support frozen dataclasses ([#17974](https://github.com/astral-sh/ruff/pull/17974))
- Understand that the presence of a `__getattribute__` method indicates arbitrary members can exist on a type ([#18280](https://github.com/astral-sh/ruff/pull/18280))
- Add a subdiagnostic if `invalid-return-type` is emitted on a method with an empty body on a non-protocol subclass of a protocol class ([#18243](https://github.com/astral-sh/ruff/pull/18243))
- Improve `invalid-type-form` diagnostic where a module-literal type is used in a type expression and the module has a member which would be valid in a type expression ([#18244](https://github.com/astral-sh/ruff/pull/18244))
- Split `invalid-base` error code into two error codes ([#18245](https://github.com/astral-sh/ruff/pull/18245))
- Rename `call-possibly-unbound-method` to `possibly-unbound-implicit-call` ([#18017](https://github.com/astral-sh/ruff/pull/18017))

### Configuration

- Add `tests` to `src.root` by default if a `tests/` directory exists and is not a package ([#18286](https://github.com/astral-sh/ruff/pull/18286))
- Tell the user why we inferred the Python version we inferred ([#18082](https://github.com/astral-sh/ruff/pull/18082))
- Add support for detecting activated Conda and Pixi environments ([#18267](https://github.com/astral-sh/ruff/pull/18267))
- Move `respect-ignore-files` configuration setting under `src` section ([#18322](https://github.com/astral-sh/ruff/pull/18322))

### Server

- Fix server panic when calling `system_mut` ([#18252](https://github.com/astral-sh/ruff/pull/18252))
- Abort process if worker thread panics ([#18211](https://github.com/astral-sh/ruff/pull/18211))
- Gracefully handle salsa cancellations and panics in background request handlers ([#18254](https://github.com/astral-sh/ruff/pull/18254))

### Contributors

- [@felixscherz](https://github.com/felixscherz)
- [@carljm](https://github.com/carljm)
- [@j178](https://github.com/j178)
- [@thejchap](https://github.com/thejchap)
- [@brainwane](https://github.com/brainwane)
- [@AlexWaygood](https://github.com/AlexWaygood)
- [@lipefree](https://github.com/lipefree)
- [@InSyncWithFoo](https://github.com/InSyncWithFoo)
- [@brandtbucher](https://github.com/brandtbucher)
- [@MichaReiser](https://github.com/MichaReiser)
- [@maxmynter](https://github.com/maxmynter)
- [@fabridamicelli](https://github.com/fabridamicelli)
- [@sharkdp](https://github.com/sharkdp)

## 0.0.1-alpha.6

### Server

- Add rule link to server diagnostics ([#18128](https://github.com/astral-sh/ruff/pull/18128))
- Avoid panicking when there are multiple workspaces ([#18151](https://github.com/astral-sh/ruff/pull/18151))
- Show related information in diagnostic ([#17359](https://github.com/astral-sh/ruff/pull/17359))

### Configuration

- Default `src.root` setting to `['.', '<project_name>']` if an `src/` directory does not exist but a `<project-name>/<project-name>` directory does exist ([#18141](https://github.com/astral-sh/ruff/pull/18141))

### Typing semantics and features

- Consider a class with a dynamic element in its MRO assignable to any subtype of `type` ([#18205](https://github.com/astral-sh/ruff/pull/18205))
- Ensure that a function-literal type is always considered equivalent to itself ([#18227](https://github.com/astral-sh/ruff/pull/18227))
- Promote literals when inferring class specializations from constructors ([#18102](https://github.com/astral-sh/ruff/pull/18102))
- Support `typing.TypeAliasType` ([#18156](https://github.com/astral-sh/ruff/pull/18156))
- Infer function-call type variables in both directions ([#18155](https://github.com/astral-sh/ruff/pull/18155))

### Improvements to modeling of runtime semantics

- Integer indexing into `bytes` returns `int` ([#18218](https://github.com/astral-sh/ruff/pull/18218))
- Emit `invalid-exception-caught` diagnostics even when the caught exception is not bound to a variable ([#18202](https://github.com/astral-sh/ruff/pull/18202))

### Usability improvements

- Add hint to some diagnostics that [PEP 604](https://peps.python.org/pep-0604/) union syntax is only available on Python 3.10+ ([#18192](https://github.com/astral-sh/ruff/pull/18192))
- Add note to `unresolved-import` diagnostic hinting to users to configure their Python environment ([#18207](https://github.com/astral-sh/ruff/pull/18207))
- Make `division-by-zero` an opt-in diagnostic rather than opt-out ([#18220](https://github.com/astral-sh/ruff/pull/18220))

### Import resolution improvements

- Add support for PyPy virtual environments ([#18203](https://github.com/astral-sh/ruff/pull/18203))

### Contributors

- [@dhruvmanila](https://github.com/dhruvmanila)
- [@InSyncWithFoo](https://github.com/InSyncWithFoo)
- [@AlexWaygood](https://github.com/AlexWaygood)
- [@MichaReiser](https://github.com/MichaReiser)
- [@BradonZhang](https://github.com/BradonZhang)
- [@dcreager](https://github.com/dcreager)
- [@danielhollas](https://github.com/danielhollas)
- [@esadek](https://github.com/esadek)
- [@kiran-4444](https://github.com/kiran-4444)
- [@Mathemmagician](https://github.com/Mathemmagician)
- [@sharkdp](https://github.com/sharkdp)
- [@felixscherz](https://github.com/felixscherz)
- [@adamaaronson](https://github.com/adamaaronson)
- [@carljm](https://github.com/carljm)

## 0.0.1-alpha.5

### Bug fixes

- Fix assignability checks for invariant generics parameterized by gradual types ([#18138](https://github.com/astral-sh/ruff/pull/18138))
- Revert boolean expression control flow change which caused a performance regression ([#18150](https://github.com/astral-sh/ruff/pull/18150))
- Remove pyvenv.cfg validation check for lines with multiple `=` ([#18144](https://github.com/astral-sh/ruff/pull/18144))

### Contributors

- [@MatthewMckee4](https://github.com/MatthewMckee4)
- [@AlexWaygood](https://github.com/AlexWaygood)

## 0.0.1-alpha.4

### Enhancements

- Allow unions including `Any`/`Unknown` as bases ([#18094](https://github.com/astral-sh/ruff/pull/18094))
- Better control flow for boolean expressions that are inside if ([#18010](https://github.com/astral-sh/ruff/pull/18010))
- Improve invalid method calls for unmatched overloads ([#18122](https://github.com/astral-sh/ruff/pull/18122))
- Add support for `NamedTuple` 'fallback' attributes ([#18127](https://github.com/astral-sh/ruff/pull/18127))
- `type[…]` is always assignable to `type` ([#18121](https://github.com/astral-sh/ruff/pull/18121))
- Support accessing `__builtins__` global ([#18118](https://github.com/astral-sh/ruff/pull/18118))

### Bug fixes

- Fix relative imports in stub packages ([#18132](https://github.com/astral-sh/ruff/pull/18132))

### Contributors

- [@MatthewMckee4](https://github.com/MatthewMckee4)
- [@felixscherz](https://github.com/felixscherz)
- [@BurntSushi](https://github.com/BurntSushi)
- [@maxmynter](https://github.com/maxmynter)
- [@sharkdp](https://github.com/sharkdp)
- [@TomerBin](https://github.com/TomerBin)
- [@MichaReiser](https://github.com/MichaReiser)

## 0.0.1-alpha.3

### Enhancements

- Include synthesized arguments in displayed counts for `too-many-positional-arguments` ([#18098](https://github.com/astral-sh/ruff/pull/18098))

### Bug fixes

- Fix `redundant-cast` false positives when casting to `Unknown` ([#18111](https://github.com/astral-sh/ruff/pull/18111))
- Fix normalization of unions containing instances parameterized with unions ([#18112](https://github.com/astral-sh/ruff/pull/18112))
- Make dataclass instances adhere to DataclassInstance ([#18115](https://github.com/astral-sh/ruff/pull/18115))

### CLI

- Change layout of extra verbose output and respect `--color` for verbose output ([#18089](https://github.com/astral-sh/ruff/pull/18089))

### Documentation

- Use Cargo-style versions in the changelog ([#397](https://github.com/astral-sh/ty/pull/397))

### Contributors

- [@zanieb](https://github.com/zanieb)
- [@sharkdp](https://github.com/sharkdp)
- [@AlexWaygood](https://github.com/AlexWaygood)
- [@InSyncWithFoo](https://github.com/InSyncWithFoo)
- [@MichaReiser](https://github.com/MichaReiser)

## 0.0.1-alpha.2

### Enhancements

- Improve diagnostics for failure to call overloaded function ([#18073](https://github.com/astral-sh/ruff/pull/18073))
- Fix inconsistent casing in `invalid-return-type` diagnostic ([#18084](https://github.com/astral-sh/ruff/pull/18084))
- Add type-expression syntax link to `invalid-type-expression` diagnostics ([#18104](https://github.com/astral-sh/ruff/pull/18104))

### Bug fixes

- Add cycle handling for unpacking targets ([#18078](https://github.com/astral-sh/ruff/pull/18078))
- Do not look up `__init__` on instances ([#18092](https://github.com/astral-sh/ruff/pull/18092))

### Typing

- Infer parameter specializations of explicitly implemented generic protocols ([#18054](https://github.com/astral-sh/ruff/pull/18054))
- Check assignments to implicit global symbols are assignable to the types declared on `types.ModuleType` ([#18077](https://github.com/astral-sh/ruff/pull/18077))
- Fix various generics-related TODOs ([#18062](https://github.com/astral-sh/ruff/pull/18062))

### Documentation

- Fix rule link in the configuration description ([#381](https://github.com/astral-sh/ty/pull/381))
- Use `https://ty.dev/rules` when linking to the rules table ([#18072](https://github.com/astral-sh/ruff/pull/18072))
- Use `ty server` instead of `ty lsp` ([#360](https://github.com/astral-sh/ty/pull/360))
- Fix missing `>` in HTML anchor tags in CLI reference ([#18096](https://github.com/astral-sh/ruff/pull/18096))
- Fix link to rules docs ([#378](https://github.com/astral-sh/ty/pull/378))
- Fix repository in README transform script ([#361](https://github.com/astral-sh/ty/pull/361))

### Contributors

- [@dhruvmanila](https://github.com/dhruvmanila)
- [@Usul-Dev](https://github.com/Usul-Dev)
- [@dcreager](https://github.com/dcreager)
- [@AlexWaygood](https://github.com/AlexWaygood)
- [@BurntSushi](https://github.com/BurntSushi)
- [@MichaReiser](https://github.com/MichaReiser)
- [@frgfm](https://github.com/frgfm)
- [@kiran-4444](https://github.com/kiran-4444)
- [@sharkdp](https://github.com/sharkdp)
- [@eruditmorina](https://github.com/eruditmorina)

## 0.0.1-alpha.1

### Enhancements

- Add basic support for non-virtual Python environments ([#17991](https://github.com/astral-sh/ruff/pull/17991))
- Do not allow invalid virtual environments from discovered `.venv` or `VIRTUAL_ENV` ([#18003](https://github.com/astral-sh/ruff/pull/18003))
- Refine message for why a rule is enabled ([#18038](https://github.com/astral-sh/ruff/pull/18038))
- Update `--python` to accept paths to executables in environments ([#17954](https://github.com/astral-sh/ruff/pull/17954))
- Improve diagnostics for `assert_type` and `assert_never` ([#18050](https://github.com/astral-sh/ruff/pull/18050))
- Add a note to the diagnostic if a new builtin is used on an old Python version ([#18068](https://github.com/astral-sh/ruff/pull/18068))

### Bug fixes

- Fix infinite recursion bug in `is_disjoint_from` ([#18043](https://github.com/astral-sh/ruff/pull/18043))
- Recognize submodules in self-referential imports ([#18005](https://github.com/astral-sh/ruff/pull/18005))

### Typing

- Allow a class to inherit from an intersection if the intersection contains a dynamic type and the intersection is not disjoint from `type` ([#18055](https://github.com/astral-sh/ruff/pull/18055))
- Allow classes to inherit from `type[Any]` or `type[Unknown]` ([#18060](https://github.com/astral-sh/ruff/pull/18060))
- Apply function specialization to all overloads ([#18020](https://github.com/astral-sh/ruff/pull/18020))
- Implement `DataClassInstance` protocol for dataclasses ([#18018](https://github.com/astral-sh/ruff/pull/18018))
- Induct into instances and subclasses when finding and applying generics ([#18052](https://github.com/astral-sh/ruff/pull/18052))
- Infer parameter specializations of generic aliases ([#18021](https://github.com/astral-sh/ruff/pull/18021))
- Narrowing for `hasattr()` ([#18053](https://github.com/astral-sh/ruff/pull/18053))
- Silence false positives for PEP-695 ParamSpec annotations ([#18001](https://github.com/astral-sh/ruff/pull/18001))
- Understand homogeneous tuple annotations ([#17998](https://github.com/astral-sh/ruff/pull/17998))
- `__file__` is always a string inside a Python module ([#18071](https://github.com/astral-sh/ruff/pull/18071))

### CLI

- Avoid initializing progress bars early ([#18049](https://github.com/astral-sh/ruff/pull/18049))

### Contributors

- [@soof-golan](https://github.com/soof-golan)
- [@ibraheemdev](https://github.com/ibraheemdev)
- [@dhruvmanila](https://github.com/dhruvmanila)
- [@charliermarsh](https://github.com/charliermarsh)
- [@MichaReiser](https://github.com/MichaReiser)
- [@carljm](https://github.com/carljm)
- [@abhijeetbodas2001](https://github.com/abhijeetbodas2001)
- [@zanieb](https://github.com/zanieb)
- [@AlexWaygood](https://github.com/AlexWaygood)
- [@dcreager](https://github.com/dcreager)
- [@mtshiba](https://github.com/mtshiba)
- [@sharkdp](https://github.com/sharkdp)

## 0.0.0-alpha.8

### Changes

- Add `--config` CLI arg ([#17697](https://github.com/astral-sh/ruff/pull/17697))
- Add CLI documentation and update README ([#284](https://github.com/astral-sh/ty/pull/284))
- Add a warning about pre-release status to the CLI ([#17983](https://github.com/astral-sh/ruff/pull/17983))
- Add missing bitwise-operator branches for boolean and integer arithmetic ([#17949](https://github.com/astral-sh/ruff/pull/17949))
- Add progress bar for `ty check` ([#17965](https://github.com/astral-sh/ruff/pull/17965))
- Add CLI reference ([#17978](https://github.com/astral-sh/ruff/pull/17978))
- Change default severity for `unbound-reference` to `error` ([#17936](https://github.com/astral-sh/ruff/pull/17936))
- Change range of `revealed-type` diagnostic to be the range of the argument passed in, not the whole call ([#17980](https://github.com/astral-sh/ruff/pull/17980))
- Default to latest supported Python version ([#17938](https://github.com/astral-sh/ruff/pull/17938))
- Display "All checks passed!" message in green ([#17982](https://github.com/astral-sh/ruff/pull/17982))
- Document configuration schema ([#17950](https://github.com/astral-sh/ruff/pull/17950))
- Generate and add rules table ([#17953](https://github.com/astral-sh/ruff/pull/17953))
- Handle type variables that have other type variables as a default ([#17956](https://github.com/astral-sh/ruff/pull/17956))
- Ignore `possibly-unresolved-reference` by default ([#17934](https://github.com/astral-sh/ruff/pull/17934))
- Implement `global` handling and `load-before-global-declaration` syntax error ([#17637](https://github.com/astral-sh/ruff/pull/17637))
- Make `unused-ignore-comment` disabled by default for now ([#17955](https://github.com/astral-sh/ruff/pull/17955))
- Recognise functions containing `yield from` expressions as being generator functions ([#17930](https://github.com/astral-sh/ruff/pull/17930))
- Fix stack overflow on recursive protocols ([#17929](https://github.com/astral-sh/ruff/pull/17929))
- Report duplicate `Protocol` or `Generic` base classes with `[duplicate-base]`, not `[inconsistent-mro]` ([#17971](https://github.com/astral-sh/ruff/pull/17971))
- Respect the gradual guarantee when reporting errors in resolving MROs ([#17962](https://github.com/astral-sh/ruff/pull/17962))
- Support `typing.Self` in methods ([#17689](https://github.com/astral-sh/ruff/pull/17689))
- Support extending `__all__` from an imported module even when the module is not an `ExprName` node ([#17947](https://github.com/astral-sh/ruff/pull/17947))
- Support extending `__all__` with a literal tuple or set as well as a literal list ([#17948](https://github.com/astral-sh/ruff/pull/17948))
- Understand classes that inherit from subscripted `Protocol[]` as generic ([#17832](https://github.com/astral-sh/ruff/pull/17832))
- Update ty metadata ([#17943](https://github.com/astral-sh/ruff/pull/17943))
- Add `py.typed` ([#276](https://github.com/astral-sh/ty/pull/276))
- Bottom-up improvement of diagnostic messages for union type function calls ([#17984](https://github.com/astral-sh/ruff/pull/17984))
- Fix more ecosystem/fuzzer panics with fixpoint ([#17758](https://github.com/astral-sh/ruff/pull/17758))
- Remove `lint:` prefix from top-level diagnostic preamble ([#17987](https://github.com/astral-sh/ruff/pull/17987))

### Contributors

- [@Glyphack](https://github.com/Glyphack)
- [@BurntSushi](https://github.com/BurntSushi)
- [@paul-nameless](https://github.com/paul-nameless)
- [@MichaReiser](https://github.com/MichaReiser)
- [@ntbre](https://github.com/ntBre)
- [@ibraheemdev](https://github.com/ibraheemdev)
- [@sharkdp](https://github.com/sharkdp)
- [@thejchap](https://github.com/thejchap)
- [@carljm](https://github.com/carljm)
- [@jorenham](https://github.com/jorenham)
- [@AlexWaygood](https://github.com/AlexWaygood)
- [@dcreager](https://github.com/dcreager)
