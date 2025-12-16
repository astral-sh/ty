# ty

An extremely fast Python type checker and language server, written in Rust.

ty is backed by [Astral](https://astral.sh), the creators of
[uv](https://github.com/astral-sh/uv) and [Ruff](https://github.com/astral-sh/ruff).

## Highlights

- 10x - 100x faster than mypy and Pyright
- Comprehensive and helpful diagnostics
- Configurable rule levels, per-file overrides, suppression comments, and first-class project support
- Designed for adoption, with support for redeclarations and partially typed code
- Language server with code navigation, completions, code actions, auto-import, inlay hints, on-hover help, etc.
- Fine-grained incremental analysis designed for fast updates when editing files in an IDE
- Editor integrations for VS Code, PyCharm, and more
- Advanced typing features like first-class intersection types, advanced type narrowing, and
    type-driven reachability analysis

## Getting started

Run ty with [uvx](https://docs.astral.sh/uv/guides/tools/#running-tools) to get started quickly:

```shell
uvx ty check
```

ty will check all Python files in the working directory or project by default.

See the [type checking](./type-checking.md) documentation for more details.

## Installation

To install ty, see the [installation](./installation.md) documentation.

To add the ty language server to your editor, see the [editors](./editors.md) documentation.

## Playground

ty has an [online playground](https://play.ty.dev) you can use to try it out on snippets or small
projects.

!!! tip

    The playground is a great way to share snippets with other people, e.g., when sharing a bug
    report.
