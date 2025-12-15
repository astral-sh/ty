# Type checking

You can generally expect ty to support all typing features that are described and specified in the
[Python typing documentation] (for a detailed overview, please refer to the
[type system features tracking issue](https://github.com/astral-sh/ty/issues/1889)). This page
highlights some of the unique features that ty's type system provides.

## Redeclarations

ty allows you to reuse the same symbol with a different type. The following example shows how the
`paths` parameter is redeclared as a list of strings:

```py
def split_paths(paths: str) -> list[Path]:
    paths: list[str] = paths.split(":")
    return [Path(p) for p in paths]
```

(Full example in the [playground](https://play.ty.dev/80a74c95-a43e-4a3d-8c26-f88e879d7dcb))

## Intersection types

ty has first-class support for intersection types. In contrast to a union type `A | B`, which means
"*either* A *or* B", an intersection type `A & B` means "*both* A *and* B". Type narrowing in ty is
based on intersections. For example, notice how we can call `obj.serialize_json()` *and* access the
`.version` property in the following function:

```py
def output_as_json(obj: Serializable) -> str:
    if isinstance(obj, Versioned):
        reveal_type(obj)  # reveals: Serializable & Versioned

        return str({
            "data": obj.serialize_json(),
            "version": obj.version
        })
    else:
        return obj.serialize_json()
```

(Full example in the [playground](https://play.ty.dev/39241435-5e78-4ce9-817f-ce65be73a6ed))

Intersections can also be built using gradual types like `Any` or its implicit counterpart
`Unknown`. For example, imagine you call into untyped (third party) code that returns an object of
type `Unknown`. Narrowing the type of that object using `isinstance` will result in an intersection
type `Unknown & Iterable`. This type allows you to use `obj` as an iterable. But more importantly,
it still gives you access to attributes defined on the original unknown type (`.description`, in this
example):

```py
def print_content(data: bytes):
    obj = untyped_library.deserialize(data)

    if isinstance(obj, Iterable):
        print(obj.description)
        for part in obj:
            print("*", part.description)
    else:
        print(obj.description)
```

(Full example in the [playground](https://play.ty.dev/8f98820e-7306-4d69-b572-56d69a92b90f))

Intersection types are also used in `hasattr` narrowing. Take a look at the following example where
we narrow a type of `Person | Animal | None` using `hasattr(…, "name")`. `Person` is preserved in
the narrowed union type because it has a `name` attribute. `Animal` is intersected with a synthetic
protocol, accounting for the possibility of subclasses of `Animal` that add a `name` member.
`None` is excluded completely since it is a final type that has no `name` attribute:

```py
class Person:
    name: str

class Animal:
    species: str

def greet(being: Person | Animal | None):
    if hasattr(being, "name"):
        # `being` is now of type `Person | (Animal & <Protocol with members 'name'>)`

        print(f"Hello, {being.name}!")
    else:
        print("Hello there!")
```

(Full example in the [playground](https://play.ty.dev/31f2c718-516a-4a85-80e0-2a4682b818f1))

!!! info

    If you run into a situation like this and would like `Animal` to be excluded from the narrowed
    type as well, you can make `Animal` a `@final` class. This also allows ty to infer a more precise
    type for `being.name` (`str` instead of `object`).

If ty is the only type checker you use, you can also make direct use of intersection types in
annotations by importing `Intersection` from the special `ty_extensions` module that is (currently)
only available at type-checking time:

```py
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ty_extensions import Intersection

    type SerializableVersioned = Intersection[Serializable, Versioned]

def output_as_json(obj: SerializableVersioned) -> str:
    ...
```

(Full example in the [playground](https://play.ty.dev/f003e901-0e45-4f45-9759-d6db9d5e5f66))

## Top and bottom materializations

Gradual types generally have two special [materializations]. The top materialization represents the
"largest" type that a gradual type can materialize to: the union of all possible materializations.
For example, the top materialization of `Any` is `object`, and the top materialization of
`Any & int` is `int`. For invariant generic classes, the top materialization cannot be expressed in
Python's type system, but it is a useful type that ty intersects with when `isinstance` checks
involve generic classes. For example, when checking `isinstance(…, list)`, ty intersects with the
top materialization of `list[Unknown]`:

```py
@final
class Item: ...

def process(items: Item | list[Item]):
    if isinstance(items, list):
        # reveals: list[Item]
        reveal_type(items)
```

(Full example in the [playground](https://play.ty.dev/f1306120-0b8d-4ed5-b832-1f2d379eae2b))

!!! info

    You might wonder why `Item` is declared `@final` here. If we remove the `@final` decorator, the
    inferred type in the `if` branch becomes `(Item & Top[list[Unknown]]) | list[Item]` instead.
    This accounts for the possibility of classes that inherit from both `Item` *and* `list`! If
    you run into this situation and want to rule out this case, you can also perform the `isinstance`
    check against `Item` instead. The `else` branch will then have a narrowed type of
    `list[Item] & ~Item`, which effectively acts like `list[Item]`.

## Reachability based on types

Reachability analysis in ty is based on type inference. This allows ty to detect unreachable
branches in many more situations compared to approaches which match on a few known patterns (e.g.
`sys.version_info >= (3, 10)` checks). This has useful practical applications. Consider a case
where you are writing code that needs to be compatible with two major versions of a dependency.
The following code can be successfully type-checked with either pydantic 1.x installed, or pydantic
2.x installed. In both cases, ty will only consider the corresponding branch to be reachable, and
will not emit any type errors for the other branch. This works because
`pydantic.__version__.startswith("2.")` can be evaluated to `True` or `False` at type-checking time:

```py
import pydantic
from pydantic import BaseModel

PYDANTIC_V2 = pydantic.__version__.startswith("2.")

class Person(BaseModel):
    name: str

def to_json(person: Person):
    if PYDANTIC_V2:
        return person.model_dump_json()  # no error here when checking with 1.x
    else:
        return person.json()
```

(Full example in the [playground](https://play.ty.dev/34a227bb-93d5-405e-86c3-72f57ec5642e))

## Gradual guarantee

ty generally tries to avoid emitting false positive type errors in untyped code. The following
snippet does not produce any type errors when checked with ty (whereas other type checkers make the
assumption that `max_retries` is of type `None`, leading to an error in the attribute assignment):

```py
class RetryPolicy:
    max_retries = None

policy = RetryPolicy()
policy.max_retries = 1
```

(Full example in the [playground](https://play.ty.dev/a5286db1-cdfd-45e7-af54-29649ba5c423))

This is achieved by treating `max_retries` as being of type `Unknown | None`, which means that the
type of the attribute is not fully known, but `None` is definitely a possible value.

Users can always opt into stricter checking by adding type annotations (`int | None`, in this case).

!!! info

    We are also planning to add a mode for users that prefer to have stricter types inferred by default
    in these situations. You can follow [this issue](https://github.com/astral-sh/ty/issues/1240) for
    updates.

## Fixpoint iteration

In a situation where a symbol's type cyclically depends on itself, ty uses a mechanism called fixpoint iteration to
be able to infer a type for that symbol. In the `tick` method below, note how the type of `self.value` depends on
`self.value` itself. ty starts by assuming that `self.value` is just `Unknown | Literal[0]` (the type inferred
from the `__init__` method), and then iterates until the type converges to `Unknown | Literal[0, 1, 2, 3, 4]`.
Without the modulo operation, the union would grow indefinitely. In that case, we fall back to `int` after a certain
number of iterations.

```py
class LoopingCounter:
    def __init__(self):
        self.value = 0

    def tick(self):
        self.value = (self.value + 1) % 5

# reveals: Unknown | Literal[0, 1, 2, 3, 4]
reveal_type(LoopingCounter().value)
```

(Full example in the [playground](https://play.ty.dev/64400d96-ee1b-48f3-8361-b583dddddf82))

[materializations]: https://typing.python.org/en/latest/spec/concepts.html#materialization
[python typing documentation]: https://typing.python.org/
