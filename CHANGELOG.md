# Changelog

## 0.0.1a1

### Bug fixes

- fix infinite recursion bug in `is_disjoint_from` ([#18043](https://github.com/astral-sh/ruff/pull/18043))

### Typing

- Allow a class to inherit from an intersection if the intersection contains a dynamic type and the intersection is not disjoint from `type` ([#18055](https://github.com/astral-sh/ruff/pull/18055))
- Allow classes to inherit from `type[Any]` or `type[Unknown]` ([#18060](https://github.com/astral-sh/ruff/pull/18060))
- Apply function specialization to all overloads ([#18020](https://github.com/astral-sh/ruff/pull/18020))
- Implement `DataClassInstance` protocol for dataclasses. ([#18018](https://github.com/astral-sh/ruff/pull/18018))
- Induct into instances and subclasses when finding and applying generics ([#18052](https://github.com/astral-sh/ruff/pull/18052))
- Infer parameter specializations of generic aliases ([#18021](https://github.com/astral-sh/ruff/pull/18021))
- Narrowing for `hasattr()` ([#18053](https://github.com/astral-sh/ruff/pull/18053))
- Silence false positives for PEP-695 ParamSpec annotations ([#18001](https://github.com/astral-sh/ruff/pull/18001))
- Understand homogeneous tuple annotations ([#17998](https://github.com/astral-sh/ruff/pull/17998))

### CLI

- Avoid initializing progress bars early ([#18049](https://github.com/astral-sh/ruff/pull/18049))

### Other changes

- Add basic support for non-virtual Python environments ([#17991](https://github.com/astral-sh/ruff/pull/17991))
- Do not allow invalid virtual environments from discovered `.venv` or `VIRTUAL_ENV` ([#18003](https://github.com/astral-sh/ruff/pull/18003))
- Refine message for why a rule is enabled ([#18038](https://github.com/astral-sh/ruff/pull/18038))
- Update `--python` to accept paths to executables in environments ([#17954](https://github.com/astral-sh/ruff/pull/17954))
- Improve diagnostics for assert_type and assert_never ([#18050](https://github.com/astral-sh/ruff/pull/18050))
- Add a note to the diagnostic if a new builtin is used on an old Python version ([#18068](https://github.com/astral-sh/ruff/pull/18068))

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

## 0.0.0a8

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
