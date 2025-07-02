# Python version

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

By default, the lower bound of the project's [`requires-python`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#python-requires) field (from the `pyproject.toml`) is
used as the target Python version, ensuring that features and symbols only available in newer Python
versions are not used.

If the `requires-python` field is not available but a virtual environment *has* been
configured or detected, ty will try to infer the Python version being used from the virtual
environment's metadata.

If no virtual environment is present or inferring the Python version from the metadata fails,
ty will fall back to the latest stable Python version supported by ty (currently 3.13).

The Python version may also be explicitly specified using the
[`python-version`](./reference/configuration.md#python-version) setting or the
[`--python-version`](./reference/cli.md#ty-check--python-version) flag.
