# Module discovery

## First-party modules

First-party modules are Python files that are part of your project source code.

By default, ty searches for first-party modules in the project root. It also searches the following
directories, if they exist and are not themselves packages (i.e. they contain neither an
`__init__.py` nor an `__init__.pyi` file):

- `./src`
- `./<project-name>`, if `./<project-name>/<project-name>` exists
- `./python`

These directories are searched before the project root, in the order listed above.

If your project uses a different layout, configure the project's
[`environment.root`](./reference/configuration.md#root) in your `pyproject.toml` or `ty.toml`. For example,
if your project's code is in an `app/` directory:

```text
example-pkg
├── README.md
├── pyproject.toml
└── app
    └── example_pkg
        └── __init__.py
```

then set [`environment.root`](./reference/configuration.md#root) in your `pyproject.toml` to `["./app"]`:

=== "pyproject.toml"

    ```toml
    [tool.ty.environment]
    root = ["./app"]
    ```

=== "ty.toml"

    ```toml
    [environment]
    root = ["./app"]
    ```

## Third-party modules

Third-party modules are Python packages that are not part of your project or the standard library.
These are usually declared as dependencies in a `pyproject.toml` or `requirements.txt` file
and installed using a package manager like uv or pip. Examples of popular third-party
modules are `requests`, `numpy` and `django`.

ty searches for third-party modules in the configured [Python environment](#python-environment).

## Python environment

The Python environment is used for discovery of third-party modules.

For a project with no explicitly configured environment, ty searches for one in the following order:

1. An active virtual environment, using the `VIRTUAL_ENV` environment variable.
1. An active [non-`base` Conda environment](https://docs.conda.io/projects/conda/en/stable/user-guide/getting-started.html#listing-environments).
1. A `.venv` directory in the project root.
1. An active [`base` Conda environment](https://docs.conda.io/projects/conda/en/stable/user-guide/getting-started.html#listing-environments).
1. A `python3` or `python` interpreter on `PATH`.

!!! note

    When using project management tools, such as uv or Poetry, the `run` command usually automatically
    activates the virtual environment and will be detected by ty.

The Python environment may be explicitly configured using the
[`environment.python`](./reference/configuration.md#python) setting or
[`--python`](./reference/cli.md#ty-check--python) flag.

When setting the environment explicitly, non-virtual environments can be provided.

### `PYTHONPATH`

ty also respects the [`PYTHONPATH`](./reference/environment.md#pythonpath) environment variable.
Each existing directory listed in `PYTHONPATH` is added to the module search path, just after any
[`extra-paths`](./reference/configuration.md#extra-paths) and before the environment's
`site-packages`, mirroring the resolution order of the Python interpreter itself.

`PYTHONPATH` uses the same format as the shell's `PATH`: one or more directory paths separated by the
platform's path separator (`:` on Unix, `;` on Windows). Entries that don't exist or aren't
directories are ignored.
