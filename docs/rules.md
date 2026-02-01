# Rules

Rules are individual checks that ty performs to detect common issues in your code, such as
incompatible assignments, missing imports, or invalid type annotations. Each rule focuses on a
specific pattern and can be turned on or off depending on your project’s needs.

!!! tip

    See the [rules reference](./reference/rules.md) for an enumeration of all supported rules.

## Rule levels

Each rule has a configurable level:

- `error`: violations are reported as errors and ty exits with an exit code of 1 if there's any.
- `warn`: violations are reported as warnings. Depending on your configuration, ty exits with an exit code of 0 if there are only warning violations (default) or 1 when using `--error-on-warning`.
- `ignore`: the rule is turned off

You can configure the level for each rule on the command line using the `--warn`, `--error`, and
`--ignore` flags. For example:

```shell

ty check \
  --warn unused-ignore-comment \        # Make `unused-ignore-comment` a warning
  --ignore redundant-cast \             # Disable `redundant-cast`
  --error possibly-missing-attribute \  # Error on `possibly-missing-attribute`
  --error possibly-missing-import       # Error on `possibly-missing-import`
```

The options can be repeated. Subsequent options override earlier options.

Rule levels can also be changed in the [`rules`](./reference/configuration.md#rules) section of a
[configuration file](./configuration.md).

For example, the following is equivalent to the command above:

```toml title="pyproject.toml"
[tool.ty.rules]
unused-ignore-comment = "warn"
redundant-cast = "ignore"
possibly-missing-attribute = "error"
possibly-missing-import = "error"
```

You can also configure the level for all rules at once in your configuration file.
There is no equivalent option on the command line.

For example, setting the level for all rules to `error`:

```toml title="pyproject.toml"
[tool.ty.rules]
all = "error"
```
