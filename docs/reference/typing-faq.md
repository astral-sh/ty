# Typing FAQ

This page answers some commonly asked questions about ty and Python's type system.

## What is the `Unknown` type and when does it appear?

`Unknown` is ty's way of representing a type that could not be fully inferred. It behaves the same
way as `Any`, but appears implicitly, rather than through an explicit `Any` annotation:

```py
from missing_module import MissingClass  # error: unresolved-import

reveal_type(MissingClass)  # Unknown
```

ty also uses unions with `Unknown` to maintain the
[gradual guarantee](../features/type-system.md#gradual-guarantee), which helps avoid false positive
errors in untyped code while still providing useful type information where possible.

For example, consider the following untyped `Message` class (which could come from a third-party
dependency that you have no control over). ty treats the `data` attribute as having type
`Unknown | None`, since there is no type annotation that restricts it further. The `Unknown` in the
union allows ty to avoid raising errors on the `msg.data = …` assignment. On the other hand, the
`None` in the union reflects the fact that `data` *could* possibly be `None`, and requires code that
uses `msg.data` to handle that case explicitly.

```py
class Message:
    data = None

    def __init__(self, title):
        self.title = title


def receive(msg: Message):
    reveal_type(msg.data)  # Unknown | None


msg = Message("Favorite color")
msg.data = {"color": "blue"}
```

([Full example in the playground](https://play.ty.dev/862941a8-a3f6-4818-9ea1-d9d59b0bd2fa))

## Why does ty show `int | float` when I annotate something as `float`?

The [Python typing specification](https://typing.python.org/en/latest/spec/special-types.html)
includes a special rule for numeric types where an `int` can be used wherever a `float` is expected:

```py
def circle_area(radius: float) -> float:
    return 3.14 * radius * radius

circle_area(2)      # OK: int is allowed where float is expected
```

This rule is a special case, since `int` is not actually a subclass of `float`. To support this, ty
treats `float` annotations as meaning `int | float`. Unlike some other type checkers, ty makes this
behavior explicit in type hints and error messages. For example, if you
[hover over the `radius` parameter](https://play.ty.dev/fdc144c6-031c-4af9-b520-a4c6ccde9261), ty
will show `int | float`.

A similar rule applies to `complex`, which is treated as `int | float | complex`.

!!! info

    These special rules for `float` and `complex` exist for a reason. In almost all cases, you
    probably want to accept both `int` and `float` when you annotate something as `float`.
    If you really need to accept *only* `float` and not `int`, you can use ty's `JustFloat`
    type. At the time of writing, this import needs to be guarded by a `TYPE_CHECKING` block:

    ```py
    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from ty_extensions import JustFloat
    else:
        JustFloat = float

    def only_actual_floats_allowed(f: JustFloat) -> None: ...

    only_actual_floats_allowed(1.0)  # OK
    only_actual_floats_allowed(1)    # error: invalid-argument-type
    ```

    ([Full example in the playground](https://play.ty.dev/fb034780-3ba7-4c6a-9449-5b0f44128bab))

    If you need this for `complex`, you can use `ty_extensions.JustComplex` in a similar way.

## Does ty have a strict mode?

Not yet. A stricter inference mode is tracked in
[this issue](https://github.com/astral-sh/ty/issues/1240). In the meantime, you can consider using Ruff's
[`flake8-annotations` rules](https://docs.astral.sh/ruff/rules/#flake8-annotations-ann) to enforce
more explicit type annotations in your code.

## Why can't ty resolve my imports?

Import resolution issues are often caused by a missing or incorrect environment configuration. When
ty reports *"Cannot resolve imported module …"*, check the following:

1. **Virtual environment**: Make sure your virtual environment is discoverable. ty looks for an
    active virtual environment via `VIRTUAL_ENV` or a `.venv` directory in your project root. See the
    [module discovery](../modules.md#python-environment) documentation for more details.

1. **Project structure**: If your source code is not in the project root or `src/` directory,
    configure [`environment.root`](./configuration.md#root) in your `pyproject.toml`:

    ```toml
    [tool.ty.environment]
    root = ["./app"]
    ```

1. **Third-party packages**: Ensure dependencies are installed in your virtual environment. Run ty
    with `-v` to see the search paths being used.

1. **Compiled extensions**: ty requires `.py` or `.pyi` files for type information. If a package
    contains only compiled extensions (`.so` or `.pyd` files), you'll need stub files (`.pyi`) for ty
    to understand the types. See also [this issue](https://github.com/astral-sh/ty/issues/487) which
    tracks improvements in this area.

## Does ty support monorepos?

ty can work with monorepos, but automatic discovery of nested projects is limited. By default, ty
uses the current working directory or the `--project` option to determine the project root.

For monorepos with multiple Python packages, you have a few options:

1. **Run ty per-package**: Run `ty check` from each package directory, or use `--project` to specify
    the package:

    ```bash
    ty check --project packages/package-a
    ty check --project packages/package-b
    ```

1. **Configure multiple source roots**: Use [`environment.root`](./configuration.md#root) to specify
    multiple source directories:

    ```toml
    [tool.ty.environment]
    root = ["packages/package-a", "packages/package-b"]
    ```

    This has the disadvantage of treating all packages as a single project, which may lead to cases
    in which ty thinks something is importable when it wouldn't be at runtime.

You can follow [this issue](https://github.com/astral-sh/ty/issues/819) to get updates on this
topic.

## Does ty support PEP 723 inline-metadata scripts?

It depends on what you want to do. If you have a single inline-metadata script, you can type check
it with ty by using uv's `--with-requirements` flag to install the dependencies specified in the
script header:

```bash
uvx --with-requirements script.py ty check script.py
```

If you have multiple scripts in your workspace, ty does not yet recognize that they have different
dependencies based on their inline metadata.

You can follow [this issue](https://github.com/astral-sh/ty/issues/691) for updates.

## Is there a pre-commit hook for ty?

Not yet. You can track progress in [this issue](https://github.com/astral-sh/ty/issues/269), which
also includes some suggested manual hooks you can use in the meantime.

## Does ty support (mypy) plugins?

No. ty does not have a plugin system and there is currently no plan to add one.

We prefer extending the type system with well-specified features rather than relying on
type-checker-specific plugins. That said, we are considering adding support for popular third-party
libraries like pydantic, SQLAlchemy, attrs, or django directly into ty.
