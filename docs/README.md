# ty

## Getting started

For a quick guide on getting started, see the top-level [README](../README.md#getting-started).

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

### Installing globally

Install ty globally with uv:

```shell
uv tool install ty@latest
```

Or, pipx:

```shell
pipx install ty
```

### Installing with pip

Install ty into your current Python environment with pip:

```shell
pip install ty
```

## Module discovery

### First-party modules

First-party modules are Python files that are part of your project source code.

By default, ty searches for first-party modules in the project's root directory or the `src`
directory, if present.

If your project uses a different layout, configure the project's
[`src.root`](./reference/configuration.md#root) in your `pyproject.toml` or `ty.toml`. For example,
if your project's code is in an `app/` directory:

```text
example-pkg
├── README.md
├── pyproject.toml
└── app
    └── example_pkg
        └── __init__.py
```

then set [`src.root`](./reference/configuration.md#root) in your `pyproject.toml` to `./app`:

```toml
[tool.ty.src]
root = "./app"
```

### Third-party modules

Third-party modules are Python packages that are not part of your project or the standard library.
These are usually declared as dependencies in a `pyproject.toml` or `requirements.txt` file
and installed using a package manager like uv or pip. Examples of popular third-party
modules are `requests`, `numpy` and `django`.

ty searches for third-party modules in the configured [Python environment](#python-environment).

### Python environment

The Python environment is used for discovery of third-party modules.

By default, ty will attempt to discover a virtual environment.

First, ty checks for an active virtual environment using the `VIRTUAL_ENV` environment variable. If
not set, ty will search for a `.venv` directory in the project root or working directory. ty only
supports discovery of virtual environments at this time.

> [!NOTE]
>
> When using project management tools, such as uv or Poetry, the `run` command usually automatically
> activates the virtual environment and will be detected by ty.

The Python environment may be explicitly configured using the
[`environment.python`](./reference/configuration.md#python) setting or
[`--python`](./reference/cli.md#ty-check--python) flag.

When setting the environment explicitly, non-virtual environments can be provided.

## Python version

The Python version affects allowed syntax, type definitions of the standard library, and type
definitions of first- and third-party modules that are conditional on the Python version.

For example, Python 3.10 introduced support for `match` statements and added the
`sys.stdlib_module_names` symbol to the standard library. Syntactic features always
need to be available in the lowest supported Python version, but symbols may be used
in a `sys.version_info` conditional branch:

```python
import sys

# `invalid-syntax` error if `python-version` is set to 3.9 or lower:
match "echo hello".split():
    case ["echo", message]:
        print(message)
    case _:
        print("unknown command")

# `unresolved-attribute` error if `python-version` is set to 3.9 or lower:
print(sys.stdlib_module_names)

if sys.version_info >= (3, 10):
    # ok, because the usage is guarded by a version check:
    print(sys.stdlib_module_names)
```

By default, the lower bound of the project's [`requires-python`](<(https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#python-requires)>) field (from the `pyproject.toml`) is
used as the target Python version, ensuring that features and symbols only available in newer Python
versions are not used.

If the `requires-python` field is not available, the latest stable version supported by ty is used,
which is currently 3.13.

ty will not infer the Python version from the Python environment at this time.

The Python version may be explicitly specified using the
[`python-version`](./reference/configuration.md#python-version) setting or the
[`--python-version`](./reference/cli.md#ty-check--python-version) flag.

## Excluding files

By default, ty ignores files listed in an `.ignore` or `.gitignore` file.

To disable this functionality, set [`respect-ignore-files`](./reference/configuration.md#respect-ignore-files) to `false`.

You may also explicitly pass the paths that ty should check, e.g.:

```shell
ty check src scripts/benchmark.py
```

We plan on adding dedicated options for including and excluding files in future releases.

## Editor integration

ty can be integrated with various editors to provide a seamless development experience.

### VS Code

The Astral team maintains an official VS Code extension.

Install the [ty extension](https://marketplace.visualstudio.com/items?itemName=astral-sh.ty) from the VS Code Marketplace.

See the extension's [README](https://github.com/astral-sh/ty-vscode) for more details on usage.

### Other editors

ty can be used with any editor that supports the [language server
protocol](https://microsoft.github.io/language-server-protocol/).

To start the language server, use the `server` subcommand:

```shell
ty server
```

Refer to your editor's documentation to learn how to connect to an LSP server.

See the [editor settings](./reference/editor-settings.md) for more details on configuring the language
server.

## Rules

Rules are individual checks that ty performs to detect common issues in your code, such as
incompatible assignments, missing imports, or invalid type annotations. Each rule focuses on a
specific pattern and can be turned on or off depending on your project’s needs.

See [rules](./reference/rules.md) for an enumeration of all supported rules.

### Rule levels

Each rule has a configurable level:

- `error`: violations are reported as errors and ty exits with an exit code of 1 if there's any.
- `warn`: violations are reported as warnings. Depending on your configuration, ty exits with an exit code of 0 if there are only warning violations (default) or 1 when using `--error-on-warning`.
- `ignore`: the rule is turned off

You can configure the level for each rule on the command line using the `--warn`, `--error`, and
`--ignore` flags. For example:

```shell

ty check \
    --warn unused-ignore-comment \          # Make `unused-ignore-comment` a warning
    --ignore redundant-cast \               # Disable `redundant-cast`
    --error possibly-unbound-attribute \    # Error on `possibly-unbound-attribute`
    --error possibly-unbound-import         # Error on `possibly-unbound-import`
```

The options can be repeated. Subsequent options override earlier options.

Rule levels can also be changed in the [`rules`](./reference/configuration.md#rules) section of a
[configuration file](#configuration-files).

For example, the following is equivalent to the command above:

```toml
[tool.ty.rules]
unused-ignore-comment = "warn"
redundant-cast = "ignore"
possibly-unbound-attribute = "error"
possibly-unbound-import = "error"
```

## Suppressions

Rules can also be ignored in specific locations in your code (instead of disabling the rule
entirely) to silence false positives or permissible violations.

> [!NOTE]
>
> To disable a rule entirely, set it to the `ignore` level as described in [rule levels](#rule-levels).

### ty suppression comments

To suppress a rule violation inline add a `# ty: ignore[<rule>]` comment at the end of the line:

```py
a = 10 + "test"  # ty: ignore[unsupported-operator]
```

Rule violations spanning multiple lines can be suppressed by adding the comment at the end of the
violation's first or last line:

```py
def add_three(a: int, b: int, c: int): ...

# on the first line

add_three(  # ty: ignore[missing-argument]
    3,
    2
)

# or, on the last line

add_three(
    3,
    2
)  # ty: ignore[missing-argument]
```

To suppress multiple violations on a single line, enumerate each rule separated by a comma:

```python
add_three("one", 5)  # ty: ignore[missing-argument, invalid-argument-type]
```

> [!NOTE]
>
> Enumerating rule names (e.g., `[rule1, rule2]`) is optional. However, we strongly recommend
> including suppressing specific rules to avoid accidental suppression of other errors.

### Standard suppression comments

ty supports the standard [`type:ignore`](https://typing.python.org/en/latest/spec/directives.html#type-ignore-comments) comment
format introduced by PEP 484.

ty handles these similarly to `ty: ignore` comments, but suppresses all violations on that line,
even when `type: ignore[code]` is used.

```python
# Ignore all typing errors on the next line
add_three("one", 5)  # type: ignore
```

### Unused suppression comments

If the [`unused-ignore-comment`](./reference/rules.md#unused-ignore-comment) rule is enabled, ty
will report unused `ty: ignore` and `type: ignore` comments.

`unused-ignore-comment` violations can only be suppressed using `# ty: ignore[unused-ignore-comment]`.
They cannot be suppressed using `# ty: ignore` without a rule code or `# type: ignore`.

### `@no_type_check` directive

ty supports the
[`@no_type_check`](https://typing.python.org/en/latest/spec/directives.html#no-type-check) decorator
to suppress all violations inside a function.

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

See the [configuration](./reference/configuration.md) reference for an enumeration of the available settings.

## Exit codes

- `0` if no violations with severity `error` or higher were found.
- `1` if any violations with severity `error` were found.
- `2` if ty terminates abnormally due to invalid CLI options.
- `101` if ty terminates abnormally due to an internal error.

ty supports two command line arguments that change how exit codes work:

- `--exit-zero`: ty will exit with `0` even if violations were found.
- `--error-on-warning`: ty will exit with `1` if it finds any violations with severity `warning` or higher.

## Reference

For more details, see the reference documentation:

- [Commands](./reference/cli.md)
- [Rules](./reference/rules.md)
- [Configuration](./reference/configuration.md)
- [Environment variables](./reference/env.md)
