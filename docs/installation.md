# Installing ty

## Adding ty to your project

!!! tip

    Adding ty as a dependency ensures that all developers on the project are using the same version
    of ty.

Use [uv](https://github.com/astral-sh/uv) (or your project manager of choice) to add ty as a
development dependency:

```shell
uv add --dev ty
```

Then, use `uv run` to invoke ty:

```shell
uv run ty
```

## Installing globally

Install ty globally with uv:

```shell
uv tool install ty@latest
```

Or, pipx:

```shell
pipx install ty
```

## Installing with pip

Install ty into your current Python environment with pip:

```shell
pip install ty
```

## Adding ty to your editor

See the [editor integration](./editors.md) guide to add ty to your editor.
