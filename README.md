# ty

An extremely fast Python type checker and language server, written in Rust.

> [!WARNING]
> ty is pre-release software and not ready for production use. Expect to encounter bugs, missing
> features, and fatal errors.

ty is in active development, and we're working hard to make it stable
and feature-complete.

## Getting started

Use [uvx](https://docs.astral.sh/uv/guides/tools/#running-tools) to get started quickly:

```shell
uvx ty check
```

> [!NOTE]
> When using uvx, ty will find installed packages in the active virtual environment (via
>  `VIRTUAL_ENV`) or discover a virtual environment named `.venv` in the project root or working
> directory. See [module discovery](./docs/README.md#module-discovery) for details.

## Installation

### Adding ty to your project

Use [uv](https://github.com/astral-sh/uv) (or your project manager of choice) to add ty as a
development dependency:

```shell
uv add --dev ty
```

Adding ty as a dependency ensures that all developers on the project are using the same version of
ty.

Then, use `uv run` to invoke ty:

```shell
uv run ty
```

### Installing ty

Install ty globally with uv:

```shell
uv tool install ty@latest
```

Or, into an existing environment with pip:

```shell
pip install ty
```

## Viewing ty commands

Running ty will list available commands:

```console
$ ty
An extremely fast Python type checker.

Usage: ty <COMMAND>

...
```

For detailed information about command-line options, see the [commands] reference.

## Checking a project

To run ty on all files in your project:

```console
$ ty check
All checks passed!
```

> [!NOTE]
> If you added ty as a dependency in your project, use `uv run` to invoke ty. Alternatively, you can
> [activate](https://docs.astral.sh/uv/pip/environments/#using-a-virtual-environment) the virtual
> environment and run ty directly. If you installed ty globally, you can run it without activating
> the environment but it may not see installed packages; see [module discovery](./docs/README.md#module-discovery)
> for details.

ty checks the entire project by default, but you can also provide specific paths to check:

```shell
ty check src/main.py
```

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
