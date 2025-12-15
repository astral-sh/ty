# Type system features

This page summarizes the support for various type system features in ty. Sections are organized to follow the structure of the [Python typing specification](https://typing.python.org/en/latest/spec/), with some additional sections at the end.

## Special types and type qualifiers

[Official documentation](https://typing.python.org/en/latest/spec/special-types.html)

**tests:** [`any.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/annotations/any.md), [`never.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/annotations/never.md), [`int_float_complex.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/annotations/int_float_complex.md), [`final.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/type_qualifiers/final.md), [`classvar.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/type_qualifiers/classvar.md), [`annotated.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/annotations/annotated.md), [`union.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/annotations/union.md), [`instance_layout_conflict.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/instance_layout_conflict.md)

- [x] `Any`
- [x] `None`
- [x] `NoReturn`, `Never`
- [x] `object`
- [x] `Literal[...]` (strings, ints, bools, enum, None)
- [x] `LiteralString`
- [x] `type[C]`
- [x] `float`/`complex` special cases (`float` means `int | float`)
- [x] `Final`, `Final[T]`
    - [ ] Diagnostic: subclass overrides `Final` attribute #871
    - [ ] Diagnostic: `Final` without binding #872
- [x] `@final` decorator
- [x] `@disjoint_base` decorator
- [x] `ClassVar`, `ClassVar[T]`
    - [ ] Diagnostic: `ClassVar` with type variable #518
- [ ] `type()` functional syntax #740
- [x] `InitVar[T]` (see Dataclasses)
- [x] `Annotated[T, ...]`
- [x] `Required[T]`, `NotRequired[T]` (see TypedDict)
- [x] `ReadOnly[T]` (see TypedDict)
- [x] `Union[X, Y]`, `X | Y`
- [x] `Optional[X]`

## Generics

[Official documentation](https://typing.python.org/en/latest/spec/generics.html)

**tests:** [`pep695/`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/generics/pep695/), [`legacy/`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/generics/legacy/), [`self.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/annotations/self.md), [`scoping.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/generics/scoping.md)

- [x] `TypeVar` (legacy syntax)
- [x] `TypeVar` (PEP 695 syntax: `def f[T]()`)
- [x] `TypeVar` upper bound (`bound=`)
- [x] `TypeVar` constraints
- [x] `TypeVar` defaults (PEP 696)
- [x] `TypeVar` variance (`covariant`, `contravariant`)
- [x] `TypeVar` variance inference (`infer_variance`)
- [x] Generic classes (legacy and PEP 695 syntax)
- [x] Generic functions (legacy and PEP 695 syntax)
- [x] Generic type aliases (PEP 695)
    - [ ] Some limitations #1851
- [x] `ParamSpec` (legacy and PEP 695 syntax)
- [x] `ParamSpec.args`, `ParamSpec.kwargs`
- [x] `ParamSpec` defaults
- [ ] `TypeVarTuple` #156
- [x] `Self`
- [ ] `Self` in attribute annotations #1124
- [ ] Generic bounds/constraints on type variables #1839
- [ ] `Callable`s in typevar solving
- [ ] Generic protocols in typevar solving #1714
- [ ] `ParamSpec` usage validation #1861

## Protocols

[Official documentation](https://typing.python.org/en/latest/spec/protocol.html)

**tests:** [`protocols.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/protocols.md)

- [x] `Protocol` class definition
- [x] Generic protocols (legacy and PEP 695 syntax)
- [x] Structural subtyping / assignability
- [x] Protocol inheritance
- [x] `is_protocol()`, `get_protocol_members()`
- [x] `@runtime_checkable` decorator
- [x] Protocol instantiation restriction
- [x] Non-protocol class inheritance restriction
- [x] `@property` members
    - [ ] Partial support #1379
- [ ] Modules as protocol implementations #931
- [ ] `@classmethod` and `@staticmethod` members #1381
- [ ] `ClassVar` members #1380
- [ ] `type[SomeProtocol]` #903
- [ ] `issubclass()` on protocols with non-methods #1878

## Type narrowing

[Official documentation](https://typing.python.org/en/latest/spec/narrowing.html)

**tests:** [`narrow/`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/narrow/), [`type_guards.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/narrow/type_guards.md)

- [x] `isinstance()` / `issubclass()` narrowing
- [x] `is None` / `is not None` narrowing
- [x] `is` / `is not` identity narrowing
- [x] Truthiness narrowing
- [x] `assert` narrowing
- [x] `match` statement narrowing
- [x] `hasattr()` narrowing
- [x] `callable()` narrowing
- [x] Assignment narrowing
- [x] `TypeIs[…]` user-defined type guards
- [ ] `TypeGuard[…]` user-defined type guards #117
- [ ] `TypeIs`/`TypeGuard` as method #1569
- [ ] Tuple length checks #560
- [ ] Tuple match case narrowing #561

## Tuples

[Official documentation](https://typing.python.org/en/latest/spec/tuples.html)

**tests:** [`subscript/tuple.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/subscript/tuple.md), [`comparison/tuples.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/comparison/tuples.md), [`binary/tuples.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/binary/tuples.md)

- [x] `tuple[X, Y, Z]` heterogeneous tuples
- [x] `tuple[X, ...]` homogeneous tuples
- [x] `tuple[()]` empty tuple
- [x] Mixed tuples (`tuple[X, *tuple[Y, ...]]`)
- [x] Indexing with literal integers
- [x] Diagnostic: index out of bounds
- [x] Slicing tuples
- [x] Tuple subclasses
- [x] `typing.Tuple` (deprecated alias)
- [x] Covariant element types
- [x] Tuple inheritance
- [x] Unpacking in assignments
- [x] `*args` unpacking in calls
- [ ] Diagnostic: invalid comparisons for non-fixed-length tuples #1741
- [ ] `TypeVarTuple` / `Unpack` #156

## `NamedTuple`

[Official documentation](https://typing.python.org/en/latest/spec/namedtuples.html)

**tests:** [`named_tuple.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/named_tuple.md)

- [x] Class syntax (`class Foo(NamedTuple): ...`)
- [x] Field access by name and index, slicing, unpacking
- [x] Default values, diagnostic for non-default after default
- [x] Read-only fields (assignment rejected)
- [x] Inheritance, generic `NamedTuple`s
- [x] Multiple inheritance restriction
- [x] Underscore field name restriction
- [x] Prohibited attribute override check (`_asdict`, `_make`, …)
- [x] `_fields`, `_field_defaults`, `_make`, `_asdict`, `_replace`
- [x] Subtype of `tuple[...]`
- [x] `super()` restriction in `NamedTuple` methods
- [x] `NamedTuple` in type expressions
- [ ] Functional syntax (`NamedTuple("Foo", [...])`) #1049
- [ ] `collections.namedtuple`: not tested
- [ ] Subclass field conflicting with base class field: not tested
- [x] `type[NamedTuple]` in type expressions
    - [ ] Not fully supported

## `TypedDict`

[Official documentation](https://typing.python.org/en/latest/spec/typeddict.html)

**tests:** [`typed_dict.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/typed_dict.md)

- [x] Class syntax (`class Foo(TypedDict): ...`)
- [x] Key access by literal string, `Final` constants
- [x] Constructor validation (missing keys, invalid types)
- [x] `total` parameter
- [x] `Required[…]`, `NotRequired[…]`
- [x] `ReadOnly[…]`
- [x] Inheritance, generic `TypedDict`s
- [x] Recursive `TypedDict`
- [x] Structural assignability and equivalence
- [x] Methods (`get`, `pop`, `setdefault`, `keys`, `values`, `copy`)
- [x] `__total__`, `__required_keys__`, `__optional_keys__`
- [ ] Functional syntax (`TypedDict("Foo", {...})`) #154
- [ ] `closed`, `extra_items` (PEP 728) #154
- [ ] `Unpack` for `**kwargs` typing #1746
- [ ] Tagged union narrowing #1479
- [ ] Diagnostic: Invalid `isinstance()` check on `TypedDict`: not tested

## Enums

[Official documentation](https://typing.python.org/en/latest/spec/enums.html)

**tests:** [`enums.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/enums.md), [`comparison/enums.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/comparison/enums.md)

- [x] `Enum`, `IntEnum`, `StrEnum`
- [x] `Literal[EnumMember]` types
- [x] `.name`, `.value` inference
- [x] `auto()` value inference
- [x] `member()`, `nonmember()`
- [x] Enum aliases
- [x] `_ignore_` attribute
    - [ ] List form not fully supported
- [x] Implicitly final (subclassing restriction)
- [x] Exhaustiveness checking (`if`/`match`)
- [x] Custom `__eq__`/`__ne__` methods
- [x] Iteration over enum members
    - [ ] `list(Enum)` returns `list[Unknown]`
- [ ] Functional syntax (`Enum("Name", [...])`) #876
- [ ] `enum.Flag` expansion handling #876
- [ ] Custom `__new__` or `__init__` methods #876
- [ ] `_generate_next_value_` support #876
- [ ] Value-based member retrieval (`Color("red")`) #876
- [ ] Narrowing with custom `__eq__` in `match` #1454

## Literals

[Official documentation](https://typing.python.org/en/latest/spec/literal.html)

**tests:** [`literal.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/annotations/literal.md), [`literal_string.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/annotations/literal_string.md)

- [x] `Literal[0]` (integer literals)
- [x] `Literal["a"]` (string literals)
- [x] `Literal[b"a"]` (bytes literals)
- [x] `Literal[True]` (boolean literals)
- [x] `Literal[Color.RED]` (enum literals)
- [x] `Literal[None]`
- [x] Nested `Literal` flattening
- [x] Union of literals simplification
- [x] `Literal` with type aliases
- [x] Invalid form diagnostics
- [x] `LiteralString`
- [x] `LiteralString` assignability
- [x] `LiteralString` narrowing
- [x] `LiteralString` cannot be parameterized
- [x] `LiteralString` cannot be subclassed

## Callables

[Official documentation](https://typing.python.org/en/latest/spec/callables.html)

**tests:** [`callable.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/annotations/callable.md), [`callable_instance.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/call/callable_instance.md)

- [x] `Callable[[X, Y], R]` syntax
- [x] `Callable[..., R]` gradual form
- [x] `Callable` with `ParamSpec`
- [x] Callback protocols (`__call__` method)
- [x] Callable assignability (contra/covariance)
- [x] Nested `Callable` types
- [x] `Callable` in unions/intersections
- [x] Invalid form diagnostics
- [ ] `Concatenate` #1535
- [ ] `Unpack` for `**kwargs` typing #1746

## Overloads

[Official documentation](https://typing.python.org/en/latest/spec/overload.html)

**tests:** [`overloads.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/overloads.md), [`call/overloads.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/call/overloads.md)

- [x] `@overload` decorator
- [x] Overload resolution
- [x] Generic overloads
- [x] Methods, constructors, `@staticmethod`, `@classmethod`
- [x] Version-specific overloads
- [x] Diagnostic: at least two overloads required
- [x] Diagnostic: missing implementation (non-stub)
- [x] Diagnostic: inconsistent decorators
- [x] Diagnostic: `@final`/`@override` placement
- [ ] Variadic parameters with generics #1825
- [ ] Unannotated implementation validation: not tested #1232
- [ ] Diagnostic: overlapping overloads #103
- [ ] Implementation consistency check #109
- [ ] `@overload` with other decorators #1675

## Dataclasses

[Official documentation](https://typing.python.org/en/latest/spec/dataclasses.html)

**tests:** [`dataclasses.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/dataclasses/dataclasses.md), [`fields.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/dataclasses/fields.md)

- [x] `@dataclass` decorator (`init`, `repr`, `eq`, `order`, `frozen`, `match_args`, `kw_only`, `slots`, `weakref_slot`, `unsafe_hash`)
- [x] `field()` (`default`, `default_factory`, `init`, `kw_only`, `doc`, `repr`, `hash`, `compare`)
- [x] `InitVar[…]`, `ClassVar[…]` exclusion, `KW_ONLY` sentinel
- [x] `fields()`, `__dataclass_fields__`
- [x] `Final` fields
- [x] Inheritance, generic dataclasses, descriptor-typed fields
- [x] `replace()`, `__replace__`
    - [ ] `replace()` returns `Unknown`
- [x] `asdict()`
    - [ ] Incorrectly accepts class objects
- [ ] `astuple()`: not tested
- [ ] `make_dataclass()`, `is_dataclass()`: not tested
- [x] Diagnostic: frozen/non-frozen dataclass inheritance
- [ ] Diagnostic: non-default field after default field #111
- [ ] Diagnostic: `order=True` with custom comparison methods #111
- [ ] Diagnostic: `frozen=True` with `__setattr__`/`__delattr__` #111
- [ ] `__post_init__` signature validation #111
- [ ] Diagnostic: unsound subclassing of `order=True` dataclasses #1681

## `dataclass_transform`

[Official documentation](https://typing.python.org/en/latest/spec/dataclasses.html#dataclass-transform)

**tests:** [`dataclass_transform.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/dataclasses/dataclass_transform.md)

- [x] Function-based, metaclass-based, base-class-based transformers
- [x] `eq_default`, `order_default`, `kw_only_default` parameters
- [x] `frozen_default` parameter
    - [ ] Metaclass override not working
- [x] `field_specifiers` (`init`, `default`, `default_factory`, `factory`, `kw_only`, `alias`)
- [ ] `field_specifiers` (`converter`) #1327

## Constructors

[Official documentation](https://typing.python.org/en/latest/spec/constructors.html)

**tests:** [`constructor.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/call/constructor.md)

- [x] `__init__` signature inference
- [x] `__new__` signature inference
- [x] Constructor inheritance from superclass
- [x] Both `__new__` and `__init__` present
- [x] Descriptor-based `__new__`/`__init__`
- [x] Generic class constructor inference
- [x] Type variable solving from constructor params
- [ ] Custom `__new__` return type #281
- [ ] Custom metaclass `__call__`
- [ ] `__new__`/`__init__` consistency validation
- [ ] Diagnostic: explicit `__init__` on instance #1016

## Type aliases

[Official documentation](https://typing.python.org/en/latest/spec/aliases.html)

**tests:** [`pep695_type_aliases.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/pep695_type_aliases.md), [`pep613_type_aliases.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/pep613_type_aliases.md), [`implicit_type_aliases.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/implicit_type_aliases.md)

- [x] Implicit type aliases (`Alias = int`)
- [x] PEP 613 `TypeAlias` annotation
    - [ ] Fully stringified RHS not supported
- [x] PEP 695 `type` statement
- [x] Generic type aliases (PEP 695)
    - [ ] Limitations #1851
- [x] Generic implicit/PEP 613 aliases
    - [ ] Partial support #1739
- [ ] Self-referential generic aliases #1738
- [x] `TypeAliasType` introspection (`__name__`, `__value__`)

## Type checker directives

[Official documentation](https://typing.python.org/en/latest/spec/directives.html)

**tests:** [`directives/`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/directives/)

- [x] `cast(T, value)`
- [x] `assert_type(value, T)`
- [x] `assert_never(value)`
- [x] `reveal_type(value)`
- [x] `TYPE_CHECKING` constant
- [x] `no_type_check` decorator
- [x] `type: ignore` comments
- [x] `@deprecated` decorator
- [x] `@override` decorator
- [ ] Diagnostic: override without `@override` decorator #155
- [x] Redundant `cast` diagnostic

## Module resolution

[Official documentation](https://typing.python.org/en/latest/spec/distributing.html)

**tests:** [`import/`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/import/)

- [x] Stub files (`.pyi`)
- [x] Stub packages (`<package>-stubs`)
- [x] Partial stub packages (`py.typed` with `partial`)
- [x] Namespace packages (PEP 420)
- [x] Relative imports
- [x] `__all__` declarations
- [x] `__all__` mutations (`.append`, `.extend`, `+=`)
- [x] `__all__` with submodule `__all__`
- [x] Wildcard (`*`) imports
- [x] Wildcard imports in stubs re-export
- [x] Re-export conventions (`import X as X`)
- [x] Conditional re-exports in stub files
- [x] Reachability constraints in imports
- [x] Cyclic imports
- [x] `py.typed` marker files
- [ ] `conftest.py` resolution (pytest) #414
- [ ] Compiled extensions (`.so` files) #715
- [ ] conda/pixi environment support #265
- [ ] Per-library import suppression #1354

## Control flow analysis

**tests:** [`terminal_statements.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/terminal_statements.md), [`exhaustiveness_checking.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/exhaustiveness_checking.md), [`unreachable.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/unreachable.md), [`exception/control_flow.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/exception/control_flow.md)

- [x] Terminal statements (`return`, `raise`)
- [x] Loop control flow (`break`, `continue`)
- [x] `for`/`while` loop analysis
- [x] `try`/`except`/`else`/`finally` control flow
    - [ ] `finally` limitations #233
- [x] `Never`/`NoReturn` function propagation
- [x] Exhaustiveness checking (`if`/`elif`/`else`)
- [x] Exhaustiveness checking (`match`)
- [ ] Advanced `match` pattern inference #887
- [x] `assert_never()`
- [x] `sys.version_info` comparisons
- [x] `sys.platform` checks
- [x] Statically known branches
- [ ] Walrus operator in boolean expressions #626
- [ ] Cyclic control flow (loop back edges) #232
- [ ] Gray out unreachable code #784

## Invalid overrides

(Liskov Substitution Principle)

**tests:** [`liskov.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/liskov.md), [`override.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/override.md)

- [x] Covariant return types
- [x] Contravariant parameter types
- [x] Invariant mutable attributes
- [x] Full class hierarchy checked
- [x] Positional/keyword parameter kind changes
- [x] Additional optional parameters
- [x] `*args`/`**kwargs` compatibility
- [x] `@staticmethod` and `@classmethod` overrides
- [x] Synthesized method overrides (dataclasses)
- [ ] Method overridden by non-method
- [ ] Non-method overridden by non-method

## Abstract base classes

**tests:** [`return_type.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/function/return_type.md), [`overloads.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/overloads.md)

- [x] `@abstractmethod` decorator
- [x] Empty body allowed for abstract methods
- [x] `@abstractmethod` with `@overload` validation
- [ ] Diagnostic: instantiating abstract class #1877

## `__slots__`

**tests:** [`instance_layout_conflict.md`](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/resources/mdtest/instance_layout_conflict.md)

- [x] `__slots__` (string or tuple of strings)
- [ ] `__slots__` (list, dict, set literals)
- [ ] Attribute resolution from `__slots__` #1268
- [ ] Diagnostic: access outside `__slots__` #1268
- [ ] Diagnostic: class variable shadowing `__slots__` name #1268
- [ ] `__dict__`/`__weakref__` presence validation #1268
- [ ] Diagnostic: non-empty `__slots__` on builtin subclasses #1268

## Standard library

- [ ] `@cached_property` #1446
- [ ] `functools.partial` #1536
- [ ] `functools.total_ordering` #1202
