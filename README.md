# ty

An extremely fast Python type checker and language server, written in Rust.

> [!WARNING]
> ty is pre-release software and not ready for production use. Expect to encounter bugs, missing
> features, and fatal errors.

ty is in active development, and we're working hard to make it stable
and feature-complete.

## Getting started

### Installation

```shell
uv tool install ty
```

### Basic usage

Type check a Python file or project:

```shell
ty check myfile.py
ty check my_project/
```

Start the language server for IDE integration:

```shell
ty server
```

For detailed information about command-line options, see the [CLI documentation](ruff/crates/ty/docs/cli.md).

## Getting involved

If you have questions or want to report a bug, please open an
[issue](https://github.com/astral-sh/ty/issues) in this repository.

Development of this project takes place in the [Ruff](https://github.com/astral-sh/ruff) repository
at this time. Please [open pull requests](https://github.com/astral-sh/ruff/pulls) there for changes
to anything in the `ruff` submodule (which includes all of the Rust source code).

See the
[contributing guide](https://github.com/astral-sh/ty/blob/main/CONTRIBUTING.md) for more details.

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
