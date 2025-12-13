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

## Protocols

[Official documentation](https://typing.python.org/en/latest/spec/protocol.html)

| Feature                                       | Status                                                          |
| --------------------------------------------- | --------------------------------------------------------------- |
| `Protocol` class definition                   | ✅                                                              |
| Generic protocols (legacy and PEP 695 syntax) | ✅                                                              |
| Structural subtyping / assignability          | ✅                                                              |
| Protocol inheritance                          | ✅                                                              |
| `is_protocol()`, `get_protocol_members()`     | ✅                                                              |
| `@runtime_checkable` decorator                | ✅                                                              |
| Protocol instantiation restriction            | ✅                                                              |
| Non-protocol class inheritance restriction    | ✅                                                              |
| `@property` members                           | ⚠️ partial [#1379](https://github.com/astral-sh/ty/issues/1379) |
| `@classmethod` and `@staticmethod` members    | ❌ [#1381](https://github.com/astral-sh/ty/issues/1381)         |
| `ClassVar` members                            | ❌ [#1380](https://github.com/astral-sh/ty/issues/1380)         |
| `type[SomeProtocol]`                          | ❌ [#903](https://github.com/astral-sh/ty/issues/903)           |
| Modules as protocol implementations           | ❌ [#931](https://github.com/astral-sh/ty/issues/931)           |

## Overloads

[Official documentation](https://typing.python.org/en/latest/spec/overload.html)

| Feature                                                | Status                                                             |
| ------------------------------------------------------ | ------------------------------------------------------------------ |
| `@overload` decorator                                  | ✅                                                                 |
| Overload resolution                                    | ✅                                                                 |
| Generic overloads                                      | ✅                                                                 |
| Methods, constructors, `@staticmethod`, `@classmethod` | ✅                                                                 |
| Version-specific overloads                             | ✅                                                                 |
| Diagnostic: at least two overloads required            | ✅                                                                 |
| Diagnostic: missing implementation (non-stub)          | ✅                                                                 |
| Diagnostic: inconsistent decorators                    | ✅                                                                 |
| Diagnostic: `@final`/`@override` placement             | ✅                                                                 |
| Unannotated implementation validation                  | ⚠️ not tested [#1232](https://github.com/astral-sh/ty/issues/1232) |

## Enums

[Official documentation](https://typing.python.org/en/latest/spec/enums.html)

| Feature                                    | Status                                                  |
| ------------------------------------------ | ------------------------------------------------------- |
| `Enum`, `IntEnum`, `StrEnum`               | ✅                                                      |
| `Literal[EnumMember]` types                | ✅                                                      |
| `.name`, `.value` inference                | ✅                                                      |
| `auto()` value inference                   | ✅                                                      |
| `member()`, `nonmember()`                  | ✅                                                      |
| Enum aliases                               | ✅                                                      |
| `_ignore_` attribute                       | ⚠️ list form not fully supported                        |
| Implicitly final (subclassing restriction) | ✅                                                      |
| Exhaustiveness checking (`if`/`match`)     | ✅                                                      |
| Custom `__eq__`/`__ne__` methods           | ✅                                                      |
| Iteration over enum members                | ⚠️ `list(Enum)` returns `list[Unknown]`                 |
| Functional syntax (`Enum("Name", [...])`)  | ❌                                                      |
| Narrowing with custom `__eq__` in `match`  | ❌ [#1454](https://github.com/astral-sh/ty/issues/1454) |

## Type narrowing

[Official documentation](https://typing.python.org/en/latest/spec/narrowing.html)

| Feature                                   | Status                                                  |
| ----------------------------------------- | ------------------------------------------------------- |
| `isinstance()` / `issubclass()` narrowing | ✅                                                      |
| `is None` / `is not None` narrowing       | ✅                                                      |
| `is` / `is not` identity narrowing        | ✅                                                      |
| Truthiness narrowing                      | ✅                                                      |
| `assert` narrowing                        | ✅                                                      |
| `match` statement narrowing               | ✅                                                      |
| `hasattr()` narrowing                     | ✅                                                      |
| `callable()` narrowing                    | ✅                                                      |
| Assignment narrowing                      | ✅                                                      |
| `TypeIs[…]` user-defined type guards      | ✅                                                      |
| `TypeGuard[…]` user-defined type guards   | ⚠️ partial (no narrowing applied yet)                   |
| `TypeIs`/`TypeGuard` as method            | ❌ [#1569](https://github.com/astral-sh/ty/issues/1569) |

## Special types and type qualifiers

[Official documentation](https://typing.python.org/en/latest/spec/special-types.html)

| Feature                                           | Status |
| ------------------------------------------------- | ------ |
| `Any`                                             | ✅     |
| `None`                                            | ✅     |
| `NoReturn`, `Never`                               | ✅     |
| `object`                                          | ✅     |
| `Literal[...]` (strings, ints, bools, enum, None) | ✅     |
| `LiteralString`                                   | ✅     |
| `Callable[[...], R]`                              | ✅     |
| `Callable[..., R]` (arbitrary arguments)          | ✅     |
| `Callable` with `ParamSpec`                       | ✅     |
| `type[C]`                                         | ✅     |
| `Final`, `Final[T]`                               | ✅     |
| `@final` decorator                                | ✅     |
| `ClassVar`, `ClassVar[T]`                         | ✅     |
| `InitVar[T]` (see Dataclasses)                    | ✅     |
| `Annotated[T, ...]`                               | ✅     |
| `Required[T]`, `NotRequired[T]` (see TypedDict)   | ✅     |
| `ReadOnly[T]` (see TypedDict)                     | ✅     |
| `Union[X, Y]`, \`X                                | Y\`    |
| `Optional[X]`                                     | ✅     |

## Type aliases

[Official documentation](https://typing.python.org/en/latest/spec/aliases.html)

| Feature                                                 | Status                                                              |
| ------------------------------------------------------- | ------------------------------------------------------------------- |
| Implicit type aliases (`Alias = int`)                   | ✅                                                                  |
| PEP 613 `TypeAlias` annotation                          | ✅                                                                  |
| PEP 695 `type` statement                                | ✅                                                                  |
| Generic type aliases (PEP 695)                          | ⚠️ limitations [#1851](https://github.com/astral-sh/ty/issues/1851) |
| Generic implicit/PEP 613 aliases                        | ⚠️ partial [#1739](https://github.com/astral-sh/ty/issues/1739)     |
| Self-referential generic aliases                        | ❌ [#1738](https://github.com/astral-sh/ty/issues/1738)             |
| `TypeAliasType` introspection (`__name__`, `__value__`) | ✅                                                                  |

## Type checker directives

[Official documentation](https://typing.python.org/en/latest/spec/directives.html)

| Feature                     | Status |
| --------------------------- | ------ |
| `cast(T, value)`            | ✅     |
| `assert_type(value, T)`     | ✅     |
| `assert_never(value)`       | ✅     |
| `reveal_type(value)`        | ✅     |
| `TYPE_CHECKING` constant    | ✅     |
| `no_type_check` decorator   | ✅     |
| `type: ignore` comments     | ✅     |
| `@deprecated` decorator     | ✅     |
| `@override` decorator       | ✅     |
| Redundant `cast` diagnostic | ✅     |

## Invalid overrides

(Liskov Substitution Principle)

| Feature                                      | Status |
| -------------------------------------------- | ------ |
| Covariant return types                       | ✅     |
| Contravariant parameter types                | ✅     |
| Invariant mutable attributes                 | ✅     |
| Full class hierarchy checked                 | ✅     |
| Positional/keyword parameter kind changes    | ✅     |
| Additional optional parameters               | ✅     |
| `*args`/`**kwargs` compatibility             | ✅     |
| `@staticmethod` and `@classmethod` overrides | ✅     |
| Synthesized method overrides (dataclasses)   | ✅     |
