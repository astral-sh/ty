# Changelog

## 0.0.1-alpha.28

Released on 2025-11-25.

### Bug fixes

- Fix panic for unclosed string literal in type annotation position ([#21592](https://github.com/astral-sh/ruff/pull/21592))
- Fix subtraction overflow bug ([#21570](https://github.com/astral-sh/ruff/pull/21570))

### LSP server

- Add "remove unused ignore comment" code action ([#21582](https://github.com/astral-sh/ruff/pull/21582))
- Add go-to-definition for `Unknown` when it appears in an inlay hint ([#21545](https://github.com/astral-sh/ruff/pull/21545))
- Add go-to-definition support for more types ([#21546](https://github.com/astral-sh/ruff/pull/21546))
- Add go-to-definition support  for typing special forms ([#21544](https://github.com/astral-sh/ruff/pull/21544))
- Don't suggest completions that aren't subclasses of `BaseException` after `raise` ([#21571](https://github.com/astral-sh/ruff/pull/21571))
- Implement double click to insert inlay hint ([#21600](https://github.com/astral-sh/ruff/pull/21600))
- Fix edge cases for autocomplete suppressions in variable bindings ([#21576](https://github.com/astral-sh/ruff/pull/21576))
- Implement docstring rendering to markdown ([#21550](https://github.com/astral-sh/ruff/pull/21550))
- Implement goto-definition and find-references for `global`/`nonlocal` statements ([#21616](https://github.com/astral-sh/ruff/pull/21616))
- Implement goto-type for inlay type hints ([#21533](https://github.com/astral-sh/ruff/pull/21533))
- Support string annotations ([#21577](https://github.com/astral-sh/ruff/pull/21577))
- Improve import detection for completions and support `from ...<CURSOR>` completions ([#21547](https://github.com/astral-sh/ruff/pull/21547))
- Improve handling of hover/goto on imports ([#21572](https://github.com/astral-sh/ruff/pull/21572))
- Don't allow edits of some more invalid syntax types in inlay hints ([#21621](https://github.com/astral-sh/ruff/pull/21621))
- Improve inlay hint goto-definition ([#21548](https://github.com/astral-sh/ruff/pull/21548))
- Resolve applicable overloads for hover on an overloaded function call ([#21417](https://github.com/astral-sh/ruff/pull/21417))
- Consistently add the `DEFINITION` modifier when computing semantic tokens ([#21521](https://github.com/astral-sh/ruff/pull/21521))
- Suppress autocomplete suggestions during variable binding ([#21549](https://github.com/astral-sh/ruff/pull/21549))

### CLI

- Exit with code `2` if there's any IO error ([#21508](https://github.com/astral-sh/ruff/pull/21508))

### Other changes

- Add hint about resolved Python version when a user attempts to import a member added on a newer version ([#21615](https://github.com/astral-sh/ruff/pull/21615))
- Attach subdiagnostics to `unresolved-import` errors for relative imports as well as absolute imports ([#21554](https://github.com/astral-sh/ruff/pull/21554))
- Avoid expression reinference for diagnostics ([#21267](https://github.com/astral-sh/ruff/pull/21267))
- Check method definitions on subclasses for Liskov violations ([#21436](https://github.com/astral-sh/ruff/pull/21436))
- Eagerly evaluate `types.UnionType` elements as type expressions ([#21531](https://github.com/astral-sh/ruff/pull/21531))
- Extend Liskov checks to also cover classmethods and staticmethods ([#21598](https://github.com/astral-sh/ruff/pull/21598))
- Fix rendering of unused suppression diagnostic ([#21580](https://github.com/astral-sh/ruff/pull/21580))
- Implement `typing.override` ([#21627](https://github.com/astral-sh/ruff/pull/21627))
- Improve concise diagnostics for invalid exceptions when a user catches a tuple of objects ([#21578](https://github.com/astral-sh/ruff/pull/21578))
- Improve debug messages when imports fail ([#21555](https://github.com/astral-sh/ruff/pull/21555))
- Improve diagnostics when `NotImplemented` is called ([#21523](https://github.com/astral-sh/ruff/pull/21523))
- Improve diagnostics when a submodule is not available as an attribute on a module-literal type ([#21561](https://github.com/astral-sh/ruff/pull/21561))
- Improve several "Did you mean?" suggestions ([#21597](https://github.com/astral-sh/ruff/pull/21597))
- Narrow type context during literal promotion in generic class constructors ([#21574](https://github.com/astral-sh/ruff/pull/21574))
- Retain the function-like-ness of `Callable` types when binding `self` ([#21614](https://github.com/astral-sh/ruff/pull/21614))
- Substitute for `typing.Self` when checking protocol members ([#21569](https://github.com/astral-sh/ruff/pull/21569))
- Switch the error code from `unresolved-attribute` to `possibly-missing-attribute` for submodules that may not be available ([#21618](https://github.com/astral-sh/ruff/pull/21618))
- Implement `TypedDict` structural assignment ([#21467](https://github.com/astral-sh/ruff/pull/21467))
- Make implicit submodule imports re-exported ([#21573](https://github.com/astral-sh/ruff/pull/21573))
- Support PEP 613 type aliases ([#21394](https://github.com/astral-sh/ruff/pull/21394))
- Support generic aliases in `type[...]`, like `type[C[int]]` ([#21552](https://github.com/astral-sh/ruff/pull/21552))
- Tighten up handling of subscripts in type expressions ([#21503](https://github.com/astral-sh/ruff/pull/21503))

### Contributors

- [@Gankra](https://github.com/Gankra)
- [@MatthewMckee4](https://github.com/MatthewMckee4)
- [@AlexWaygood](https://github.com/AlexWaygood)
- [@RasmusNygren](https://github.com/RasmusNygren)
- [@dcreager](https://github.com/dcreager)
- [@BurntSushi](https://github.com/BurntSushi)
- [@carljm](https://github.com/carljm)
- [@MichaReiser](https://github.com/MichaReiser)
- [@sharkdp](https://github.com/sharkdp)
- [@oconnor663](https://github.com/oconnor663)
- [@lucach](https://github.com/lucach)
- [@ibraheemdev](https://github.com/ibraheemdev)

## 0.0.1-alpha.27

Released on 2025-11-18.

### Bug fixes

- Fix panic for cyclic star imports ([#21428](https://github.com/astral-sh/ruff/pull/21428))
- Fix crashes when using a homebrew Python install ([#21405](https://github.com/astral-sh/ruff/pull/21405))
- Fix incorrect inference of `enum.auto()` for enums with non-`int` mixins, and imprecise inference of `enum.auto()` for single-member enums ([#20541](https://github.com/astral-sh/ruff/pull/20541))
- Fix global symbol lookup from eagerly executed scopes such as comprehensions and classes ([#21317](https://github.com/astral-sh/ruff/pull/21317))
- Fix false positive for instance attributes that are declared as `Final` in the class body but have their value assigned in the class's `__init__` method ([#21158](https://github.com/astral-sh/ruff/pull/21158))
- Use the return type of `__get__` for descriptor lookups even when `__get__` is called with incorrect arguments ([#21424](https://github.com/astral-sh/ruff/pull/21424))
- Consider parameters being declared `global` a syntax error ([#21312](https://github.com/astral-sh/ruff/pull/21312))

### Type inference

- Support `typing.NewType` ([#21157](https://github.com/astral-sh/ruff/pull/21157))
- Support `Callable` in implicit type aliases ([#21496](https://github.com/astral-sh/ruff/pull/21496))
- Support `typing.Union` in implicit type aliases ([#21363](https://github.com/astral-sh/ruff/pull/21363))
- Precise inference for generator expressions ([#21437](https://github.com/astral-sh/ruff/pull/21437))
- Support storing attributes in comprehension scopes ([#20856](https://github.com/astral-sh/ruff/pull/20856))
- Support `isinstance()` and `issubclass()` narrowing when the second argument is a `typing.py` stdlib alias ([#21391](https://github.com/astral-sh/ruff/pull/21391))
- Support `type[…]` and `Type[…]` in implicit type aliases ([#21421](https://github.com/astral-sh/ruff/pull/21421))
- Support attribute-expression `TYPE_CHECKING` conditionals ([#21449](https://github.com/astral-sh/ruff/pull/21449))
- Support class-arguments for dataclass transformers ([#21457](https://github.com/astral-sh/ruff/pull/21457))
- Support legacy `typing` special forms in implicit type aliases ([#21433](https://github.com/astral-sh/ruff/pull/21433))
- Support stringified annotations in value-position `Annotated` instances ([#21447](https://github.com/astral-sh/ruff/pull/21447))
- Support all parameters of dataclass transforms ([#21474](https://github.com/astral-sh/ruff/pull/21474))
- Support `__hash__` semantics and `unsafe_hash` for dataclasses ([#21470](https://github.com/astral-sh/ruff/pull/21470))
- Improve handling of version-specific features of dataclasses ([#21453](https://github.com/astral-sh/ruff/pull/21453))
- Correctly infer the specialization of a non-invariant PEP-695 generic class that has an annotated `self` parameter in its `__init__` method ([#21325](https://github.com/astral-sh/ruff/pull/21325))
- Improve use of type context when inferring the result of a generic constructor call ([#20933](https://github.com/astral-sh/ruff/pull/20933), [#21442](https://github.com/astral-sh/ruff/pull/21442))
- Improve use of type context when inferring the result of a generic call expression ([#21210](https://github.com/astral-sh/ruff/pull/21210))
- Improve heuristics used to decide when it is appropriate to "promote" a `Literal` type such as `Literal[42]` to its instance supertype (in this case, `int`) when solving type variables ([#21439](https://github.com/astral-sh/ruff/pull/21439))
- Improve use of type context to infer conditional expressions ([#21443](https://github.com/astral-sh/ruff/pull/21443))
- Make `__getattr__` available for `ModuleType` instances ([#21450](https://github.com/astral-sh/ruff/pull/21450))
- Introduce implicit local variables for `from` imports of submodules in `__init__.py(i)` ([#21173](https://github.com/astral-sh/ruff/pull/21173))
- Make implicit submodule locals only occur in global scope of an `__init__.py(i)` ([#21370](https://github.com/astral-sh/ruff/pull/21370))
- Make implicit submodule locals also occur for absolute `from` imports in `__init__.py(i)` files ([#21372](https://github.com/astral-sh/ruff/pull/21372))
- Consider `from thispackage import y` a re-export of `y` in `__init__.pyi` ([#21387](https://github.com/astral-sh/ruff/pull/21387))
- Allow PEP-604 unions in stubs and `TYPE_CHECKING` blocks prior to 3.10 ([#21379](https://github.com/astral-sh/ruff/pull/21379))
- Ensure annotation/type expressions in stub files are always deferred ([#21401](https://github.com/astral-sh/ruff/pull/21401), [#21456](https://github.com/astral-sh/ruff/pull/21456))
- Silence false-positive diagnostics when using `typing.Dict` or `typing.Callable` as the second argument to `isinstance()` ([#21386](https://github.com/astral-sh/ruff/pull/21386))
- Sync vendored typeshed stubs ([#21466](https://github.com/astral-sh/ruff/pull/21466)). [Typeshed diff](https://github.com/python/typeshed/compare/bf7214784877c52638844c065360d4814fae4c65...f8cdc0bd526301e873cd952eb0d457bdf2554e57)

### LSP server

- Support for notebooks in VS Code ([#21175](https://github.com/astral-sh/ruff/pull/21175))
- Fix goto-definition for `float` and `complex` in type annotation positions ([#21388](https://github.com/astral-sh/ruff/pull/21388))
- Support goto-definition on call argument inlay hints ([#20349](https://github.com/astral-sh/ruff/pull/20349))
- Add more keywords to scope-based completions ([#21383](https://github.com/astral-sh/ruff/pull/21383))
- Add synthetic members to completions on dataclasses ([#21446](https://github.com/astral-sh/ruff/pull/21446))
- Only suggest the `import` keyword in autocompletions for `from <name> <CURSOR>` statements ([#21291](https://github.com/astral-sh/ruff/pull/21291))
- Suppress completion suggestions following `as` tokens ([#21460](https://github.com/astral-sh/ruff/pull/21460))
- Suppress invalid suggestions in `import` statements ([#21484](https://github.com/astral-sh/ruff/pull/21484))
- Suppress redundant inlay hints for function args ([#21365](https://github.com/astral-sh/ruff/pull/21365))
- Suppress some trivial expression inlay hints ([#21367](https://github.com/astral-sh/ruff/pull/21367))
- Suppress inlay hints for `+1` and `-1` ([#21368](https://github.com/astral-sh/ruff/pull/21368))
- Improve [semantic token](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_semanticTokens) classification for names ([#21399](https://github.com/astral-sh/ruff/pull/21399))
- Classify parameter declarations as definitions when computing semantic tokens ([#21420](https://github.com/astral-sh/ruff/pull/21420))

### Diagnostics

- Better invalid-assignment diagnostics ([#21476](https://github.com/astral-sh/ruff/pull/21476))
- Better concise diagnostic messages ([#21498](https://github.com/astral-sh/ruff/pull/21498))
- Improve subscript assignment diagnostics ([#21411](https://github.com/astral-sh/ruff/pull/21411), [#21452](https://github.com/astral-sh/ruff/pull/21452))
- Improve diagnostic range for `non-subscriptable` diagnostics ([#21461](https://github.com/astral-sh/ruff/pull/21461))
- Improve diagnostics for invalid exceptions ([#21475](https://github.com/astral-sh/ruff/pull/21475))
- Add hyperlinks to rule codes in CLI ([#21502](https://github.com/astral-sh/ruff/pull/21502))

### Performance improvements

- Cache computation of dataclass/NamedTuple/TypedDict fields ([#21512](https://github.com/astral-sh/ruff/pull/21512))
- Faster subscript assignment checks for (unions of) `TypedDict`s ([#21378](https://github.com/astral-sh/ruff/pull/21378))
- Reduce memory allocations for string-literal types ([#21497](https://github.com/astral-sh/ruff/pull/21497))

### Contributors

- [@thejchap](https://github.com/thejchap)
- [@mtshiba](https://github.com/mtshiba)
- [@ibraheemdev](https://github.com/ibraheemdev)
- [@Gankra](https://github.com/Gankra)
- [@charliecloudberry](https://github.com/charliecloudberry)
- [@lucach](https://github.com/lucach)
- [@AlexWaygood](https://github.com/AlexWaygood)
- [@MichaReiser](https://github.com/MichaReiser)
- [@Glyphack](https://github.com/Glyphack)
- [@dcreager](https://github.com/dcreager)
- [@saada](https://github.com/saada)
- [@11happy](https://github.com/11happy)
- [@oconnor663](https://github.com/oconnor663)
- [@MatthewMckee4](https://github.com/MatthewMckee4)
- [@BurntSushi](https://github.com/BurntSushi)
- [@RasmusNygren](https://github.com/RasmusNygren)
- [@sharkdp](https://github.com/sharkdp)

## 0.0.1-alpha.26

Released on 2025-11-10.

### Bug fixes

- Language server: For [semantic tokens](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_semanticTokens), fix range filtering for tokens starting at the end of the requested range ([#21193](https://github.com/astral-sh/ruff/pull/21193))
- Fix panic due to simplifying `Divergent` types out of intersections types ([#21253](https://github.com/astral-sh/ruff/pull/21253))
- Fix merging of `--exclude` CLI flag and `src.exclude` config-file setting ([#21341](https://github.com/astral-sh/ruff/pull/21341))

### Type inference

- Infer type of `self` for decorated methods and properties ([#21123](https://github.com/astral-sh/ruff/pull/21123))
- Add support for properties that return `Self` ([#21335](https://github.com/astral-sh/ruff/pull/21335))
- Understand legacy and PEP 695 `ParamSpec` ([#21139](https://github.com/astral-sh/ruff/pull/21139))
- Type inference for comprehensions ([#20962](https://github.com/astral-sh/ruff/pull/20962))
- Reachability and narrowing for enum methods ([#21130](https://github.com/astral-sh/ruff/pull/21130))
- Implicit type aliases: Support for PEP 604 unions, `Literal`s, `Optional`, and `Annotated` ([#21195](https://github.com/astral-sh/ruff/pull/21195), [#21296](https://github.com/astral-sh/ruff/pull/21296), [#21321](https://github.com/astral-sh/ruff/pull/21321))
- `dict` is not assignable to `TypedDict` ([#21238](https://github.com/astral-sh/ruff/pull/21238))
- Allow values of type `None` in type expressions ([#21263](https://github.com/astral-sh/ruff/pull/21263))
- Add narrowing for `isinstance()` and `issubclass()` checks that use PEP-604 unions ([#21334](https://github.com/astral-sh/ruff/pull/21334))
- Do not promote `Literal` types when solving type variables in contravariant positions ([#21164](https://github.com/astral-sh/ruff/pull/21164), <https://github.com/astral-sh/ruff/pull/21171>))
- Fix lookup of `__new__` methods on instances ([#21147](https://github.com/astral-sh/ruff/pull/21147))
- Fix narrowing of generic classes in class patterns for `match` statements ([#21150](https://github.com/astral-sh/ruff/pull/21150))
- Improve understanding of disjointness for `@final` classes ([#21167](https://github.com/astral-sh/ruff/pull/21167))
- Fix the inferred signature of the synthesized `__init__` method of a non-dataclass inheriting from a generic dataclass ([#21159](https://github.com/astral-sh/ruff/pull/21159))
- Improve exhaustiveness analysis for type variables with bounds or constraints ([#21172](https://github.com/astral-sh/ruff/pull/21172))
- Prefer exact matches when solving constrained type variables ([#21165](https://github.com/astral-sh/ruff/pull/21165))
- Simplify unions containing multiple type variables during inference ([#21275](https://github.com/astral-sh/ruff/pull/21275))
- Use the declared attribute type when inferring union attribute assignments ([#21170](https://github.com/astral-sh/ruff/pull/21170))
- Sync vendored typeshed stubs ([#21178](https://github.com/astral-sh/ruff/pull/21178)). [Typeshed diff](https://github.com/python/typeshed/compare/d6f4a0f7102b1400a21742cf9b7ea93614e2b6ec...bf7214784877c52638844c065360d4814fae4c65)
- Use declared attribute types as type context when solving type variables ([#21143](https://github.com/astral-sh/ruff/pull/21143))
- Don't union in the inferred type of a parameter's default value when inferring the type of an annotated parameter ([#21208](https://github.com/astral-sh/ruff/pull/21208))
- Support subscripting typing.Literal with a type alias ([#21207](https://github.com/astral-sh/ruff/pull/21207))

### LSP server

- Don't provide completions when in a class or function definition ([#21146](https://github.com/astral-sh/ruff/pull/21146))
- Favor symbols defined in the current file over imported symbols ([#21194](https://github.com/astral-sh/ruff/pull/21194)) and builtin symbols ([#21285](https://github.com/astral-sh/ruff/pull/21285))

### Diagnostics

- Add diagnostics for `isinstance()` and `issubclass()` calls that use invalid PEP-604 unions for their second argument ([#21343](https://github.com/astral-sh/ruff/pull/21343))
- Don't assume in diagnostic messages that a `TypedDict` key error is about subscript access ([#21166](https://github.com/astral-sh/ruff/pull/21166))

### Other changes

- Consistently wrap tokens in parser diagnostics in `backticks` instead of 'quotes' ([#21163](https://github.com/astral-sh/ruff/pull/21163))
- Discover the `site-packages` directory from the environment that ty is installed in ([#21286](https://github.com/astral-sh/ruff/pull/21286)), improving the ergonomics of `uvx ty check`
- Support implicit imports of submodules in `__init__.pyi` ([#20855](https://github.com/astral-sh/ruff/pull/20855))
- Use "cannot" consistently over "can not" in diagnostics ([#21255](https://github.com/astral-sh/ruff/pull/21255))
- Resolve `from foo import bar` to the `foo.bar` submodule rather than using the `__getattr__` function in `foo/__init__.py` (in situations where they both exist)([#21260](https://github.com/astral-sh/ruff/pull/21260))

### Contributors

- [@MatthewMckee4](https://github.com/MatthewMckee4)
- [@dhruvmanila](https://github.com/dhruvmanila)
- [@sharkdp](https://github.com/sharkdp)
- [@Gankra](https://github.com/Gankra)
- [@saada](https://github.com/saada)
- [@zanieb](https://github.com/zanieb)
- [@MichaReiser](https://github.com/MichaReiser)
- [@ibraheemdev](https://github.com/ibraheemdev)
- [@AlexWaygood](https://github.com/AlexWaygood)
- [@lucach](https://github.com/lucach)
- [@mtshiba](https://github.com/mtshiba)
- [@carljm](https://github.com/carljm)

## 0.0.1-alpha.25

Released on 2025-10-29.

### Bug fixes

- Fix bug where ty would think all types had an `__mro__` attribute ([#20995](https://github.com/astral-sh/ruff/pull/20995))
- Fix rare panic with highly cyclic `TypeVar` definitions ([#21059](https://github.com/astral-sh/ruff/pull/21059))
- Fix infinite recursion with generic type aliases ([#20969](https://github.com/astral-sh/ruff/pull/20969))
- Add missing newline before first diagnostic in CLI output ([#21058](https://github.com/astral-sh/ruff/pull/21058))
- Make the ty server's auto-import feature skip symbols in the current module ([#21100](https://github.com/astral-sh/ruff/pull/21100))
- Don't provide goto-definition for definitions which are not reexported in builtins ([#21127](https://github.com/astral-sh/ruff/pull/21127))
- Avoid duplicate diagnostics during multi-inference of standalone expressions ([#21056](https://github.com/astral-sh/ruff/pull/21056))

### Type inference and diagnostics

- Use constructor parameter types as context to inform solving type variables ([#21054](https://github.com/astral-sh/ruff/pull/21054))
- Consider `__len__` when determining the truthiness of an instance of a tuple class or a `@final` class ([#21049](https://github.com/astral-sh/ruff/pull/21049))
- Delegate truthiness inference of an enum `Literal` type to its enum-instance supertype ([#21060](https://github.com/astral-sh/ruff/pull/21060))
- Improve `invalid-argument-type` diagnostics where a union type was provided ([#21044](https://github.com/astral-sh/ruff/pull/21044))

### LSP server

- Suggest `type_check_only` items last in completions ([#20910](https://github.com/astral-sh/ruff/pull/20910))
- Render `import <...>` in completions when "label details" isn't supported ([#21109](https://github.com/astral-sh/ruff/pull/21109))
- Update workspace diagnostic progress every 50ms ([#21019](https://github.com/astral-sh/ruff/pull/21019))

### CLI

- Add `--no-progress` option to suppress the rendering of a progress bar ([#21063](https://github.com/astral-sh/ruff/pull/21063))

### Contributors

- [@ibraheemdev](https://github.com/ibraheemdev)
- [@MatthewMckee4](https://github.com/MatthewMckee4)
- [@BurntSushi](https://github.com/BurntSushi)
- [@mtshiba](https://github.com/mtshiba)
- [@AlexWaygood](https://github.com/AlexWaygood)
- [@MichaReiser](https://github.com/MichaReiser)
- [@decorator-factory](https://github.com/decorator-factory)

## 0.0.1-alpha.24

Released on 2025-10-23.

### Breaking changes

- Rename `unknown-rule` lint to `ignore-comment-unknown-rule` ([#20948](https://github.com/astral-sh/ruff/pull/20948))

### Type inference and diagnostics

- Infer a type of `Self` for unannotated `self` parameters in methods ([#20922](https://github.com/astral-sh/ruff/pull/20922))
- Prefer the declared type over the inferred type for invariant collection literals ([#20927](https://github.com/astral-sh/ruff/pull/20927))
- Use declared variable types as bidirectional type context for solving type variables ([#20796](https://github.com/astral-sh/ruff/pull/20796))
- Support `dataclass_transform` for base class models ([#20783](https://github.com/astral-sh/ruff/pull/20783))
- Support dataclass-transform `field_specifiers` ([#20888](https://github.com/astral-sh/ruff/pull/20888))
- `dataclass_transform` support for fields with an `alias` ([#20961](https://github.com/astral-sh/ruff/pull/20961))
- Add support for legacy namespace packages ([#20897](https://github.com/astral-sh/ruff/pull/20897))
- Add suggestion to "unknown rule" diagnostics ([#20948](https://github.com/astral-sh/ruff/pull/20948))
- Improve error messages for "unresolved attribute" diagnostics ([#20963](https://github.com/astral-sh/ruff/pull/20963))
- Avoid unnecessarily widening generic specializations ([#20875](https://github.com/astral-sh/ruff/pull/20875))
- Truncate `Literal` type display in some situations ([#20928](https://github.com/astral-sh/ruff/pull/20928))

### Bug fixes

- Fix panic involving cyclic `TypeVar` default ([#20967](https://github.com/astral-sh/ruff/pull/20967))
- Fix panic involving ever-growing default types ([#20991](https://github.com/astral-sh/ruff/pull/20991))
- Fix panic involving infinitely expanding implicit attribute types ([#20988](https://github.com/astral-sh/ruff/pull/20988))
- Fix autocomplete suggestions when the cursor is at the end of a file ([#20993](https://github.com/astral-sh/ruff/pull/20993))
- Fix inconsistent highlighting of self ([#20986](https://github.com/astral-sh/ruff/pull/20986))
- Fix out-of-order semantic token for function with regular argument after kwargs ([#21013](https://github.com/astral-sh/ruff/pull/21013))
- Fix panic on recursive class definitions in a stub that use constrained type variables ([#20955](https://github.com/astral-sh/ruff/pull/20955))
- Fix panic when attempting to validate the members of a protocol that inherits from a protocol in another module ([#20956](https://github.com/astral-sh/ruff/pull/20956))
- Fix rare hang relating to multithreading ([#21038](https://github.com/astral-sh/ruff/pull/21038))
- Fix non-deterministic overload function inference ([#20966](https://github.com/astral-sh/ruff/pull/20966))
- Fix auto-import edits made by autocompletions for files with an existing `from __future__` import ([#20987](https://github.com/astral-sh/ruff/pull/20987))

### LSP server

- Support goto-definition for binary and unary operators ([#21001](https://github.com/astral-sh/ruff/pull/21001))
- Support goto-definition on vendored typeshed stubs ([#21020](https://github.com/astral-sh/ruff/pull/21020))
- Provide completions on `TypeVar`s ([#20943](https://github.com/astral-sh/ruff/pull/20943))
- Display variance when hovering over type variables ([#20900](https://github.com/astral-sh/ruff/pull/20900))
- Avoid sending an unnecessary "clear diagnostics" message for clients supporting [pull diagnostics](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_pullDiagnostics). ([#20989](https://github.com/astral-sh/ruff/pull/20989))

### Other changes

- Report `continue` and `break` statements outside loops as syntax errors ([#20944](https://github.com/astral-sh/ruff/pull/20944))

### Contributors

- [@TaKO8Ki](https://github.com/TaKO8Ki)
- [@sharkdp](https://github.com/sharkdp)
- [@InvalidPathException](https://github.com/InvalidPathException)
- [@AlexWaygood](https://github.com/AlexWaygood)
- [@mtshiba](https://github.com/mtshiba)
- [@ibraheemdev](https://github.com/ibraheemdev)
- [@Gankra](https://github.com/Gankra)
- [@MichaReiser](https://github.com/MichaReiser)

## 0.0.1-alpha.23

Released on 2025-10-16.

### Bug fixes

- Fix handling of dataclass `field()`s without default values ([#20914](https://github.com/astral-sh/ruff/pull/20914))
- Fix false-positive diagnostics on `super()` calls ([#20814](https://github.com/astral-sh/ruff/pull/20814), [#20843](https://github.com/astral-sh/ruff/pull/20843))
- Fix `match` pattern value narrowing to use equality semantics ([#20882](https://github.com/astral-sh/ruff/pull/20882))
- Fix "missing root" panic when handling completion requests ([#20917](https://github.com/astral-sh/ruff/pull/20917))
- Fix overwriting of declared base class attributes through undeclared subclass members ([#20764](https://github.com/astral-sh/ruff/pull/20764))
- Fix runaway execution time for mutually referential instance attributes ([#20645](https://github.com/astral-sh/ruff/pull/20645))

### CLI

- For `unresolved-import` diagnostics, limit the shown import paths to at most five, unless in verbose mode ([#20912](https://github.com/astral-sh/ruff/pull/20912))
- Write files that are slow to type check to log output ([#20836](https://github.com/astral-sh/ruff/pull/20836))
- Remove "pre-release software" warning ([#20817](https://github.com/astral-sh/ruff/pull/20817))

### LSP server

- Improve ranking of autocomplete suggestions ([#20807](https://github.com/astral-sh/ruff/pull/20807))

### Type inference and diagnostics

- Use return type annotations as context for bidirectional type inference ([#20528](https://github.com/astral-sh/ruff/pull/20528))
- Use bidirectional type context for `TypedDict` construction ([#20806](https://github.com/astral-sh/ruff/pull/20806))
- Add support for unpacking of heterogeneous tuples in unions ([#20377](https://github.com/astral-sh/ruff/pull/20377))
- Add a new diagnostic for generic classes that reference typevars from an enclosing scope ([#20822](https://github.com/astral-sh/ruff/pull/20822))
- Add hint when accessing standard library module attributes that are not available on the configured Python version ([#20909](https://github.com/astral-sh/ruff/pull/20909))
- Treat functions, methods, and dynamic types as function-like `Callable`s ([#20842](https://github.com/astral-sh/ruff/pull/20842))
- Treat `Callable`s as bound-method descriptors in special cases ([#20802](https://github.com/astral-sh/ruff/pull/20802))
- Treat `Callable` dunder members as bound method descriptors ([#20860](https://github.com/astral-sh/ruff/pull/20860))
- Sync vendored typeshed stubs ([#20876](https://github.com/astral-sh/ruff/pull/20876)). [Typeshed diff](https://github.com/python/typeshed/compare/91055c730ffcda6311654cf32d663858ece69bad...d6f4a0f7102b1400a21742cf9b7ea93614e2b6ec)

### Performance improvements

- Improve performance by caching union simplification type relations ([#20477](https://github.com/astral-sh/ruff/pull/20477))

### Contributors

- [@mtshiba](https://github.com/mtshiba)
- [@AlexWaygood](https://github.com/AlexWaygood)
- [@ericmarkmartin](https://github.com/ericmarkmartin)
- [@carljm](https://github.com/carljm)
- [@ntBre](https://github.com/ntBre)
- [@sharkdp](https://github.com/sharkdp)
- [@BurntSushi](https://github.com/BurntSushi)
- [@Gankra](https://github.com/Gankra)
- [@MichaReiser](https://github.com/MichaReiser)
- [@dcreager](https://github.com/dcreager)

## 0.0.1-alpha.22

Released on 2025-10-10.

### Bug fixes

- Enforce that `typing_extensions` must come from a stdlib search path. This fixes a panic that could occur with a confusing backtrace if the `extra-paths` setting was incorrectly used to point to a virtual environment ([#20715](https://github.com/astral-sh/ruff/pull/20715))
- Fix server panic when opening a project located at `/` in the file system ([#20684](https://github.com/astral-sh/ruff/pull/20684))
- Fix panics when using `--output-format=gitlab` in CI environments ([#20550](https://github.com/astral-sh/ruff/pull/20550))
- Fix stack overflows that could occur when attempting to determine if a recursive `NamedTuple` type was disjoint from another type ([#20538](https://github.com/astral-sh/ruff/pull/20538))
- Fix panics in type inference when legacy TypeVars had bounds, constraints, or defaults that cyclically referred back to the TypeVar definition (directly or indirectly) ([#20598](https://github.com/astral-sh/ruff/pull/20598))
- Fix situations where a panic during resolution of type-checker query cycles would manifest in a hang ([#20577](https://github.com/astral-sh/ruff/pull/20577))
- When analyzing a .py file, do not error if there's also a .pyi for that module ([#20461](https://github.com/astral-sh/ruff/pull/20461))
- Recognise that the runtime object `typing.Protocol` is an instance of `_ProtocolMeta` ([#20488](https://github.com/astral-sh/ruff/pull/20488))
- Fix logic that attempted to determine whether a user had explicitly activated a Conda environment, which has implications for the search paths ty uses for module resolution ([#20675](https://github.com/astral-sh/ruff/pull/20675))
- Fix false negatives when iterables with the wrong type are unpacked into a function with a `*args` variadic parameter ([#20511](https://github.com/astral-sh/ruff/pull/20511))

### Support for Python 3.14

- Use 3.14 as the default version ([#20725](https://github.com/astral-sh/ruff/pull/20725), [#20759](https://github.com/astral-sh/ruff/pull/20759), [#20760](https://github.com/astral-sh/ruff/pull/20760))
- Annotations are deferred by default for 3.14+ ([#20799](https://github.com/astral-sh/ruff/pull/20799))
- Fix false positives when accessing `__annotate__` (Py3.14+) or `__warningregistry__` as a module global ([#20154](https://github.com/astral-sh/ruff/pull/20154))

### Improvements to `TypeVar` solving and inference of generic types

- Improve solving of a type variable `T` if it appears in a union with non-`TypeVar`s (`T | None`, `T | str | None`, etc.) ([#20749](https://github.com/astral-sh/ruff/pull/20749))
- More precise type inference for dictionary literals ([#20523](https://github.com/astral-sh/ruff/pull/20523))
- When solving type variables, use type context to inform whether `Literal` types should be promoted to instance types ([#20776](https://github.com/astral-sh/ruff/pull/20776))
- Use annotated parameters as type context when solving type variables ([#20635](https://github.com/astral-sh/ruff/pull/20635))
- Correctly infer the return type of method calls when the method is annotated as returning `Self` ([#20517](https://github.com/astral-sh/ruff/pull/20517), [#20754](https://github.com/astral-sh/ruff/pull/20754))
- Use type context for inference of generic function calls ([#20476](https://github.com/astral-sh/ruff/pull/20476))
- Use `C[T]` instead of `C[Unknown]` for the upper bound of `Self` ([#20479](https://github.com/astral-sh/ruff/pull/20479))

### Improvements to assignability, subtyping, and union simplification

- Fix overly strict assignability implementation for intersections with negated gradual elements ([#20773](https://github.com/astral-sh/ruff/pull/20773))
- Ensure that `C[Any]` is understood as a subtype of `C[object]` if `C` is a covariant generic class ([#20592](https://github.com/astral-sh/ruff/pull/20592))
- Ensure that `~T` is never considered to be assignable to `T` where `T` is a type variable ([#20606](https://github.com/astral-sh/ruff/pull/20606))
- Improve assignability/subtyping between two protocol types ([#20368](https://github.com/astral-sh/ruff/pull/20368))
- Simplify `Any | (Any & T)` to `Any` ([#20593](https://github.com/astral-sh/ruff/pull/20593))
- Optimise and generalise union/intersection simplification ([#20602](https://github.com/astral-sh/ruff/pull/20602))
- Make protocol satisfiability checks more principled when a protocol has a method member that is generic over type variables scoped to the function ([#20568](https://github.com/astral-sh/ruff/pull/20568))
- Fix subtyping of invariant generics specialized with `Any`, ensuring that (for example) `list[Any]` is not considered a subtype of `list[Any]` ([#20650](https://github.com/astral-sh/ruff/pull/20650))

### Server

- Add LSP debug information command ([#20379](https://github.com/astral-sh/ruff/pull/20379))
- Add support for inlay hints on attribute assignment ([#20485](https://github.com/astral-sh/ruff/pull/20485))

### Improvements to diagnostics

- Improve diagnostics when a positional-only parameter is passed using a keyword argument ([#20495](https://github.com/astral-sh/ruff/pull/20495))
- Improve disambiguations of class names in diagnostics ([#20603](https://github.com/astral-sh/ruff/pull/20603), [#20756](https://github.com/astral-sh/ruff/pull/20756))
- Improve diagnostics for bad `@overload` definitions ([#20745](https://github.com/astral-sh/ruff/pull/20745))
- Truncate type display for long unions in some situations ([#20730](https://github.com/astral-sh/ruff/pull/20730))
- Rename "possibly unbound" diagnostics to "possibly missing" ([#20492](https://github.com/astral-sh/ruff/pull/20492))

### Improvements to enum support

- Allow multiple aliases to point to the same member ([#20669](https://github.com/astral-sh/ruff/pull/20669))
- implement `auto()` for `StrEnum` ([#20524](https://github.com/astral-sh/ruff/pull/20524))

### Improvements to ty's `@overload` implementation

- Support single-starred argument for overload call ([#20223](https://github.com/astral-sh/ruff/pull/20223))
- Filter overloads using variadic parameters ([#20547](https://github.com/astral-sh/ruff/pull/20547))

### Other typing semantics and features

- Do not union the inferred type of a module-global symbol with `Unknown` for the symbol's type when accessed from external scopes ([#20664](https://github.com/astral-sh/ruff/pull/20664))
- Ensure that class objects are understood as callable even if they do not override `object.__new__` or `object.__init__` ([#20521](https://github.com/astral-sh/ruff/pull/20521))
- Add support for `**kwargs` ([#20430](https://github.com/astral-sh/ruff/pull/20430))
- Ensure first-party module-resolution search paths always appear in a sensible order ([#20629](https://github.com/astral-sh/ruff/pull/20629))
- Respect `dataclass_transform` parameters for metaclass-based models ([#20780](https://github.com/astral-sh/ruff/pull/20780))
- Sync vendored typeshed stubs ([#20658](https://github.com/astral-sh/ruff/pull/20658)). [Typeshed diff](https://github.com/python/typeshed/compare/47dbbd6c914a5190d54bc5bd498d1e6633d97db2...91055c730ffcda6311654cf32d663858ece69bad)
- Bring ty's `TypeIs` narrowing behaviour closer to ty's narrowing behaviour for `isinstance()` checks. ([#20591](https://github.com/astral-sh/ruff/pull/20591))
- `dataclass_transform`: Support `frozen_default` and `kw_only_default` ([#20761](https://github.com/astral-sh/ruff/pull/20761))
- Allow any string `Literal` type expression as a key when constructing a `TypedDict` ([#20792](https://github.com/astral-sh/ruff/pull/20792))
- Add `--venv` as an alias to `--python` on the command line ([#20718](https://github.com/astral-sh/ruff/pull/20718))
- Add search paths listed in `PYTHONPATH` to search paths used for ty's module resolution ([#20441](https://github.com/astral-sh/ruff/pull/20441), [#20490](https://github.com/astral-sh/ruff/pull/20490))

### Contributors

- [@thejchap](https://github.com/thejchap)
- [@mtshiba](https://github.com/mtshiba)
- [@Danielkonge](https://github.com/Danielkonge)
- [@dcreager](https://github.com/dcreager)
- [@MatthewMckee4](https://github.com/MatthewMckee4)
- [@Gankra](https://github.com/Gankra)
- [@BurntSushi](https://github.com/BurntSushi)
- [@carljm](https://github.com/carljm)
- [@dhruvmanila](https://github.com/dhruvmanila)
- [@sharkdp](https://github.com/sharkdp)
- [@mmlb](https://github.com/mmlb)
- [@fgiacome](https://github.com/fgiacome)
- [@Guillaume-Fgt](https://github.com/Guillaume-Fgt)
- [@AlexWaygood](https://github.com/AlexWaygood)
- [@Renkai](https://github.com/Renkai)
- [@InvalidPathException](https://github.com/InvalidPathException)
- [@ibraheemdev](https://github.com/ibraheemdev)
- [@fatelei](https://github.com/fatelei)
- [@github-actions](https://github.com/github-actions)
- [@MichaReiser](https://github.com/MichaReiser)
- [@ntBre](https://github.com/ntBre)
- [@danparizher](https://github.com/danparizher)

## 0.0.1-alpha.21

### Bug fixes

- Fix inference of constructor calls to generic classes that have explicitly annotated `self` parameters in their `__init__` methods ([#20325](https://github.com/astral-sh/ruff/pull/20325))
- Fix a stack overflow when computing completions for recursive types ([#20354](https://github.com/astral-sh/ruff/pull/20354))
- Fix panic in `BoundMethodType::into_callable_type()` ([#20369](https://github.com/astral-sh/ruff/pull/20369))
- Fix stack overflows in binary comparison inference ([#20446](https://github.com/astral-sh/ruff/pull/20446))
- Fix many "too many cycle iterations" panics concerning recursive type aliases and/or recursive generics ([#20359](https://github.com/astral-sh/ruff/pull/20359))
- Fix stack overflow involving subtype checks for recursive type aliases ([#20259](https://github.com/astral-sh/ruff/pull/20259))
- Fix panic when inferring the type of an infinitely-nested-tuple implicit instance attribute ([#20333](https://github.com/astral-sh/ruff/pull/20333))

### Server

- Add autocomplete suggestions for unimported symbols ([#20207](https://github.com/astral-sh/ruff/pull/20207), [#20439](https://github.com/astral-sh/ruff/pull/20439))
- Include generated `NamedTuple` methods such as `_make`, `_asdict` and `_replace` in autocomplete suggestions ([#20356](https://github.com/astral-sh/ruff/pull/20356))

### Configuration

- Automatically add `python/` to `environment.root` if a `python/` folder exists in the root of a repository ([#20263](https://github.com/astral-sh/ruff/pull/20263))

### CLI

- Add GitHub output format ([#20358](https://github.com/astral-sh/ruff/pull/20358))
- Add GitLab output format ([#20155](https://github.com/astral-sh/ruff/pull/20155))

### Typing semantics and features

- Add support for generic [PEP-695 type aliases](https://peps.python.org/pep-0695/#generic-type-alias) ([#20219](https://github.com/astral-sh/ruff/pull/20219))
- Allow annotation expressions to be `ast::Attribute` nodes ([#20413](https://github.com/astral-sh/ruff/pull/20413))
- Allow protocols to participate in nominal subtyping as well as structural subtyping ([#20314](https://github.com/astral-sh/ruff/pull/20314))
- Attribute access on top/bottom materializations ([#20221](https://github.com/astral-sh/ruff/pull/20221))
- Bind `Self` type variables to the method, not the class ([#20366](https://github.com/astral-sh/ruff/pull/20366))
- Ensure various special-cased bound methods are understood as assignable to `Callable` ([#20330](https://github.com/astral-sh/ruff/pull/20330))
- Ensure various special-cased builtin functions are understood as assignable to `Callable` ([#20331](https://github.com/astral-sh/ruff/pull/20331))
- Fall back to `object` for attribute access on synthesized protocols ([#20286](https://github.com/astral-sh/ruff/pull/20286))
- Fix signature of `NamedTupleLike._make` ([#20302](https://github.com/astral-sh/ruff/pull/20302))
- Fix subtyping/assignability of function- and class-literal types to callback protocols ([#20363](https://github.com/astral-sh/ruff/pull/20363))
- Implement the legacy PEP-484 convention for indicating positional-only parameters ([#20248](https://github.com/astral-sh/ruff/pull/20248))
- Infer more precise types for collection literals ([#20360](https://github.com/astral-sh/ruff/pull/20360))
- Make `TypeIs` invariant in its type argument ([#20428](https://github.com/astral-sh/ruff/pull/20428))
- Narrow specialized generics using `isinstance()` ([#20256](https://github.com/astral-sh/ruff/pull/20256))
- Proper assignability/subtyping checks for protocols with method members ([#20165](https://github.com/astral-sh/ruff/pull/20165))
- Reduce false positives for `ParamSpec`s and `TypeVarTuple`s ([#20239](https://github.com/astral-sh/ruff/pull/20239))
- Overload evaluation: retry parameter matching for argument type expansion ([#20153](https://github.com/astral-sh/ruff/pull/20153))
- Simplify unions of enum literals and subtypes thereof ([#20324](https://github.com/astral-sh/ruff/pull/20324))
- Support "legacy" `typing.Self` in combination with [PEP-695](https://peps.python.org/pep-0695) generic contexts ([#20304](https://github.com/astral-sh/ruff/pull/20304))
- Treat `Hashable`, and similar protocols, equivalently to `object` for subtyping/assignability ([#20284](https://github.com/astral-sh/ruff/pull/20284))
- Treat `__new__` as a static method ([#20212](https://github.com/astral-sh/ruff/pull/20212))
- `TypedDict`: Add support for `typing.ReadOnly` ([#20241](https://github.com/astral-sh/ruff/pull/20241))
- Detect syntax errors stemming from `yield from` expressions inside async functions ([#20051](https://github.com/astral-sh/ruff/pull/20051))
- `"foo".startswith` is not an instance of `types.MethodWrapperType` ([#20317](https://github.com/astral-sh/ruff/pull/20317))
- Eliminate definitely-impossible types from union in equality narrowing ([#20164](https://github.com/astral-sh/ruff/pull/20164))
- Infer more precise types for the `name` and `value` properties on enum members ([#20311](https://github.com/astral-sh/ruff/pull/20311))
- Initial support for `slots=True` in dataclasses ([#20278](https://github.com/astral-sh/ruff/pull/20278))
- Improve type narrowing in situations involving nested functions ([#19932](https://github.com/astral-sh/ruff/pull/19932))
- Support type aliases in binary comparison inference ([#20445](https://github.com/astral-sh/ruff/pull/20445))
- Sync vendored typeshed stubs ([#20394](https://github.com/astral-sh/ruff/pull/20394)). [Typeshed diff](https://github.com/python/typeshed/compare/2480d7e7c74493a024eaf254c5d2c6f452c80ee2...47dbbd6c914a5190d54bc5bd498d1e6633d97db2)

### Diagnostics

- Improve specialization-error diagnostics ([#20326](https://github.com/astral-sh/ruff/pull/20326))

### Contributors

- [@thejchap](https://github.com/thejchap)
- [@AlexWaygood](https://github.com/AlexWaygood)
- [@mtshiba](https://github.com/mtshiba)
- [@JelleZijlstra](https://github.com/JelleZijlstra)
- [@ibraheemdev](https://github.com/ibraheemdev)
- [@TaKO8Ki](https://github.com/TaKO8Ki)
- [@Glyphack](https://github.com/Glyphack)
- [@ericmarkmartin](https://github.com/ericmarkmartin)
- [@Renkai](https://github.com/Renkai)
- [@sharkdp](https://github.com/sharkdp)
- [@11happy](https://github.com/11happy)
- [@BurntSushi](https://github.com/BurntSushi)
- [@carljm](https://github.com/carljm)
- [@dhruvmanila](https://github.com/dhruvmanila)
- [@github-actions](https://github.com/github-actions)
- [@ntBre](https://github.com/ntBre)

## 0.0.1-alpha.20

### Bug fixes

- Server: Cancel background tasks when shutdown is requested ([#20039](https://github.com/astral-sh/ruff/pull/20039))
- Server: Close signature help after `)` ([#20017](https://github.com/astral-sh/ruff/pull/20017))
- Server: Fix incorrect docstring in call signature completion ([#20021](https://github.com/astral-sh/ruff/pull/20021))
- Fix 'too many cycle iterations' for unions of literals ([#20137](https://github.com/astral-sh/ruff/pull/20137))
- Fix namespace packages that behave like partial stubs ([#19994](https://github.com/astral-sh/ruff/pull/19994))
- Fix server hang (unchanged diagnostics) when changing file on Windows ([#19991](https://github.com/astral-sh/ruff/pull/19991))
- Apply `KW_ONLY` sentinel only to local fields ([#19986](https://github.com/astral-sh/ruff/pull/19986))
- Ignore field specifiers when not specified in `@dataclass_transform` ([#20002](https://github.com/astral-sh/ruff/pull/20002))

### Server

- Add completion support for `import` and `from ... import` statements ([#19883](https://github.com/astral-sh/ruff/pull/19883))
- Add type as detail to completion items ([#20047](https://github.com/astral-sh/ruff/pull/20047))
- Ask the LSP client to watch all project search paths ([#19975](https://github.com/astral-sh/ruff/pull/19975))
- Fix incorrect inlay hint type ([#20044](https://github.com/astral-sh/ruff/pull/20044))
- Update goto definition, goto declaration and hover to consider constructor method (`__init__`) ([#20014](https://github.com/astral-sh/ruff/pull/20014))
- Add docstrings to completions based on type ([#20008](https://github.com/astral-sh/ruff/pull/20008))
- Fix goto targets for keyword arguments in nested function calls ([#20013](https://github.com/astral-sh/ruff/pull/20013))
- Introduce multiline pretty printer to render function signatures across multiple lines ([#19979](https://github.com/astral-sh/ruff/pull/19979))

### Configuration

- Distinguish base conda from child conda ([#19990](https://github.com/astral-sh/ruff/pull/19990))

### Typing semantics and features

- Add support for PEP 750: t-strings ([#20085](https://github.com/astral-sh/ruff/pull/20085))
- Add support for PEP 800: Disjoint bases ([#20084](https://github.com/astral-sh/ruff/pull/20084))
- Add precise inference for unpacking a TypeVar if the TypeVar has an upper bound with a precise tuple spec ([#19985](https://github.com/astral-sh/ruff/pull/19985))
- Add precise iteration and unpacking inference for string literals and bytes literals ([#20023](https://github.com/astral-sh/ruff/pull/20023))
- Completely ignore typeshed's stub for `Any` ([#20079](https://github.com/astral-sh/ruff/pull/20079))
- Enforce that an attribute on a class `X` must be callable in order to satisfy a member on a protocol `P` ([#20142](https://github.com/astral-sh/ruff/pull/20142))
- Evaluate static truthiness of non-definitely-bound symbols to "ambiguous" ([#19579](https://github.com/astral-sh/ruff/pull/19579))
- Fix the inferred interface of specialized generic protocols ([#19866](https://github.com/astral-sh/ruff/pull/19866))
- Infer slightly more precise types for comprehensions ([#20111](https://github.com/astral-sh/ruff/pull/20111))
- Disable boundness analysis for implicit instance attributes ([#20128](https://github.com/astral-sh/ruff/pull/20128))
- Add `Top[]` and `Bottom[]` special forms ([#20054](https://github.com/astral-sh/ruff/pull/20054))
- Preserve qualifiers when accessing attributes on unions/intersections ([#20114](https://github.com/astral-sh/ruff/pull/20114))
- Strict validation of protocol members ([#17750](https://github.com/astral-sh/ruff/pull/17750))
- Support `__init_subclass__` ([#20190](https://github.com/astral-sh/ruff/pull/20190))
- Unpack variadic argument type in specialization ([#20130](https://github.com/astral-sh/ruff/pull/20130))
- Use `invalid-assignment` error code for invalid assignments to `ClassVar`s ([#20156](https://github.com/astral-sh/ruff/pull/20156))
- Use specialized parameter type for overload filter ([#19964](https://github.com/astral-sh/ruff/pull/19964))
- `__class_getitem__` is a classmethod ([#20192](https://github.com/astral-sh/ruff/pull/20192))
- Add cycle detection for find_legacy_typevars ([#20124](https://github.com/astral-sh/ruff/pull/20124))
- Add support for cyclic legacy generic protocols ([#20125](https://github.com/astral-sh/ruff/pull/20125))
- Don't eagerly unpack aliases in user-authored unions ([#20055](https://github.com/astral-sh/ruff/pull/20055))
- Don't mark entire type-alias scopes as Deferred ([#20086](https://github.com/astral-sh/ruff/pull/20086))
- Ensure union normalization really normalizes ([#20147](https://github.com/astral-sh/ruff/pull/20147))
- Improve cycle-detection coverage for apply_type_mapping ([#20159](https://github.com/astral-sh/ruff/pull/20159))
- Linear variance inference for PEP-695 type parameters ([#18713](https://github.com/astral-sh/ruff/pull/18713))
- Minor `TypedDict` fixes ([#20146](https://github.com/astral-sh/ruff/pull/20146))
- Typecheck dict methods for `TypedDict` ([#19874](https://github.com/astral-sh/ruff/pull/19874))
- Validate constructor call of `TypedDict` ([#19810](https://github.com/astral-sh/ruff/pull/19810))
- Sync vendored typeshed stubs ([#20031](https://github.com/astral-sh/ruff/pull/20031), [#20083](https://github.com/astral-sh/ruff/pull/20083), [#20188](https://github.com/astral-sh/ruff/pull/20188)) [Typeshed diff](https://github.com/python/typeshed/compare/893b9a760deb3be64d13c748318e95a752230961...2480d7e7c74493a024eaf254c5d2c6f452c80ee2)

### Diagnostics

- Add search paths info to unresolved import diagnostics ([#20040](https://github.com/astral-sh/ruff/pull/20040))
- Better error message for attempting to assign to a read-only property ([#20150](https://github.com/astral-sh/ruff/pull/20150))
- Improve diagnostics for bad calls to functions ([#20022](https://github.com/astral-sh/ruff/pull/20022))
- Improve disambiguation of types via fully qualified names ([#20141](https://github.com/astral-sh/ruff/pull/20141))
- Print diagnostics with fully qualified name to disambiguate some cases ([#19850](https://github.com/astral-sh/ruff/pull/19850))

### Performance

- Avoid unnecessary argument type expansion ([#19999](https://github.com/astral-sh/ruff/pull/19999))
- Limit argument expansion size for overload call evaluation ([#20041](https://github.com/astral-sh/ruff/pull/20041))
- Optimize TDD atom ordering ([#20098](https://github.com/astral-sh/ruff/pull/20098))

### Contributors

- [@carljm](https://github.com/carljm)
- [@sharkdp](https://github.com/sharkdp)
- [@dylwil3](https://github.com/dylwil3)
- [@dcreager](https://github.com/dcreager)
- [@MichaReiser](https://github.com/MichaReiser)
- [@ericmarkmartin](https://github.com/ericmarkmartin)
- [@Renkai](https://github.com/Renkai)
- [@JelleZijlstra](https://github.com/JelleZijlstra)
- [@BurntSushi](https://github.com/BurntSushi)
- [@AlexWaygood](https://github.com/AlexWaygood)
- [@github-actions](https://github.com/github-actions)
- [@PrettyWood](https://github.com/PrettyWood)
- [@dhruvmanila](https://github.com/dhruvmanila)
- [@Glyphack](https://github.com/Glyphack)
- [@Gankra](https://github.com/Gankra)
- [@MatthewMckee4](https://github.com/MatthewMckee4)
- [@leandrobbraga](https://github.com/leandrobbraga)

## 0.0.1-alpha.19

### Bug fixes

- Fix false-positive diagnostics if a function parameter is annotated with `type[P]` where `P` is a protocol class ([#19947](https://github.com/astral-sh/ruff/pull/19947))
- Fix ANSI colors in terminal output on old Windows terminals ([#19984](https://github.com/astral-sh/ruff/pull/19984))
- Fix protocol interface inference for protocols in stub files with `ClassVar` members and "subprotocols" that extend other protocols ([#19950](https://github.com/astral-sh/ruff/pull/19950))
- Fix inference of equality comparisons between enum members ([#19666](https://github.com/astral-sh/ruff/pull/19666))
- Remove incorrect type narrowing for `if type(x) is C[int]` ([#19926](https://github.com/astral-sh/ruff/pull/19926))
- Improve detection of `TypeError`s resulting from protocol classes illegally inheriting from non-protocol classes ([#19941](https://github.com/astral-sh/ruff/pull/19941)). We previously detected this error, but only when the protocol class illegally inherited from a non-generic class or an unspecialized generic class. We now also detect it when the protocol class inherits from a specialized generic class.
- Fix incorrectly precise type inference in some situations involving nested scopes ([#19908](https://github.com/astral-sh/ruff/pull/19908))
- Fix unpacking a type alias with a precise tuple spec ([#19981](https://github.com/astral-sh/ruff/pull/19981))

### `NamedTuple` semantics improvements

- Synthesize read-only properties for all declared members on `NamedTuple` classes ([#19899](https://github.com/astral-sh/ruff/pull/19899))
- Allow any instance of a `NamedTuple` class to be passed to a function parameter annotated with `typing.NamedTuple` ([#19915](https://github.com/astral-sh/ruff/pull/19915))
- Detect `NamedTuple` classes where fields without default values illegally follow fields with default values ([#19945](https://github.com/astral-sh/ruff/pull/19945)). This causes `TypeError` to be raised at runtime.
- Detect illegal multiple inheritance with `NamedTuple` ([#19943](https://github.com/astral-sh/ruff/pull/19943)). This causes `TypeError` to be raised at runtime.

### Other typing and semantics improvements

- Add support for stubs packages with `partial` in their `py.typed` files ([#19931](https://github.com/astral-sh/ruff/pull/19931))
- Look for `site-packages` directories in `<sys.prefix>/lib64/` as well as `<sys.prefix>/lib/` on non-Windows systems ([#19978](https://github.com/astral-sh/ruff/pull/19978)). This change fixes a number of `unresolved-import` false-positive diagnostics reported by Poetry users.
- Add diagnostics for invalid `await` expressions ([#19711](https://github.com/astral-sh/ruff/pull/19711))
- Add `else`-branch narrowing for `if type(a) is A` when `A` is `@final` ([#19925](https://github.com/astral-sh/ruff/pull/19925))
- Improve solving of typevars with defaults, and `typing.Self` ([#19786](https://github.com/astral-sh/ruff/pull/19786))
- Support the `kw_only` parameter for `dataclasses.dataclass()` and `dataclasses.field()` ([#19677](https://github.com/astral-sh/ruff/pull/19677))
- Sync vendored typeshed stubs ([#19923](https://github.com/astral-sh/ruff/pull/19923)). [Typeshed diff](https://github.com/python/typeshed/compare/3f08a4ed10b321c378107c236a06a33584869a9b...893b9a760deb3be64d13c748318e95a752230961).

### Server improvements

- Improve goto/hover for definitions ([#19976](https://github.com/astral-sh/ruff/pull/19976))

### Performance improvements

- Short-circuit a server [inlay hints request](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_inlayHint) if all settings under `ty.inlayHints` are disabled ([#19963](https://github.com/astral-sh/ruff/pull/19963))
- Speedup server tracing checks ([#19965](https://github.com/astral-sh/ruff/pull/19965))
- Add caching to logic for inferring whether a class is a `NamedTuple`, a dataclass or a `TypedDict` ([#19912](https://github.com/astral-sh/ruff/pull/19912))
- Speedup project file discovery ([#19913](https://github.com/astral-sh/ruff/pull/19913))

### Contributors

- [@dcreager](https://github.com/dcreager)
- [@MichaReiser](https://github.com/MichaReiser)
- [@sharkdp](https://github.com/sharkdp)
- [@github-actions](https://github.com/github-actions)
- [@mtshiba](https://github.com/mtshiba)
- [@theammir](https://github.com/theammir)
- [@AlexWaygood](https://github.com/AlexWaygood)
- [@thejchap](https://github.com/thejchap)
- [@Gankra](https://github.com/Gankra)
- [@MatthewMckee4](https://github.com/MatthewMckee4)
- [@carljm](https://github.com/carljm)

## 0.0.1-alpha.18

### Bug fixes

- Fix goto definition on imports ([#19834](https://github.com/astral-sh/ruff/pull/19834))
- Support non-generic recursive type aliases that use [the `type` statement](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-type_stmt) ([#19805](https://github.com/astral-sh/ruff/pull/19805))
- Handle cycles when finding implicit attributes ([#19833](https://github.com/astral-sh/ruff/pull/19833))

### Server

- Implement support for "rename" language server feature ([#19551](https://github.com/astral-sh/ruff/pull/19551))
- Add `ty.experimental.rename` server setting ([#19800](https://github.com/astral-sh/ruff/pull/19800))
- Add `ty.inlayHints.variableTypes` server setting ([#19780](https://github.com/astral-sh/ruff/pull/19780))
- Add inlay hints for call arguments (configured by `ty.inlayHints.callArgumentNames` server setting) ([#19269](https://github.com/astral-sh/ruff/pull/19269))
- Enable goto definition to jump to the runtime definition in the standard library for stdlib symbols (rather than the type definition in typeshed's stubs) ([#19529](https://github.com/astral-sh/ruff/pull/19529))
- Support LSP client settings ([#19614](https://github.com/astral-sh/ruff/pull/19614))
- Update goto range for attribute access to only target the attribute ([#19848](https://github.com/astral-sh/ruff/pull/19848))
- Warn users if the server received unknown options ([#19779](https://github.com/astral-sh/ruff/pull/19779))
- Render docstrings in hover ([#19882](https://github.com/astral-sh/ruff/pull/19882))
- Resolve docstrings for modules ([#19898](https://github.com/astral-sh/ruff/pull/19898))

### Typing semantics and features

- Add precise inference for indexing, slicing and unpacking `NamedTuple` instances ([#19560](https://github.com/astral-sh/ruff/pull/19560))
- Disallow `typing.TypedDict` in type expressions ([#19777](https://github.com/astral-sh/ruff/pull/19777))
- Implement module-level `__getattr__` support ([#19791](https://github.com/astral-sh/ruff/pull/19791))
- Improve ability to solve TypeVars when they appear in unions ([#19829](https://github.com/astral-sh/ruff/pull/19829))
- Improve subscript narrowing for `collections.ChainMap`, `collections.Counter`, `collections.deque` and `collections.OrderedDict` ([#19781](https://github.com/astral-sh/ruff/pull/19781))
- Extend all tuple special casing to tuple subclasses ([#19669](https://github.com/astral-sh/ruff/pull/19669))
- Use separate Rust types for bound and unbound type variables ([#19796](https://github.com/astral-sh/ruff/pull/19796))
- Validate writes to `TypedDict` keys ([#19782](https://github.com/astral-sh/ruff/pull/19782))
- `typing.Self` is bound by the method, not the class ([#19784](https://github.com/astral-sh/ruff/pull/19784))
- Fix deferred name loading in PEP695 generic classes/functions ([#19888](https://github.com/astral-sh/ruff/pull/19888))
- Improve handling of symbol-lookup edge cases involving class scopes ([#19795](https://github.com/astral-sh/ruff/pull/19795))

### Performance

- Improve performance around tuple types ([#19840](https://github.com/astral-sh/ruff/pull/19840))
- Improve performance of subtyping and assignability checks for protocols ([#19824](https://github.com/astral-sh/ruff/pull/19824))
- Improve multithreaded performance for large codebases ([#19867](https://github.com/astral-sh/ruff/pull/19867))

### Memory usage optimizations

- Reduce memory usage of `TupleSpec` and `TupleType` ([#19872](https://github.com/astral-sh/ruff/pull/19872))
- Reduce size of member table ([#19572](https://github.com/astral-sh/ruff/pull/19572))

### Contributors

- [@AlexWaygood](https://github.com/AlexWaygood)
- [@Gankra](https://github.com/Gankra)
- [@ntbre](https://github.com/ntBre)
- [@MichaReiser](https://github.com/MichaReiser)
- [@PrettyWood](https://github.com/PrettyWood)
- [@dhruvmanila](https://github.com/dhruvmanila)
- [@carljm](https://github.com/carljm)
- [@dcreager](https://github.com/dcreager)
- [@UnboundVariable](https://github.com/UnboundVariable)
- [@sharkdp](https://github.com/sharkdp)
- [@oconnor663](https://github.com/oconnor663)
- [@MatthewMckee4](https://github.com/MatthewMckee4)

## 0.0.1-alpha.17

### Bug fixes

- Always refresh diagnostics after a watched files change ([#19697](https://github.com/astral-sh/ruff/pull/19697))
- Correctly instantiate generic class that inherits `__init__` from generic base class ([#19693](https://github.com/astral-sh/ruff/pull/19693))
- Don't panic with argument that doesn't actually implement Iterable ([#19602](https://github.com/astral-sh/ruff/pull/19602))
- Fix "peek definition" in playground ([#19592](https://github.com/astral-sh/ruff/pull/19592))
- Fix empty spans following a line terminator and unprintable character spans in diagnostics ([#19535](https://github.com/astral-sh/ruff/pull/19535))
- Fix incorrect diagnostic when calling `__setitem__` ([#19645](https://github.com/astral-sh/ruff/pull/19645))
- Fix lookup order of class variables before they are defined ([#19743](https://github.com/astral-sh/ruff/pull/19743))
- Fix more false positives related to `Generic` or `Protocol` being subscripted with a `ParamSpec` or `TypeVarTuple` ([#19764](https://github.com/astral-sh/ruff/pull/19764))
- Keep track of type qualifiers in stub declarations without right-hand side ([#19756](https://github.com/astral-sh/ruff/pull/19756))

### Server

- Add progress reporting to workspace diagnostics ([#19616](https://github.com/astral-sh/ruff/pull/19616))
- Add stub mapping support to signature help ([#19570](https://github.com/astral-sh/ruff/pull/19570))
- Added support for "document symbols" and "workspace symbols" ([#19521](https://github.com/astral-sh/ruff/pull/19521))
- Fix server panic in workspace diagnostics request handler when typing ([#19631](https://github.com/astral-sh/ruff/pull/19631))
- Implement caching for workspace and document diagnostics ([#19605](https://github.com/astral-sh/ruff/pull/19605))
- Implement long-polling for workspace diagnostics ([#19670](https://github.com/astral-sh/ruff/pull/19670))
- Implement streaming for workspace diagnostics ([#19657](https://github.com/astral-sh/ruff/pull/19657))
- Implemented support for "selection range" language server feature ([#19567](https://github.com/astral-sh/ruff/pull/19567))

### CLI

- Add progress bar to `--watch` mode ([#19729](https://github.com/astral-sh/ruff/pull/19729))
- Clear the terminal screen in `--watch` mode ([#19712](https://github.com/astral-sh/ruff/pull/19712))
- Resolve file symlinks in src walk ([#19674](https://github.com/astral-sh/ruff/pull/19674))

### Typing semantics and features

- Support `async`/`await`, `async with` and `yield from` ([#19595](https://github.com/astral-sh/ruff/pull/19595))
- Add support for `async for` loops and async iterables ([#19634](https://github.com/astral-sh/ruff/pull/19634))
- Don't include already-bound legacy typevars in function generic context ([#19558](https://github.com/astral-sh/ruff/pull/19558))
- Infer types for key-based access on `TypedDict`s ([#19763](https://github.com/astral-sh/ruff/pull/19763))
- Improve `isinstance()` truthiness analysis for generic types ([#19668](https://github.com/astral-sh/ruff/pull/19668))
- Infer `type[tuple[int, str]]` as the meta-type of `tuple[int, str]` ([#19741](https://github.com/astral-sh/ruff/pull/19741))
- Remove false positives when subscripting `Generic` or `Protocol` with a `ParamSpec` or `TypeVarTuple` ([#19749](https://github.com/astral-sh/ruff/pull/19749))
- Remove special casing for string-literal-in-tuple `__contains__` ([#19642](https://github.com/astral-sh/ruff/pull/19642))
- Remove special casing for tuple addition ([#19636](https://github.com/astral-sh/ruff/pull/19636))
- Return `Option<TupleType>` from `infer_tuple_type_expression` ([#19735](https://github.com/astral-sh/ruff/pull/19735))
- Support `as`-patterns in reachability analysis ([#19728](https://github.com/astral-sh/ruff/pull/19728))
- Support `__setitem__` and improve `__getitem__` related diagnostics ([#19578](https://github.com/astral-sh/ruff/pull/19578))
- Synthesize precise `__getitem__` overloads for tuple subclasses ([#19493](https://github.com/astral-sh/ruff/pull/19493))
- Track different uses of legacy typevars, including context when rendering typevars ([#19604](https://github.com/astral-sh/ruff/pull/19604))
- Upcast heterogeneous and mixed tuples to homogeneous tuples where it's necessary to solve a `TypeVar` ([#19635](https://github.com/astral-sh/ruff/pull/19635))
- Fix incorrect lazy scope narrowing ([#19744](https://github.com/astral-sh/ruff/pull/19744))
- Synthesize `__replace__` for dataclasses ([#19545](https://github.com/astral-sh/ruff/pull/19545))

### Diagnostics

- Add diagnostics for async context managers ([#19704](https://github.com/astral-sh/ruff/pull/19704))
- Display generic function signature properly ([#19544](https://github.com/astral-sh/ruff/pull/19544))
- Improve the `Display` for generic `type[]` types ([#19667](https://github.com/astral-sh/ruff/pull/19667))
- Remap Jupyter notebook cell indices in `ruff_db` ([#19698](https://github.com/astral-sh/ruff/pull/19698))

### Documentation

- Add the `ty` badge ([#897](https://github.com/astral-sh/ty/pull/897))

### Contributors

- [@mtshiba](https://github.com/mtshiba)
- [@MichaReiser](https://github.com/MichaReiser)
- [@sharkdp](https://github.com/sharkdp)
- [@github-actions](https://github.com/github-actions)
- [@UnboundVariable](https://github.com/UnboundVariable)
- [@jorenham](https://github.com/jorenham)
- [@silamon](https://github.com/silamon)
- [@AlexWaygood](https://github.com/AlexWaygood)
- [@thejchap](https://github.com/thejchap)
- [@ngroman](https://github.com/ngroman)
- [@leandrobbraga](https://github.com/leandrobbraga)
- [@dcreager](https://github.com/dcreager)
- [@ntbre](https://github.com/ntBre)
- [@MatthewMckee4](https://github.com/MatthewMckee4)

## 0.0.1-alpha.16

### Bug fixes

- Fix server panics when hovering over invalid syntax in `Callable` annotations ([#19517](https://github.com/astral-sh/ruff/pull/19517))
- `match` statements: Fix narrowing and reachability of class patterns with arguments ([#19512](https://github.com/astral-sh/ruff/pull/19512))
- Fix server panics when hovering over illegal `Literal[…]` annotations with inner subscript expressions ([#19489](https://github.com/astral-sh/ruff/pull/19489))
- Pass down specialization to generic dataclass bases ([#19472](https://github.com/astral-sh/ruff/pull/19472))

### Server

- Add support for "go to definition" for attribute accesses and keyword arguments ([#19417](https://github.com/astral-sh/ruff/pull/19417))
- Add support for "go to definition" for import statements ([#19428](https://github.com/astral-sh/ruff/pull/19428))
- Add support for "document highlights" ([#19515](https://github.com/astral-sh/ruff/pull/19515))
- Add partial support for "find references" ([#19475](https://github.com/astral-sh/ruff/pull/19475))
- Prefer the runtime definition, not the stub definition, on a go-to-definition request for a class or function. Currently this is only implemented for definitions originating outside of the stdlib. ([#19471](https://github.com/astral-sh/ruff/pull/19471))
- Add [semantic token](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_semanticTokens) support for more identifiers ([#19473](https://github.com/astral-sh/ruff/pull/19473))
- Avoid rechecking the entire project when a file in the editor is opened or closed ([#19463](https://github.com/astral-sh/ruff/pull/19463))

### Typing semantics and features

- Handle splatted arguments in function calls ([#18996](https://github.com/astral-sh/ruff/pull/18996))
- Improve place lookup and narrowing in lazy scopes ([#19321](https://github.com/astral-sh/ruff/pull/19321))
- Add exhaustiveness checking and reachability analysis for `match` statements ([#19508](https://github.com/astral-sh/ruff/pull/19508))
- Improve reachability analysis for `isinstance(…)` branches ([#19503](https://github.com/astral-sh/ruff/pull/19503))
- Make tuple subclass constructors sound ([#19469](https://github.com/astral-sh/ruff/pull/19469))
- Extend tuple `__len__` and `__bool__` special casing to also cover tuple subclasses ([#19289](https://github.com/astral-sh/ruff/pull/19289))
- Add support for `dataclasses.field` ([#19553](https://github.com/astral-sh/ruff/pull/19553))
- Add support for `dataclasses.InitVar` ([#19527](https://github.com/astral-sh/ruff/pull/19527))
- Add support for `@warnings.deprecated` and `typing_extensions.deprecated` ([#19376](https://github.com/astral-sh/ruff/pull/19376))
- Do not consider a type `T` to satisfy a method member on a protocol unless the method is available on the meta-type of `T` ([#19187](https://github.com/astral-sh/ruff/pull/19187))
- Implement expansion of enums into unions of literals ([#19382](https://github.com/astral-sh/ruff/pull/19382))
- Support iterating over enums ([#19486](https://github.com/astral-sh/ruff/pull/19486))
- Detect enums if metaclass is a subtype of `EnumType` / `EnumMeta` ([#19481](https://github.com/astral-sh/ruff/pull/19481))
- Infer single-valuedness for enums deriving from `int` or `str` ([#19510](https://github.com/astral-sh/ruff/pull/19510))
- Detect illegal non-enum attribute accesses in `Literal` annotations ([#19477](https://github.com/astral-sh/ruff/pull/19477))
- Disallow assignment to `Final` class attributes ([#19457](https://github.com/astral-sh/ruff/pull/19457))
- Handle implicit instance attributes declared `Final` ([#19462](https://github.com/astral-sh/ruff/pull/19462))
- Disallow `Final` in function parameter- and return-type annotations ([#19480](https://github.com/astral-sh/ruff/pull/19480))
- Disallow illegal uses of `ClassVar` ([#19483](https://github.com/astral-sh/ruff/pull/19483))
- Make `del x` force a local resolution of `x` in the current scope ([#19389](https://github.com/astral-sh/ruff/pull/19389))
- Perform type narrowing for places marked `global` ([#19381](https://github.com/astral-sh/ruff/pull/19381))
- Infer correct types for attribute accesses on intersections with negative parts ([#19524](https://github.com/astral-sh/ruff/pull/19524))
- Sync vendored typeshed stubs ([typeshed diff](https://github.com/python/typeshed/compare/84e41f2853d7af3d651d620f093031cba849bd1d...08225953c98cfd375d80bc88865e5aae77d2c07f))

### Memory usage optimizations

- Reduce ty's memory usage (for example: [#19409](https://github.com/astral-sh/ruff/pull/19409), [#19435](https://github.com/astral-sh/ruff/pull/19435), [#19414](https://github.com/astral-sh/ruff/pull/19414))

### Contributors

- [@sharkdp](https://github.com/sharkdp)
- [@BurntSushi](https://github.com/BurntSushi)
- [@oconnor663](https://github.com/oconnor663)
- [@Gankra](https://github.com/Gankra)
- [@carljm](https://github.com/carljm)
- [@AlexWaygood](https://github.com/AlexWaygood)
- [@MichaReiser](https://github.com/MichaReiser)
- [@dcreager](https://github.com/dcreager)
- [@mtshiba](https://github.com/mtshiba)
- [@UnboundVariable](https://github.com/UnboundVariable)

## 0.0.1-alpha.15

### Bug fixes

- Avoid stale diagnostics for open-files diagnostic mode ([#19273](https://github.com/astral-sh/ruff/pull/19273))
- Fix inconsistent semantic syntax highlighting for parameters ([#19418](https://github.com/astral-sh/ruff/pull/19418))
- Fix checking of virtual files after re-opening from an unsaved edit ([#19277](https://github.com/astral-sh/ruff/pull/19277))
- Show the correct ty version in the LSP server ([#19284](https://github.com/astral-sh/ruff/pull/19284))
- Do not surface settings errors in unrelated Python files ([#19206](https://github.com/astral-sh/ruff/pull/19206))
- Do not ignore conditionally defined dataclass fields ([#19197](https://github.com/astral-sh/ruff/pull/19197))
- Fix panic for attribute expressions with empty value ([#19069](https://github.com/astral-sh/ruff/pull/19069))
- Fix assignabiliy of dataclasses to `Callable` types ([#19192](https://github.com/astral-sh/ruff/pull/19192))
- Fix `__setattr__` call check precedence during attribute assignment ([#18347](https://github.com/astral-sh/ruff/pull/18347))

### Server

- Add definition and declaration providers (go-to-definition, go-to-declaration) ([#19371](https://github.com/astral-sh/ruff/pull/19371))
- Add signature help provider (show signature and docstring when writing a call expression) ([#19194](https://github.com/astral-sh/ruff/pull/19194))
- Add "kind" to completion suggestions ([#19216](https://github.com/astral-sh/ruff/pull/19216))
- Add completions for submodules that aren't attributes of their parent ([#19266](https://github.com/astral-sh/ruff/pull/19266))
- Filter out private type aliases from stub files when offering autocomplete suggestions ([#19282](https://github.com/astral-sh/ruff/pull/19282))
- Handle configuration errors in the LSP more gracefully ([#19262](https://github.com/astral-sh/ruff/pull/19262))
- Use Python version and path from VSCode Python extension ([#19012](https://github.com/astral-sh/ruff/pull/19012))
- Publish errors in settings as LSP diagnostics ([#19335](https://github.com/astral-sh/ruff/pull/19335))

### Typing semantics and features

- Add support for `nonlocal` statements ([#19112](https://github.com/astral-sh/ruff/pull/19112))
- Support empty function bodies in `if TYPE_CHECKING` blocks ([#19372](https://github.com/astral-sh/ruff/pull/19372))
- Emit a diagnostic when attempting to modify a `typing.Final`-qualified symbol ([#19178](https://github.com/astral-sh/ruff/pull/19178))
- Infer enum literal types when accessing enum members ([#19328](https://github.com/astral-sh/ruff/pull/19328))
- Synthesize `__setattr__` for frozen dataclasses ([#19307](https://github.com/astral-sh/ruff/pull/19307))
- Improve equivalence for module-literal types ([#19243](https://github.com/astral-sh/ruff/pull/19243))
- Reduce false positives for `TypedDict` types ([#19354](https://github.com/astral-sh/ruff/pull/19354))
- Emit an error for `global` uses if there is no explicit definition in the global scope ([#19344](https://github.com/astral-sh/ruff/pull/19344))
- Sync vendored typeshed stubs ([typeshed diff](https://github.com/python/typeshed/compare/f64707592dd3c32f756ddeebd012acb2b072aa0d...84e41f2853d7af3d651d620f093031cba849bd1d))

### CLI

- Add a `-q`/`--quiet` mode, `-qq` for silent output mode ([#19233](https://github.com/astral-sh/ruff/pull/19233))

### Contributors

- [@AlexWaygood](https://github.com/AlexWaygood)
- [@github-actions](https://github.com/github-actions)
- [@dhruvmanila](https://github.com/dhruvmanila)
- [@sharkdp](https://github.com/sharkdp)
- [@renovate](https://github.com/renovate)
- [@MatthewMckee4](https://github.com/MatthewMckee4)
- [@UnboundVariable](https://github.com/UnboundVariable)
- [@oconnor663](https://github.com/oconnor663)
- [@zanieb](https://github.com/zanieb)
- [@MichaReiser](https://github.com/MichaReiser)
- [@charliermarsh](https://github.com/charliermarsh)
- [@Gankra](https://github.com/Gankra)
- [@thejchap](https://github.com/thejchap)
- [@BurntSushi](https://github.com/BurntSushi)
- [@mdqst](https://github.com/mdqst)

## 0.0.1-alpha.14

### Bug fixes

- Add cycle detection to ty's implementation of disjointness between types, fixing a possible source of stack overflows when analysing recursive types ([#19139](https://github.com/astral-sh/ruff/pull/19139))
- Don't allow first-party code to shadow the stdlib `types` module ([#19128](https://github.com/astral-sh/ruff/pull/19128)).
    This fixes another possible source of stack overflows.
- Fix descriptor lookups for most types that overlap with `None` ([#19120](https://github.com/astral-sh/ruff/pull/19120)).
    This means that e.g. `object().__str__()` now correctly binds the `self` argument of the `__str__`
    method, as the `object` type overlaps with `None`.

### Server

- Filter a symbol from a stub file in autocomplete suggestions if it is an implementation detail of the stub ([#19121](https://github.com/astral-sh/ruff/pull/19121))
- Add initial support for [semantic tokens](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_semanticTokens) ([#19108](https://github.com/astral-sh/ruff/pull/19108)).
    This feature allows editors to apply more advanced syntax highlighting. Currently, the supported tokens are: `Namespace`, `Class`, `Parameter`, `SelfParameter`,`ClsParameter`, `Variable`, `Property`, `Function`, `Method`, `Keyword`, `String`, `Number`, `Decorator`, `BuiltinConstant` and `TypeParameter`.
- Initial support for [workspace diagnostics](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#workspace_diagnostic) ([#18939](https://github.com/astral-sh/ruff/pull/18939)).
    Enable this feature by setting the `ty.diagnosticMode` configuration setting to `"workspace"`.
- Use Python syntax highlighting in on-hover content ([#19082](https://github.com/astral-sh/ruff/pull/19082))

### Typing semantics and features

- Understand that calls to functions returning `Never` / `NoReturn` are terminal with respect to control flow ([#18333](https://github.com/astral-sh/ruff/pull/18333))
- Add subtyping between `type[]` types and `Callable` types ([#19026](https://github.com/astral-sh/ruff/pull/19026))
- Support bare `ClassVar` annotations ([#15768](https://github.com/astral-sh/ruff/pull/15768))
- Understand that two protocols with equivalent method members are equivalent ([#18659](https://github.com/astral-sh/ruff/pull/18659))
- Support declared-only instance attributes such as `self.x: int` ([#19048](https://github.com/astral-sh/ruff/pull/19048))
- Sync vendored typeshed stubs ([#19174](https://github.com/astral-sh/ruff/pull/19174)): [typeshed diff](https://github.com/python/typeshed/compare/3f727b0cd6620b7fca45318dd34542b1e1c7dbfb...f64707592dd3c32f756ddeebd012acb2b072aa0d)
- Use the inferred type as the declared type for bare `Final` symbols ([#19142](https://github.com/astral-sh/ruff/pull/19142))

### Contributors

- [@iyakushev](https://github.com/iyakushev)
- [@MatthewMckee4](https://github.com/MatthewMckee4)
- [@zanieb](https://github.com/zanieb)
- [@sharkdp](https://github.com/sharkdp)
- [@UnboundVariable](https://github.com/UnboundVariable)
- [@abhijeetbodas2001](https://github.com/abhijeetbodas2001)
- [@github-actions](https://github.com/github-actions)
- [@dhruvmanila](https://github.com/dhruvmanila)
- [@AlexWaygood](https://github.com/AlexWaygood)
- [@carljm](https://github.com/carljm)
- [@CodeMan62](https://github.com/CodeMan62)

## 0.0.1-alpha.13

### Bug fixes

- Fix stack overflows related to mutually recursive protocols ([#19003](https://github.com/astral-sh/ruff/pull/19003))
- Don't add incorrect subdiagnostic for `unresolved-reference` in `staticmethod`s and `classmethod`s ([#18487](https://github.com/astral-sh/ruff/pull/18487))
- Fix rendering of long lines in diagnostic messages that are indented with tabs ([#18962](https://github.com/astral-sh/ruff/pull/18962))
- Fix reachability of star import definitions for nonlocal lookups ([#19066](https://github.com/astral-sh/ruff/pull/19066))

### Typing semantics and features

- Support variable-length tuples in unpacking assignments ([#18948](https://github.com/astral-sh/ruff/pull/18948))
- Allow declared-only class-level attributes to be accessed on the class ([#19071](https://github.com/astral-sh/ruff/pull/19071))
- Infer nonlocal types as unions of all reachable bindings ([#18750](https://github.com/astral-sh/ruff/pull/18750))
- Use all reachable bindings for instance attributes and deferred lookups ([#18955](https://github.com/astral-sh/ruff/pull/18955))
- Improve protocol member type checking and relation handling ([#18847](https://github.com/astral-sh/ruff/pull/18847))
- Rework disjointness of protocol instances vs types with possibly unbound attributes, preventing some false instances of `Never` in `hasattr` narrowing ([#19043](https://github.com/astral-sh/ruff/pull/19043))
- Make tuple instantiations sound ([#18987](https://github.com/astral-sh/ruff/pull/18987))
- Add subdiagnostic about empty bodies in more cases ([#18942](https://github.com/astral-sh/ruff/pull/18942))
- Improve type-inference for `__import__(name)` and `importlib.import_module(name)` ([#19008](https://github.com/astral-sh/ruff/pull/19008))
- Eagerly evaluate certain constraints when analyzing control flow ([#18998](https://github.com/astral-sh/ruff/pull/18998), [#19044](https://github.com/astral-sh/ruff/pull/19044), [#19068](https://github.com/astral-sh/ruff/pull/19068))
- Update typeshed stubs ([#19060](https://github.com/astral-sh/ruff/pull/19060)): [typeshed diff](https://github.com/python/typeshed/compare/ecd5141cc036366cc9e3ca371096d6a14b0ccd13...3f727b0cd6620b7fca45318dd34542b1e1c7dbfb)

### Server

- Add `builtins` to completions ([#18982](https://github.com/astral-sh/ruff/pull/18982))
- Support LSP go-to with vendored typeshed stubs ([#19057](https://github.com/astral-sh/ruff/pull/19057))

### Documentation

- The ty documentation is now available at [docs.astral.sh/ty](https://docs.astral.sh/ty) ([#744](https://github.com/astral-sh/ty/pull/744))

### Performance

- Remove `ScopedExpressionId` ([#19019](https://github.com/astral-sh/ruff/pull/19019))

### Contributors

- [@InSyncWithFoo](https://github.com/InSyncWithFoo)
- [@MatthewMckee4](https://github.com/MatthewMckee4)
- [@dcreager](https://github.com/dcreager)
- [@mtshiba](https://github.com/mtshiba)
- [@BurntSushi](https://github.com/BurntSushi)
- [@sharkdp](https://github.com/sharkdp)
- [@ibraheemdev](https://github.com/ibraheemdev)
- [@github-actions](https://github.com/github-actions)
- [@carljm](https://github.com/carljm)
- [@AlexWaygood](https://github.com/AlexWaygood)
- [@MichaReiser](https://github.com/MichaReiser)
- [@zanieb](https://github.com/zanieb)

## 0.0.1-alpha.12

### Bug fixes

- Avoid duplicate diagnostic when reporting errors in unpacked assignments ([#18897](https://github.com/astral-sh/ruff/pull/18897))
- Fix panics when "pulling types" for `ClassVar` or `Final` parameterized with >1 argument ([#18824](https://github.com/astral-sh/ruff/pull/18824)). These could cause issues when hovering over symbols in an IDE.

### Improved modeling of Python runtime semantics

- Add support for `@staticmethod`s ([#18809](https://github.com/astral-sh/ruff/pull/18809))
- Discover implicit class attribute assignments in `@classmethod`-decorated methods. Recognize that assignments in the body of a `@staticmethod`-decorated method are never instance attributes ([#18587](https://github.com/astral-sh/ruff/pull/18587))
- Report when a dataclass contains more than one `KW_ONLY` field ([#18731](https://github.com/astral-sh/ruff/pull/18731))

### Type narrowing improvements

- Ty will now perform `isinstance()` and `issubclass()` narrowing when the second argument is a union type, intersection type or `TypeVar` type ([#18900](https://github.com/astral-sh/ruff/pull/18900))
- Ty now narrows types in comprehensions and generator expressions ([#18934](https://github.com/astral-sh/ruff/pull/18934))
- Understand two `NominalInstanceType`s as disjoint types if attempting to use multiple inheritance with their underlying classes would result in an instance memory layout conflict ([#18864](https://github.com/astral-sh/ruff/pull/18864))

### Other typing semantics features

- Support "mixed" tuples such as `tuple[int, *tuple[str, ...]]` ([#18600](https://github.com/astral-sh/ruff/pull/18600), [#18901](https://github.com/astral-sh/ruff/pull/18901))
- Support type inference for subscript expressions on union types ([#18846](https://github.com/astral-sh/ruff/pull/18846))
- Introduce a new subtyping framework in which gradual types can participate, allowing for more advanced union type simplification ([#18799](https://github.com/astral-sh/ruff/pull/18799))
- Surface the matched overload directly when reporting a diagnostic for an invalid call to an overloaded function ([#18452](https://github.com/astral-sh/ruff/pull/18452))

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
