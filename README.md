# ty

[![ty](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
[![PyPI](https://img.shields.io/pypi/v/ty.svg)](https://pypi.python.org/pypi/ty)
[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?logo=discord&logoColor=white)](https://discord.com/invite/astral-sh)

An extremely fast Python type checker and language server, written in Rust.

ty is backed by [Astral](https://astral.sh), the creators of
[uv](https://github.com/astral-sh/uv) and [Ruff](https://github.com/astral-sh/ruff).

## Highlights

- 10x - 100x faster than mypy and Pyright
- Comprehensive [diagnostics](https://docs.astral.sh/ty/features/diagnostics/) with rich contextual information
- Configurable [rule levels](https://docs.astral.sh/ty/rules/), [per-file overrides](https://docs.astral.sh/ty/reference/configuration/#overrides), [suppression comments](https://docs.astral.sh/ty/suppression/), and first-class project support
- Designed for adoption, with support for [redeclarations](https://docs.astral.sh/ty/features/type-system/#redeclarations) and [partially typed code](https://docs.astral.sh/ty/features/type-system/#gradual-guarantee)
- [Language server](https://docs.astral.sh/ty/features/language-server/) with code navigation, completions, code actions, auto-import, inlay hints, on-hover help, etc.
- Fine-grained incremental analysis designed for fast updates when editing files in an IDE
- Editor integrations for [VS Code](https://docs.astral.sh/ty/editors/#vs-code), [PyCharm](https://docs.astral.sh/ty/editors/#pycharm), [Neovim](https://docs.astral.sh/ty/editors/#neovim) and more
- Advanced typing features like first-class [intersection types](https://docs.astral.sh/ty/features/type-system/#intersection-types), advanced [type narrowing](https://docs.astral.sh/ty/features/type-system/#top-and-bottom-materializations), and
    [type-driven reachability analysis](https://docs.astral.sh/ty/features/type-system/#reachability-based-on-types)

## Getting started

Run ty with [uvx](https://docs.astral.sh/uv/guides/tools/#running-tools) to get started quickly:

```shell
uvx ty check
```

Or, check out the [ty playground](https://play.ty.dev) to try it out in your browser.

To learn more about using ty, see the [documentation](https://docs.astral.sh/ty/).

## Installation

To install ty, see the [installation](./installation.md) documentation.

To add the ty language server to your editor, see the [editor integration](./editors.md) guide.

## Getting help

If you have questions or want to report a bug, please open an
[issue](https://github.com/astral-sh/ty/issues) in this repository.

You may also join our [Discord server](https://discord.com/invite/astral-sh).

## Contributing

Development of this project takes place in the [Ruff](https://github.com/astral-sh/ruff) repository
at this time. Please [open pull requests](https://github.com/astral-sh/ruff/pulls) there for changes
to anything in the `ruff` submodule (which includes all of the Rust source code).

See the
[contributing guide](./CONTRIBUTING.md) for more details.

## License

ty is licensed under the MIT license ([LICENSE](LICENSE) or
<https://opensource.org/licenses/MIT>).

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in ty
by you, as defined in the MIT license, shall be licensed as above, without any additional terms or
conditions.

<div align="center">
  <a target="_blank" href="https://astral.sh" style="background:none">
    <img src="https://raw.githubusercontent.com/astral-sh/uv/main/assets/svg/Astral.svg" alt="Made by Astral">
  </a>
</div>
