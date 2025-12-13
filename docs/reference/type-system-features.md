<!-- markdownlint-disable -->

# Type system features

This page summarizes the support for various type system features in ty.

## Dataclasses

[Official documentation](https://typing.python.org/en/latest/spec/dataclasses.html)

| Feature                                                                                                                           | Status                                                |
| :-------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------- |
| `@dataclass` decorator (`init`, `repr`, `eq`, `order`, `frozen`, `match_args`, `kw_only`, `slots`, `weakref_slot`, `unsafe_hash`) | ✅                                                    |
| `field()` (`default`, `default_factory`, `init`, `kw_only`, `doc`, `repr`, `hash`, `compare`)                                     | ✅                                                    |
| `InitVar[…]`, `ClassVar[…]` exclusion, `KW_ONLY` sentinel                                                                         | ✅                                                    |
| `fields()`, `__dataclass_fields__`                                                                                                | ✅                                                    |
| `Final` fields                                                                                                                    | ✅                                                    |
| Inheritance, generic dataclasses, descriptor-typed fields                                                                         | ✅                                                    |
| `replace()`, `__replace__`                                                                                                        | ⚠️ `__replace__` works, `replace()` returns `Unknown` |
| `asdict()`                                                                                                                        | ⚠️ incorrectly accepts class objects                  |
| `astuple()`                                                                                                                       | ⚠️ not tested                                         |
| `make_dataclass()`, `is_dataclass()`                                                                                              | ⚠️ not tested                                         |
| Diagnostic: frozen dataclass inheriting from non-frozen                                                                           | ⚠️ not tested                                         |
| Diagnostic: non-default field after default field                                                                                 | ❌ [#111](https://github.com/astral-sh/ty/issues/111) |
| Diagnostic: `order=True` with custom comparison methods                                                                           | ❌ [#111](https://github.com/astral-sh/ty/issues/111) |
| Diagnostic: `frozen=True` with `__setattr__`/`__delattr__`                                                                        | ❌ [#111](https://github.com/astral-sh/ty/issues/111) |
| `__post_init__` signature validation                                                                                              | ❌ [#111](https://github.com/astral-sh/ty/issues/111) |

## `dataclass_transform`

[Official documentation](https://typing.python.org/en/latest/spec/dataclasses.html#dataclass-transform)

| Feature                                                                                  | Status                                                  |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Function-based, metaclass-based, base-class-based transformers                           | ✅                                                      |
| `eq_default`, `order_default`, `kw_only_default` parameters                              | ✅                                                      |
| `frozen_default` parameter                                                               | ⚠️ metaclass override not working                       |
| `field_specifiers` (`init`, `default`, `default_factory`, `factory`, `kw_only`, `alias`) | ✅                                                      |
| `field_specifiers` (`converter`)                                                         | ❌ [#1327](https://github.com/astral-sh/ty/issues/1327) |
