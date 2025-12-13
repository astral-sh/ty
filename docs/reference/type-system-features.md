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

## `NamedTuple`

[Official documentation](https://typing.python.org/en/latest/spec/namedtuples.html)

| Feature                                                      | Status                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------- |
| Class syntax (`class Foo(NamedTuple): ...`)                  | ✅                                                      |
| Field access by name and index, slicing, unpacking           | ✅                                                      |
| Default values, diagnostic for non-default after default     | ✅                                                      |
| Read-only fields (assignment rejected)                       | ✅                                                      |
| Inheritance, generic `NamedTuple`s                           | ✅                                                      |
| Multiple inheritance restriction                             | ✅                                                      |
| Underscore field name restriction                            | ✅                                                      |
| Prohibited attribute override check (`_asdict`, `_make`, …)  | ✅                                                      |
| `_fields`, `_field_defaults`, `_make`, `_asdict`, `_replace` | ✅                                                      |
| Subtype of `tuple[...]`                                      | ✅                                                      |
| `super()` restriction in `NamedTuple` methods                | ✅                                                      |
| `NamedTuple` in type expressions                             | ✅                                                      |
| Functional syntax (`NamedTuple("Foo", [...])`)               | ❌ [#1049](https://github.com/astral-sh/ty/issues/1049) |
| `collections.namedtuple`                                     | ⚠️ not tested                                           |
| Subclass field conflicting with base class field             | ⚠️ not tested                                           |
| `type[NamedTuple]` in type expressions                       | ⚠️ not fully supported                                  |

## `TypedDict`

[Official documentation](https://typing.python.org/en/latest/spec/typeddict.html)

| Feature                                                        | Status                                                  |
| -------------------------------------------------------------- | ------------------------------------------------------- |
| Class syntax (`class Foo(TypedDict): ...`)                     | ✅                                                      |
| Key access by literal string, `Final` constants                | ✅                                                      |
| Constructor validation (missing keys, invalid types)           | ✅                                                      |
| `total` parameter                                              | ✅                                                      |
| `Required[…]`, `NotRequired[…]`                                | ✅                                                      |
| `ReadOnly[…]`                                                  | ✅                                                      |
| Inheritance, generic `TypedDict`s                              | ✅                                                      |
| Recursive `TypedDict`                                          | ✅                                                      |
| Structural assignability and equivalence                       | ✅                                                      |
| Methods (`get`, `pop`, `setdefault`, `keys`, `values`, `copy`) | ✅                                                      |
| `__total__`, `__required_keys__`, `__optional_keys__`          | ✅                                                      |
| Functional syntax (`TypedDict("Foo", {...})`)                  | ❌ [#154](https://github.com/astral-sh/ty/issues/154)   |
| `closed`, `extra_items` (PEP 728)                              | ❌ [#154](https://github.com/astral-sh/ty/issues/154)   |
| `Unpack` for `**kwargs` typing                                 | ❌ [#1746](https://github.com/astral-sh/ty/issues/1746) |
| Tagged union narrowing                                         | ❌ [#1479](https://github.com/astral-sh/ty/issues/1479) |
| Diagnostic: Invalid `isinstance()` check on `TypedDict`        | ⚠️ not tested                                           |

## Generics

[Official documentation](https://typing.python.org/en/latest/spec/generics.html)

| Feature                                           | Status                                                                   |
| ------------------------------------------------- | ------------------------------------------------------------------------ |
| `TypeVar` (legacy syntax)                         | ✅                                                                       |
| `TypeVar` (PEP 695 syntax: `def f[T]()`)          | ✅                                                                       |
| `TypeVar` upper bound (`bound=`)                  | ✅                                                                       |
| `TypeVar` constraints                             | ✅                                                                       |
| `TypeVar` defaults (PEP 696)                      | ✅                                                                       |
| `TypeVar` variance (`covariant`, `contravariant`) | ✅                                                                       |
| `TypeVar` variance inference (`infer_variance`)   | ✅                                                                       |
| Generic classes (legacy and PEP 695 syntax)       | ✅                                                                       |
| Generic functions (legacy and PEP 695 syntax)     | ✅                                                                       |
| Generic type aliases (PEP 695)                    | ⚠️ some limitations [#1851](https://github.com/astral-sh/ty/issues/1851) |
| `ParamSpec` (legacy and PEP 695 syntax)           | ✅                                                                       |
| `ParamSpec.args`, `ParamSpec.kwargs`              | ✅                                                                       |
| `Concatenate`                                     | ✅                                                                       |
| `ParamSpec` defaults                              | ✅                                                                       |
| `TypeVarTuple`                                    | ❌ [#156](https://github.com/astral-sh/ty/issues/156)                    |
| `Unpack` for `*args` typing                       | ❌ [#156](https://github.com/astral-sh/ty/issues/156)                    |
| `Self`                                            | ✅                                                                       |
