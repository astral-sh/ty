# Changelog

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
