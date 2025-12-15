# ty

An extremely fast Python type checker and language server, written in Rust.

<!-- TODO
## Highlights

- ...
-->

## Getting started

Run ty with [uvx](https://docs.astral.sh/uv/guides/tools/#running-tools) to get started quickly:

```shell
uvx ty check
```

!!! note

    ty will run on all Python files in the working directory and or subdirectories. If used from a
    project, ty will run on all Python files in the project (starting in the directory with the
    `pyproject.toml`).

You can also provide specific paths to check:

```shell
uvx ty check example.py
```

!!! note

    When type checking, ty will find installed packages in the active virtual environment (via
    `VIRTUAL_ENV`) or discover a virtual environment named `.venv` in the project root or working
    directory. It will not find packages in non-virtual environments without specifying the target
    path with `--python`. See the [module discovery](./modules.md) documentation for
    details.

## Installation

To install ty, see the [installation](./installation.md) documentation.

To add ty language server to your editor, see the [editors](./editors.md) documentation.

## Playground

ty has an [online playground](https://play.ty.dev) you can use to try it out on snippets or small
projects.

!!! tip

    The playground is a great way to share snippets with other people, e.g., when sharing a bug
    report.
