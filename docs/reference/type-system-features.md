<!-- markdownlint-disable -->

# Type system features

This page summarizes the support for various type system features in ty. Sections are organized to
follow the structure of the [Python typing specification](https://typing.python.org/en/latest/spec/),
with some additional sections at the end.

## Special types and type qualifiers

[Official documentation](https://typing.python.org/en/latest/spec/special-types.html)

| Feature                                           | Status                                                |
| ------------------------------------------------- | ----------------------------------------------------- |
| `Any`                                             | ✅                                                    |
| `None`                                            | ✅                                                    |
| `NoReturn`, `Never`                               | ✅                                                    |
| `object`                                          | ✅                                                    |
| `Literal[...]` (strings, ints, bools, enum, None) | ✅                                                    |
| `LiteralString`                                   | ✅                                                    |
| `type[C]`                                         | ✅                                                    |
| `Final`, `Final[T]`                               | ✅                                                    |
| Diagnostic: subclass overrides `Final` attribute  | ❌ [#871](https://github.com/astral-sh/ty/issues/871) |
| Diagnostic: `Final` without binding               | ❌ [#872](https://github.com/astral-sh/ty/issues/872) |
| `@final` decorator                                | ✅                                                    |
| `@disjoint_base` decorator                        | ✅                                                    |
| `ClassVar`, `ClassVar[T]`                         | ✅                                                    |
| Diagnostic: `ClassVar` with type variable         | ❌ [#518](https://github.com/astral-sh/ty/issues/518) |
| `type()` functional syntax                        | ❌ [#740](https://github.com/astral-sh/ty/issues/740) |
| `InitVar[T]` (see Dataclasses)                    | ✅                                                    |
| `Annotated[T, ...]`                               | ✅                                                    |
| `Required[T]`, `NotRequired[T]` (see TypedDict)   | ✅                                                    |
| `ReadOnly[T]` (see TypedDict)                     | ✅                                                    |
| `Union[X, Y]`, `X \| Y`                           | ✅                                                    |
| `Optional[X]`                                     | ✅                                                    |

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
| `ParamSpec` defaults                              | ✅                                                                       |
| `TypeVarTuple`                                    | ❌ [#156](https://github.com/astral-sh/ty/issues/156)                    |
| `Self`                                            | ✅                                                                       |
| `Self` in attribute annotations                   | ❌ [#1124](https://github.com/astral-sh/ty/issues/1124)                  |
| Generic bounds/constraints on type variables      | ❌ [#1839](https://github.com/astral-sh/ty/issues/1839)                  |
| `ParamSpec` usage validation                      | ❌ [#1861](https://github.com/astral-sh/ty/issues/1861)                  |

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
| Modules as protocol implementations           | ⚠️ [#931](https://github.com/astral-sh/ty/issues/931)           |
| `@classmethod` and `@staticmethod` members    | ❌ [#1381](https://github.com/astral-sh/ty/issues/1381)         |
| `ClassVar` members                            | ❌ [#1380](https://github.com/astral-sh/ty/issues/1380)         |
| `type[SomeProtocol]`                          | ❌ [#903](https://github.com/astral-sh/ty/issues/903)           |
| `issubclass()` on protocols with non-methods  | ❌ [#1878](https://github.com/astral-sh/ty/issues/1878)         |

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
| `TypeGuard[…]` user-defined type guards   | ❌ [#117](https://github.com/astral-sh/ty/issues/117)   |
| `TypeIs`/`TypeGuard` as method            | ❌ [#1569](https://github.com/astral-sh/ty/issues/1569) |
| Tuple length checks                       | ❌ [#560](https://github.com/astral-sh/ty/issues/560)   |
| Tuple match case narrowing                | ❌ [#561](https://github.com/astral-sh/ty/issues/561)   |

## Tuples

[Official documentation](https://typing.python.org/en/latest/spec/tuples.html)

| Feature                                                     | Status                                                  |
| ----------------------------------------------------------- | ------------------------------------------------------- |
| `tuple[X, Y, Z]` heterogeneous tuples                       | ✅                                                      |
| `tuple[X, ...]` homogeneous tuples                          | ✅                                                      |
| `tuple[()]` empty tuple                                     | ✅                                                      |
| Mixed tuples (`tuple[X, *tuple[Y, ...]]`)                   | ✅                                                      |
| Indexing with literal integers                              | ✅                                                      |
| Diagnostic: index out of bounds                             | ✅                                                      |
| Slicing tuples                                              | ✅                                                      |
| Tuple subclasses                                            | ✅                                                      |
| `typing.Tuple` (deprecated alias)                           | ✅                                                      |
| Covariant element types                                     | ✅                                                      |
| Tuple inheritance                                           | ✅                                                      |
| Unpacking in assignments                                    | ✅                                                      |
| `*args` unpacking in calls                                  | ⚠️ [#891](https://github.com/astral-sh/ty/issues/891)   |
| Diagnostic: invalid comparisons for non-fixed-length tuples | ❌ [#1741](https://github.com/astral-sh/ty/issues/1741) |
| `TypeVarTuple` / `Unpack`                                   | ❌ [#156](https://github.com/astral-sh/ty/issues/156)   |

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

## Literals

[Official documentation](https://typing.python.org/en/latest/spec/literal.html)

| Feature                                 | Status |
| --------------------------------------- | ------ |
| `Literal[0]` (integer literals)         | ✅     |
| `Literal["a"]` (string literals)        | ✅     |
| `Literal[b"a"]` (bytes literals)        | ✅     |
| `Literal[True]` (boolean literals)      | ✅     |
| `Literal[Color.RED]` (enum literals)    | ✅     |
| `Literal[None]`                         | ✅     |
| Nested `Literal` flattening             | ✅     |
| Union of literals simplification        | ✅     |
| `Literal` with type aliases             | ✅     |
| Invalid form diagnostics                | ✅     |
| `LiteralString`                         | ✅     |
| `LiteralString` assignability           | ✅     |
| `LiteralString` narrowing               | ✅     |
| `LiteralString` cannot be parameterized | ✅     |
| `LiteralString` cannot be subclassed    | ✅     |

## Callables

[Official documentation](https://typing.python.org/en/latest/spec/callables.html)

| Feature                                    | Status                                                  |
| ------------------------------------------ | ------------------------------------------------------- |
| `Callable[[X, Y], R]` syntax               | ✅                                                      |
| `Callable[..., R]` gradual form            | ✅                                                      |
| `Callable` with `ParamSpec`                | ✅                                                      |
| Callback protocols (`__call__` method)     | ✅                                                      |
| Callable assignability (contra/covariance) | ✅                                                      |
| Nested `Callable` types                    | ✅                                                      |
| `Callable` in unions/intersections         | ✅                                                      |
| Invalid form diagnostics                   | ✅                                                      |
| `Concatenate`                              | ❌ [#1535](https://github.com/astral-sh/ty/issues/1535) |
| `Unpack` for `**kwargs` typing             | ❌ [#1746](https://github.com/astral-sh/ty/issues/1746) |

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
| Variadic parameters with generics                      | ⚠️ [#1825](https://github.com/astral-sh/ty/issues/1825)            |
| Unannotated implementation validation                  | ⚠️ not tested [#1232](https://github.com/astral-sh/ty/issues/1232) |
| Diagnostic: overlapping overloads                      | ❌ [#103](https://github.com/astral-sh/ty/issues/103)              |
| Implementation consistency check                       | ❌ [#109](https://github.com/astral-sh/ty/issues/109)              |
| `@overload` with other decorators                      | ⚠️ [#1675](https://github.com/astral-sh/ty/issues/1675)            |

## Dataclasses

[Official documentation](https://typing.python.org/en/latest/spec/dataclasses.html)

| Feature                                                                                                                           | Status                                                  |
| :-------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------ |
| `@dataclass` decorator (`init`, `repr`, `eq`, `order`, `frozen`, `match_args`, `kw_only`, `slots`, `weakref_slot`, `unsafe_hash`) | ✅                                                      |
| `field()` (`default`, `default_factory`, `init`, `kw_only`, `doc`, `repr`, `hash`, `compare`)                                     | ✅                                                      |
| `InitVar[…]`, `ClassVar[…]` exclusion, `KW_ONLY` sentinel                                                                         | ✅                                                      |
| `fields()`, `__dataclass_fields__`                                                                                                | ✅                                                      |
| `Final` fields                                                                                                                    | ✅                                                      |
| Inheritance, generic dataclasses, descriptor-typed fields                                                                         | ✅                                                      |
| `replace()`, `__replace__`                                                                                                        | ⚠️ `__replace__` works, `replace()` returns `Unknown`   |
| `asdict()`                                                                                                                        | ⚠️ incorrectly accepts class objects                    |
| `astuple()`                                                                                                                       | ⚠️ not tested                                           |
| `make_dataclass()`, `is_dataclass()`                                                                                              | ⚠️ not tested                                           |
| Diagnostic: frozen/non-frozen dataclass inheritance                                                                               | ✅                                                      |
| Diagnostic: non-default field after default field                                                                                 | ❌ [#111](https://github.com/astral-sh/ty/issues/111)   |
| Diagnostic: `order=True` with custom comparison methods                                                                           | ❌ [#111](https://github.com/astral-sh/ty/issues/111)   |
| Diagnostic: `frozen=True` with `__setattr__`/`__delattr__`                                                                        | ❌ [#111](https://github.com/astral-sh/ty/issues/111)   |
| `__post_init__` signature validation                                                                                              | ❌ [#111](https://github.com/astral-sh/ty/issues/111)   |
| Diagnostic: unsound subclassing of `order=True` dataclasses                                                                       | ❌ [#1681](https://github.com/astral-sh/ty/issues/1681) |

## `dataclass_transform`

[Official documentation](https://typing.python.org/en/latest/spec/dataclasses.html#dataclass-transform)

| Feature                                                                                  | Status                                                  |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Function-based, metaclass-based, base-class-based transformers                           | ✅                                                      |
| `eq_default`, `order_default`, `kw_only_default` parameters                              | ✅                                                      |
| `frozen_default` parameter                                                               | ⚠️ metaclass override not working                       |
| `field_specifiers` (`init`, `default`, `default_factory`, `factory`, `kw_only`, `alias`) | ✅                                                      |
| `field_specifiers` (`converter`)                                                         | ❌ [#1327](https://github.com/astral-sh/ty/issues/1327) |

## Constructors

[Official documentation](https://typing.python.org/en/latest/spec/constructors.html)

| Feature                                       | Status                                                  |
| --------------------------------------------- | ------------------------------------------------------- |
| `__init__` signature inference                | ✅                                                      |
| `__new__` signature inference                 | ✅                                                      |
| Constructor inheritance from superclass       | ✅                                                      |
| Both `__new__` and `__init__` present         | ✅                                                      |
| Descriptor-based `__new__`/`__init__`         | ✅                                                      |
| Generic class constructor inference           | ✅                                                      |
| Type variable solving from constructor params | ✅                                                      |
| Custom `__new__` return type                  | ❌ [#281](https://github.com/astral-sh/ty/issues/281)   |
| Custom metaclass `__call__`                   | ❌                                                      |
| `__new__`/`__init__` consistency validation   | ❌                                                      |
| Diagnostic: explicit `__init__` on instance   | ❌ [#1016](https://github.com/astral-sh/ty/issues/1016) |

## Type aliases

[Official documentation](https://typing.python.org/en/latest/spec/aliases.html)

| Feature                                                 | Status                                                              |
| ------------------------------------------------------- | ------------------------------------------------------------------- |
| Implicit type aliases (`Alias = int`)                   | ✅                                                                  |
| PEP 613 `TypeAlias` annotation                          | ⚠️ fully stringified RHS not supported                              |
| PEP 695 `type` statement                                | ✅                                                                  |
| Generic type aliases (PEP 695)                          | ⚠️ limitations [#1851](https://github.com/astral-sh/ty/issues/1851) |
| Generic implicit/PEP 613 aliases                        | ⚠️ partial [#1739](https://github.com/astral-sh/ty/issues/1739)     |
| Self-referential generic aliases                        | ❌ [#1738](https://github.com/astral-sh/ty/issues/1738)             |
| `TypeAliasType` introspection (`__name__`, `__value__`) | ✅                                                                  |

## Type checker directives

[Official documentation](https://typing.python.org/en/latest/spec/directives.html)

| Feature                                            | Status                                                |
| -------------------------------------------------- | ----------------------------------------------------- |
| `cast(T, value)`                                   | ✅                                                    |
| `assert_type(value, T)`                            | ✅                                                    |
| `assert_never(value)`                              | ✅                                                    |
| `reveal_type(value)`                               | ✅                                                    |
| `TYPE_CHECKING` constant                           | ✅                                                    |
| `no_type_check` decorator                          | ✅                                                    |
| `type: ignore` comments                            | ✅                                                    |
| `@deprecated` decorator                            | ✅                                                    |
| `@override` decorator                              | ✅                                                    |
| Diagnostic: override without `@override` decorator | ❌ [#155](https://github.com/astral-sh/ty/issues/155) |
| Redundant `cast` diagnostic                        | ✅                                                    |

## Module resolution

[Official documentation](https://typing.python.org/en/latest/spec/distributing.html)

| Feature                                           | Status                                                  |
| ------------------------------------------------- | ------------------------------------------------------- |
| Stub files (`.pyi`)                               | ✅                                                      |
| Stub packages (`<package>-stubs`)                 | ✅                                                      |
| Partial stub packages (`py.typed` with `partial`) | ✅                                                      |
| Namespace packages (PEP 420)                      | ✅                                                      |
| Relative imports                                  | ✅                                                      |
| `__all__` declarations                            | ✅                                                      |
| `__all__` mutations (`.append`, `.extend`, `+=`)  | ✅                                                      |
| `__all__` with submodule `__all__`                | ✅                                                      |
| Wildcard (`*`) imports                            | ✅                                                      |
| Wildcard imports in stubs re-export               | ✅                                                      |
| Re-export conventions (`import X as X`)           | ✅                                                      |
| Conditional re-exports in stub files              | ✅                                                      |
| Reachability constraints in imports               | ✅                                                      |
| Cyclic imports                                    | ✅                                                      |
| `py.typed` marker files                           | ✅                                                      |
| `conftest.py` resolution (pytest)                 | ⚠️ [#414](https://github.com/astral-sh/ty/issues/414)   |
| Compiled extensions (`.so` files)                 | ❌ [#715](https://github.com/astral-sh/ty/issues/715)   |
| conda/pixi environment support                    | ❌ [#265](https://github.com/astral-sh/ty/issues/265)   |
| Per-library import suppression                    | ❌ [#1354](https://github.com/astral-sh/ty/issues/1354) |

## Control flow analysis

| Feature                                      | Status                                                                      |
| -------------------------------------------- | --------------------------------------------------------------------------- |
| Terminal statements (`return`, `raise`)      | ✅                                                                          |
| Loop control flow (`break`, `continue`)      | ✅                                                                          |
| `for`/`while` loop analysis                  | ✅                                                                          |
| `try`/`except`/`else`/`finally` control flow | ⚠️ `finally` limitations [#233](https://github.com/astral-sh/ty/issues/233) |
| `Never`/`NoReturn` function propagation      | ✅                                                                          |
| Exhaustiveness checking (`if`/`elif`/`else`) | ✅                                                                          |
| Exhaustiveness checking (`match`)            | ✅                                                                          |
| Advanced `match` pattern inference           | ❌ [#887](https://github.com/astral-sh/ty/issues/887)                       |
| `assert_never()`                             | ✅                                                                          |
| `sys.version_info` comparisons               | ✅                                                                          |
| `sys.platform` checks                        | ✅                                                                          |
| Statically known branches                    | ✅                                                                          |
| Walrus operator in boolean expressions       | ❌ [#626](https://github.com/astral-sh/ty/issues/626)                       |
| Cyclic control flow (loop back edges)        | ❌ [#232](https://github.com/astral-sh/ty/issues/232)                       |
| Gray out unreachable code                    | ❌ [#784](https://github.com/astral-sh/ty/issues/784)                       |

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
| Method overridden by non-method              | ❌     |
| Non-method overridden by non-method          | ❌     |

## Abstract base classes

| Feature                                       | Status                                                  |
| --------------------------------------------- | ------------------------------------------------------- |
| `@abstractmethod` decorator                   | ✅                                                      |
| Empty body allowed for abstract methods       | ✅                                                      |
| `@abstractmethod` with `@overload` validation | ✅                                                      |
| Diagnostic: instantiating abstract class      | ❌ [#1877](https://github.com/astral-sh/ty/issues/1877) |

## `__slots__`

| Feature                                                 | Status                                                  |
| ------------------------------------------------------- | ------------------------------------------------------- |
| `__slots__` (string or tuple of strings)                | ✅                                                      |
| `__slots__` (list, dict, set literals)                  | ❌                                                      |
| Attribute resolution from `__slots__`                   | ❌ [#1268](https://github.com/astral-sh/ty/issues/1268) |
| Diagnostic: access outside `__slots__`                  | ❌ [#1268](https://github.com/astral-sh/ty/issues/1268) |
| Diagnostic: class variable shadowing `__slots__` name   | ❌ [#1268](https://github.com/astral-sh/ty/issues/1268) |
| `__dict__`/`__weakref__` presence validation            | ❌ [#1268](https://github.com/astral-sh/ty/issues/1268) |
| Diagnostic: non-empty `__slots__` on builtin subclasses | ❌ [#1268](https://github.com/astral-sh/ty/issues/1268) |

## Standard library

| Feature                    | Status                                                  |
| -------------------------- | ------------------------------------------------------- |
| `@cached_property`         | ❌ [#1446](https://github.com/astral-sh/ty/issues/1446) |
| `functools.partial`        | ❌ [#1536](https://github.com/astral-sh/ty/issues/1536) |
| `functools.total_ordering` | ❌ [#1202](https://github.com/astral-sh/ty/issues/1202) |
