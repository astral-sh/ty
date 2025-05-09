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

For detailed information about command-line options, see the [CLI documentation](./docs/cli.md).

### Checking your project

```shell
ty check
```

## Editor integration

ty can be integrated with various editors and IDEs to provide a seamless development experience. This section provides instructions on how to set up ty with your editor and configure it to your liking.

### VS Code

Install the [ty extension](https://marketplace.visualstudio.com/items?itemName=astral-sh.ty) from the VS Code Marketplace.

For more documentation on the ty extension, refer to the extension's [README](https://github.com/astral-sh/ty-vscode).

### Other editors

ty can be used with any editor that supports the [language server protocol](https://microsoft.github.io/language-server-protocol/). To start the language server, run `ty server`. Refer to your editor's documentation
to learn how to connect to an LSP server.

<!-- ## Concepts

### Projects

### Rules

### Suppression comments -->

## Configuration

<!-- ### Configuration files -->

### Environment variables

ty defines and respects the following environment variables:

#### `TY_LOG`

If set, ty will use this value as the log level for its `--verbose` output. Accepts any filter compatible with the `tracing_subscriber` crate. For example:

- `TY_LOG=uv=debug` is the equivalent of `-vv` to the command line
- `TY_LOG=trace` will enable all trace-level logging.

See the [tracing documentation](https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#example-syntax) for more.

#### `TY_MAX_PARALLELISM`

Specifies an upper limit for the number of tasks ty is allowed to run in parallel. For example, how many files should be checked in parallel.

This isn’t the same as a thread limit. ty may spawn additional threads when necessary, e.g. to watch for file system changes or a dedicated UI thread.

#### Externally defined variables

ty also reads the following externally defined environment variables:

##### `RAYON_NUM_THREADS`

Specifies an upper limit for the number of threads ty uses when performing work in parallel. Equivalent to `TY_MAX_PARALLELISM`.

##### `VIRTUAL_ENV`

Used to detect an activated virtual environment.

##### `XDG_CONFIG_HOME`

Path to user-level configuration directory on Unix systems.

## Reference

- [Commands](./docs/cli.md)
- [Rules](./docs/rules.md)
- [Settings](./docs/configuration.md)

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
