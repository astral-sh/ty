# ty

[![PyPI](https://img.shields.io/pypi/v/ty.svg)](https://pypi.python.org/pypi/ty)
[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?logo=discord&logoColor=white)](https://discord.com/invite/astral-sh)

An extremely fast Python type checker and language server, written in Rust.

> [!WARNING]
>
> ty is in preview and is not ready for production use.
>
> We're working hard to make ty stable and feature-complete, but until then, expect to encounter bugs,
> missing features, and fatal errors.

## Getting started

Run ty with [uvx](https://docs.astral.sh/uv/guides/tools/#running-tools) to get started quickly:

```shell
uvx ty
```

For other ways to install ty, see the [installation](./docs/README.md#installation) documentation.

If you do not provide a subcommand, ty will list available commands — for detailed information about
command-line options, see the [CLI reference](./docs/reference/cli.md).

Use the `check` command to run the type checker:

```shell
uvx ty check
```

ty will run on all Python files in the working directory and or subdirectories. If used from a
project, ty will run on all Python files in the project (starting in the directory with the
`pyproject.toml`)

You can also provide specific paths to check:

```shell
uvx ty check example.py
```

When type checking, ty will find installed packages in the active virtual environment (via
`VIRTUAL_ENV`) or discover a virtual environment named `.venv` in the project root or working
directory. It will not find packages in non-virtual environments without specifying the target path
with `--python`. See the [module discovery](./docs/README.md#module-discovery) documentation for
details.

## Learning more

To learn more about using ty, see the [documentation](./docs/README.md).

## Getting involved

If you have questions or want to report a bug, please open an
[issue](https://github.com/astral-sh/ty/issues) in this repository.

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
