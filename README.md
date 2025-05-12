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

For detailed information about command-line options, see the [commands] reference.

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

### First-party imports

By default, ty searches for first-party imports in the project's root folder or the `src` folder if it exists. If you use a different project layout, explicitly set the project's [`src.root`](https://github.com/astral-sh/ty/blob/main/docs/configuration.md#root). For example, if your project's code is in the `app` directory, like so:

```text
example-pkg
├── README.md
├── pyproject.toml
└── app
    └── example_pkg
        └── __init__.py
```

then set the `src.root` setting in the `pyproject.toml` to `./app`:

```toml
[tool.ty.src]
root = "./app"
```

### Third-party imports

By default, ty searches for third-party imports in a local virtual environment.

- `VIRTUAL_ENV`

### Python version

- `python-version`
- `requires-python` constraint

### Excluding files

ty ignores files listed in an `.ignore` or `.gitignore` file unless [`respect-ignore-files`](https://github.com/astral-sh/ty/blob/main/docs/configuration.md#respect-ignore-files) is set to `false`.

Alternatively, you can explicitly pass the paths that ty should be checked, like so: `ty check src scripts/benchmark.py`. We plan on adding dedicated options for including and excluding files in an upcoming release.

## Editor integration

ty can be integrated with various editors and IDEs to provide a seamless development experience. This section provides instructions on how to set up ty with your editor and configure it to your liking.

### VS Code

Install the [ty extension](https://marketplace.visualstudio.com/items?itemName=astral-sh.ty) from the VS Code Marketplace.

For more documentation on the ty extension, refer to the extension's [README](https://github.com/astral-sh/ty-vscode).

### Other editors

ty can be used with any editor that supports the [language server protocol](https://microsoft.github.io/language-server-protocol/). To start the language server, run `ty server`. Refer to your editor's documentation
to learn how to connect to an LSP server.

## Concepts

<!--

### Projects  -->

### Rules

Rules are individual type checks that detect common issues in your code—such as incompatible assignments, missing imports, or invalid type annotations. Each rule focuses on a specific pattern and can be turned on or off depending on your project’s needs.
See [rules] for a reference of all supported rules.

#### Rule level

Each rule has a configurable level:

- `error`: violations are reported as errors and ty exits with an exit code of 1 if there's any.
- `warn`: violations are reported as warnings. Depending on your configuration, ty exits with an exit code of 0 if there are only warning violations (default) or 1 when using `--error-on-warning`.
- `ignore`: the rule is turned off

#### Configuring rules on the command line

You can configure the lint level for each rule on the command line using `--warn`, `--error`, and `--ignore`.

```shell
ty check --warn unused-ignore-comment --ignore redundant-cast --error possibly-unbound-attribute --error possibly-unbound-import
```

This command:

- enables `unused-ignore-comment` and sets its level to warnings
- disables `redundant-cast`
- changes the lint level for `possibly-unbound-attribute` and `possibly-unbound-import` from warning to error

The options can be repeated and options coming later take precedence over earlier options.

#### Configuring rules in a configuration file

You can turn rules on or of or change their level in your [configuration](#configuration-files)'s [`rules`](https://github.com/astral-sh/ty/blob/main/docs/configuration.md#rules) section.

```toml
[tool.ty.rules]
unused-ignore-comment = "warn"
redundant-cast = "warn"
possibly-unbound-attribute = "error"
possibly-unbound-import = "error"
```

This configuration:

- enables `unused-ignore-comment` and sets its level to warnings
- disables `redundant-cast`
- changes the lint level for `possibly-unbound-attribute` and `possibly-unbound-import` from warning to error

### Suppressions

#### Line-level suppression comments

Suppression comments allow you to silence specific instances of ty violations in your code, be they false positives or permissible violations.

> [!NOTE]
> To disable a rule entirely, set [its severity to `ignore`](https://github.com/astral-sh/ruff/ty/main/docs/configuration.md#rules) in your `ty.toml` or `pyproject.toml` or disable it using the [`--ignore` CLI argument](https://github.com/astral-sh/ruff/blob/main/crates/ty/docs/cli.md#ty-check--ignore).

To suppress a violation inline add a `# ty: ignore[rule]` comment at the end of the line:

```py
a = 10 + "test"  # ty: ignore[unsupported-operator]
```

Multiline violations can be suppressed by adding the comment at the end of the violation's first or last line:

```py
def add_three(a: int, b: int, c: int): ...


add_three(  # ty: ignore[missing-argument]
    3,
    2
)
```

or when adding the suppression to the last line:

```py
add_three(
    3,
    2
)  # ty: ignore[missing-argument]
```

To suppress multiple violations on the same line, list all rule names and separate them with a comma:

```python
add_three("one", 5)  # ty: ignore[missing-argument, invalid-argument-type]
```

The comma separated list of rule names (`[rule1, rule2]`) is optional. We recommend to always suppress specific error codes to avoid accidental suppression of other errors.

ty supports the [`type: ignore` comment format](https://typing.python.org/en/latest/spec/directives.html#type-ignore-comments) introduced with PEP 484. ty handles them similarly to `ty: ignore` comments, but it suppresses all violations on that line, even when using `type: ignore[code]`.

```py
# Ignore all typing errors on the next line
add_three("one", 5)  # type: ignore
```

ty reports unused `ty: ignore` and `type: ignore` comments if the rule [`unused-ignore-comment`](https://github.com/astral-sh/ty/blob/main/crates/ty/docs/rules.md#unused-ignore-comment) is enabled. `unused-ignore-comment` violations
can only be suppressed using `ty: ignore[unused-ignore-comment]`. They can't be suppressed using `ty: ignore` (without a rule code) or a `type: ignore` comment.

#### `@no_type_check` directive

ty supports the [`@no_type_check`](https://typing.python.org/en/latest/spec/directives.html#no-type-check) decorator to suppress all violations inside a function.

```python
from typing import no_type_check

def add_three(a: int, b: int, c: int):
    a + b + c

@no_type_check
def main():
    add_three(3, 4)
```

Decorating a class with `@no_type_check` isn't supported.

## Configuration

### Configuration files

ty supports persistent configuration files at both the project- and user-level.

Specifically, ty will search for a `pyproject.toml` or `ty.toml` file in the current directory, or in the nearest parent directory.

If a `pyproject.toml` file is found, ty will read configuration from the `[tool.ty]` table. For example, to ignore the `index-out-of-bounds` rule, add the following to a `pyproject.toml`:

**`pyproject.toml`**:

```toml
[tool.ty.rules]
index-out-of-bounds = "ignore"
```

(If there is no `tool.ty` table, the `pyproject.toml` file will be ignored, and ty will continue searching in the directory hierarchy.)

ty will also search for `ty.toml` files, which follow an identical structure, but omit the `[tool.ty]` prefix. For example:

**`ty.toml`**:

```toml
[rules]
index-out-of-bounds = "ignore"
```

> [!NOTE]
> `ty.toml` files take precedence over `pyproject.toml` files, so if both `ty.toml` and `pyproject.toml` files are present in a directory, configuration will be read from `ty.toml`, and the `[tool.ty]` section in the accompanying `pyproject.toml` will be ignored.

ty will also discover user-level configuration at `~/.config/ty/ty.toml` (or `$XDG_CONFIG_HOME/ty/ty.toml`) on macOS and Linux, or `%APPDATA%\ty\ty.toml` on Windows. User-level configuration must use the `ty.toml` format, rather than the `pyproject.toml` format, as a `pyproject.toml` is intended to define a Python project.

If project- and user-level configuration files are found, the settings will be merged, with project-level configuration taking precedence over the user-level configuration.

For example, if a string, number, or boolean is present in both the project- and user-level configuration tables, the project-level value will be used, and the user-level value will be ignored. If an array is present in both tables, the arrays will be merged, with the project-level settings appearing later in the merged array.

Settings provided via command line take precedence over persistent configuration.

See the [configuration] reference for an enumeration of the available settings.

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

- [commands]
- [rules]
- [configuration]

### Exit codes

- `0` if no violations with severity `error` or higher were found.
- `1` if any violations with severity `error` were found.
- `2` if ty terminates abnormally due to invalid CLI options.
- `101` if ty terminates abnormally due to an internal error.

ty supports two command line arguments that change how exit codes work:

- `--exit-zero`: ty will exit with `0` even if violations were found.
- `--error-on-warning`: ty will exit with `1` if it finds any violations with severity `warning` or higher.

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

[commands]: https://github.com/astral-sh/ty/blob/main/docs/cli.md
[configuration]: https://github.com/astral-sh/ty/blob/main/docs/configuration.md
[rules]: https://github.com/astral-sh/ty/blob/main/docs/rules.md
