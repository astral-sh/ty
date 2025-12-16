# ty

An extremely fast Python type checker and language server, written in Rust.

<p align="center">
  <img alt="Shows a bar chart with benchmark results." width="500px" src="./assets/ty-benchmark-cli.svg#only-light">
</p>

<p align="center">
  <img alt="Shows a bar chart with benchmark results." width="500px" src="./assets/ty-benchmark-cli-dark.svg#only-dark">
</p>

<p align="center">
  <i>Type checking the <a href="https://github.com/home-assistant/core">home-assistant</a> project without caching.</i>
</p>

ty is backed by [Astral](https://astral.sh), the creators of
[uv](https://github.com/astral-sh/uv) and [Ruff](https://github.com/astral-sh/ruff).

## Highlights

- 10x - 100x faster than mypy and Pyright
- Comprehensive [diagnostics](./features/diagnostics.md) with rich contextual information
- Configurable [rule levels](./rules.md), [per-file overrides](./reference/configuration.md#overrides), [suppression comments](./suppression.md), and first-class project support
- Designed for adoption, with support for [redeclarations](./features/type-system.md#redeclarations) and [partially typed code](./features/type-system.md#gradual-guarantee)
- [Language server](./features/language-server.md) with code navigation, completions, code actions, auto-import, inlay hints, on-hover help, etc.
- Fine-grained [incremental analysis](./features/language-server.md#fine-grained-incrementality) designed for fast updates when editing files in an IDE
- Editor integrations for [VS Code](./editors.md#vs-code), [PyCharm](./editors.md#pycharm), [Neovim](./editors.md#neovim) and more
- Advanced typing features like first-class [intersection types](./features/type-system.md#intersection-types), advanced [type narrowing](./features/type-system.md#top-and-bottom-materializations), and
    [sophisticated reachability analysis](./features/type-system.md#reachability-based-on-types)

## Getting started

Run ty with [uvx](https://docs.astral.sh/uv/guides/tools/#running-tools) to get started quickly:

```shell
uvx ty check
```

ty will check all Python files in the working directory or project by default.

See the [type checking](./type-checking.md) documentation for more details.

## Installation

To install ty, see the [installation](./installation.md) documentation.

To add the ty language server to your editor, see the [editor integration](./editors.md) guide.

## Playground

ty has an [online playground](https://play.ty.dev) you can use to try it out on snippets or small
projects.

!!! tip

    The playground is a great way to share snippets with other people, e.g., when sharing a bug
    report.
