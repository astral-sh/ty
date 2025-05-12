# ty

An extremely fast Python type checker and language server, written in Rust.

> [!WARNING]
>
> ty is in preview and is not ready for production use.
>
> We're working hard to make ty stable and feature-complete, but until then, expect to encounter bugs,
> missing features, and fatal errors.

## Getting started

### Installation

```shell
uv tool install ty@latest
```

or add ty to your project:

```shell
uv add --dev ty

# With pip.
pip install ty
```

### First steps

After installing ty, you can check that ty is available by running the `ty` command:

```shell
ty
An extremely fast Python type checker.

Usage: ty <COMMAND>

...
```

You should see a help menu listing the available commands.

For detailed information about command-line options, see the [commands](./docs/reference/cli.md) reference.

## Checking a project

The easiest way to type check your project is by running ty through [uv](https://docs.astral.sh/uv/). To do that, add ty as a project dependency:

```shell
uv add --dev ty
```

and then just run `uv run ty check` to type check all python files in the project's root. If you don't have a project yet, run [`uv init`](https://docs.astral.sh/uv/concepts/projects/init/) to create one.

```shell
uv run ty check
WARN ty is pre-release software and not ready for production use. Expect to encounter bugs, missing features, and fatal errors.
All checks passed!
```

> [!NOTE]
> As an alternative to `uv run`, you can also run ty by activating the project's virtual environment (source `.venv/bin/active` on Linux and macOS, or `.venv\Scripts\activate` on Windows) and running `ty check` directly.

ty checks the entire project by default, but you can also pass specific paths to check:

```shell
uv run ty check src/main.py
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
