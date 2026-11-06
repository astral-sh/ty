# Type checking

After [installing ty](./installation.md), it's time to type check some code!

## Running the type checker

To run the type checker, use the `check` command:

```shell
ty check
```

!!! tip

    If you're in a project, you may need to use `uv run` or activate your virtual environment first
    for ty to find your dependencies.

## Environment discovery

The type checker needs to discover your installed packages in order to check your use of imported
dependencies.

ty discovers packages from a Python environment, such as an active virtual or Conda environment or
a `.venv` in the project root. If none is found, ty looks for a `python3` or `python` binary on
`PATH`. Use the `--python` flag to explicitly specify a path to a Python interpreter.

See the [module discovery](./modules.md) documentation for the full search order.

## File selection

ty will run on all Python files in the working directory (including subdirectories, recursively).
If used from a project, ty will run on all Python files in the project (starting in the directory
with the `pyproject.toml`).

You can also provide specific paths to check:

```shell
ty check example.py
```

You can also persistently configure [included and excluded files](./exclusions.md).

## Rule selection and severity

ty's type checking diagnostics are often associated with a rule.

ty's type checking rules can be configured to your project's needs. See the [rules](./rules.md)
documentation for details.

You can also suppress specific violations of rules using [suppression comments](./suppression.md).

## Watch mode

ty can be run in an incremental watch mode:

```shell
ty check --watch
```

ty will watch files for changes and recheck any affected files — including files that depend on the
changed file. ty uses [fine-grained incrementality](./features/language-server.md#fine-grained-incrementality)
to perform subsequent checks much faster than running `ty check` repeatedly.

## The type system

To learn more about what makes type checking in ty unique, read about the
[type system](./features/type-system.md).
