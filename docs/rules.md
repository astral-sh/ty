# Rules

Rules are individual checks that ty performs to detect common issues in your code, such as
incompatible assignments, missing imports, or invalid type annotations. Each rule focuses on a
specific pattern and can be turned on or off depending on your project’s needs.

!!! tip

    See the [rules reference](./reference/rules.md) for an enumeration of all supported rules.

## Rule levels

Each rule has a configurable level:

- `error`: violations are reported as errors and ty exits with an exit code of 1 if there's any.
- `warn`: violations are reported as warnings. Depending on your configuration, ty exits with an
  exit code of 0 if there are only warning violations (default) or 1 when using
  `--error-on-warning`.
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

=== "pyproject.toml"

    ```toml
    [tool.ty.rules]
    unused-ignore-comment = "warn"
    redundant-cast = "ignore"
    possibly-missing-attribute = "error"
    possibly-missing-import = "error"
    ```

=== "ty.toml"

    ```toml
    [rules]
    unused-ignore-comment = "warn"
    redundant-cast = "ignore"
    possibly-missing-attribute = "error"
    possibly-missing-import = "error"
    ```

You can also configure the level for all rules at once.

On the command line you can use `--error all`, `--warn all`, or `--ignore all`. For example:

```shell

ty check --error all
```

You can also configure this setting in the [`rules`](./reference/configuration.md#rules) section of
a [configuration file](./configuration.md).

For example, the following is equivalent to the command above:

=== "pyproject.toml"

    ```toml
    [tool.ty.rules]
    all = "error"
    ```

=== "ty.toml"

    ```toml
    [rules]
    all = "error"
    ```

## Fixes

The `ty check --fix` command applies safe fixes for diagnostics that support them. Currently, ty can
automatically fix diagnostics for these rules:

| Rule                                                                  | Fix                                                                                                                                 |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| [`redundant-cast`](./reference/rules.md#redundant-cast)               | Removes the redundant `cast(...)` call while keeping the original value.                                                            |
| [`unused-ignore-comment`](./reference/rules.md#unused-ignore-comment) | Removes unused `ty: ignore` or `type: ignore` comments, or removes only the unused rule code from a multi-code suppression comment. |

Some diagnostics also offer editor quick fixes that are not applied by `ty check --fix` because they
are not classified as safe automatic fixes. Use `ty check --add-ignore` when you want ty to add
suppression comments instead of applying diagnostic-specific fixes.
