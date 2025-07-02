# Rules

Rules are individual checks that ty performs to detect common issues in your code, such as
incompatible assignments, missing imports, or invalid type annotations. Each rule focuses on a
specific pattern and can be turned on or off depending on your project’s needs.

!!! tip

    See [rules](./reference/rules.md) for an enumeration of all supported rules.

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
  --error possibly-unbound-attribute \  # Error on `possibly-unbound-attribute`
  --error possibly-unbound-import       # Error on `possibly-unbound-import`
```

The options can be repeated. Subsequent options override earlier options.

Rule levels can also be changed in the [`rules`](./reference/configuration.md#rules) section of a
[configuration file](./configuration.md).

For example, the following is equivalent to the command above:

```toml
[tool.ty.rules]
unused-ignore-comment = "warn"
redundant-cast = "ignore"
possibly-unbound-attribute = "error"
possibly-unbound-import = "error"
```
