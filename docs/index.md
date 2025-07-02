# ty

An extremely fast Python type checker, written in Rust.

<!-- TODO
## Highlights

- ...
-->

## Getting started

Try out the [online playground](https://play.ty.dev), or run ty with
[uvx](https://docs.astral.sh/uv/guides/tools/#running-tools) to get started quickly:

```shell
uvx ty
```

For other ways to install ty, see the [installation](./installation.md) documentation.

If you do not provide a subcommand, ty will list available commands — for detailed information about
command-line options, see the [CLI reference](./reference/cli.md).

Use the `check` command to run the type checker:

```shell
uvx ty check
```

ty will run on all Python files in the working directory and or subdirectories. If used from a
project, ty will run on all Python files in the project (starting in the directory with the
`pyproject.toml`)

You can also provide specific paths to check:

```shell
uvx ty check example.py
```

When type checking, ty will find installed packages in the active virtual environment (via
`VIRTUAL_ENV`) or discover a virtual environment named `.venv` in the project root or working
directory. It will not find packages in non-virtual environments without specifying the target path
with `--python`. See the [module discovery](./modules.md) documentation for
details.

### Usage

Run [`ty check`](./reference/cli.md#ty-check), in your project's top-level directory,
to check the project for type errors using ty's default configuration.

If this provokes a cascade of errors, and you are using the standard library `venv` module
to provide your virtual environment, add the venv directory to your `.gitignore`
or `.ignore` file and then retry.
