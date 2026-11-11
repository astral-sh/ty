# Configuration

## Configuration files

ty supports persistent configuration files at both the project- and user-level.

Specifically, ty will search for a `pyproject.toml` or `ty.toml` file in the current directory, or in the nearest parent directory.

If a `pyproject.toml` file is found, ty will read configuration from the `[tool.ty]` table. If there is no `[tool.ty]` table, ty may
still read the [`project.name`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#name) and
[`project.requires-python`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#python-requires)
fields from the `pyproject.toml` file, but will then continue searching the directory hierarchy for ty-specific configuration.

For example, add the following to a `pyproject.toml` to ignore the `index-out-of-bounds` rule:

```toml title="pyproject.toml"
[tool.ty.rules]
index-out-of-bounds = "ignore"
```

ty will also search for `ty.toml` files, which follow an identical structure, but omit the `[tool.ty]` prefix. For example:

```toml title="ty.toml"
[rules]
index-out-of-bounds = "ignore"
```

!!! important

    `ty.toml` files take precedence over `pyproject.toml` files, so if both `ty.toml` and `pyproject.toml` files are present in a directory, configuration will be read from `ty.toml`, and the `[tool.ty]` section in the accompanying `pyproject.toml` will be ignored.

ty will also discover user-level configuration at `~/.config/ty/ty.toml` (or `$XDG_CONFIG_HOME/ty/ty.toml`) on macOS and Linux, or `%APPDATA%\ty\ty.toml` on Windows. User-level configuration must use the `ty.toml` format, rather than the `pyproject.toml` format, as a `pyproject.toml` is intended to define a Python project.

If project- and user-level configuration files are found, the settings will be merged, with project-level configuration taking precedence over the user-level configuration.

For example, if a string, number, or boolean is present in both the project- and user-level configuration tables, ty uses the project-level value. If an array is present in both tables, ty merges the arrays, with the project-level settings appearing later in the merged array.

Settings provided via command line take precedence over persistent configuration.

See the [configuration](./reference/configuration.md) reference for the available settings.
