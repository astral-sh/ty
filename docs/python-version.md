# Python version

The Python version affects allowed syntax, type definitions of the standard library, and type
definitions of first- and third-party modules that are conditional on the Python version.

For example, Python 3.10 introduced support for `match` statements, and Python 3.15 added
`sys.abi_info` to the standard library. Syntactic features always need to be available in the
lowest supported Python version, but symbols may be used in a `sys.version_info` conditional branch.

```python
import sys

# `invalid-syntax` error if `python-version` is set to 3.9 or lower:
match "echo hello".split():
    case ["echo", message]:
        print(message)
    case _:
        print("unknown command")

# `missing-attribute` error if `python-version` is set to 3.14 or lower:
print(sys.abi_info)

if sys.version_info >= (3, 15):
    # ty skips this branch for older targets, where `sys.abi_info` is unavailable.
    print(sys.abi_info)
```

By default, the lower bound of the project's [`requires-python`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#python-requires) field (from the `pyproject.toml`) is
used as the target Python version, ensuring that features and symbols only available in newer Python
versions are not used.

For [scripts with inline metadata](./scripts.md), ty uses the script's inline
`environment.python-version` if set, then the lower bound of its `requires-python` field. If the
inline metadata has neither setting and contains no `[tool.ty]` table, the script can inherit the
project's Python version.

If `requires-python` is absent and no target version has been set, ty will try to infer it from
the configured or discovered [Python environment](./modules.md#python-environment).

If no Python environment is present or inferring the Python version from it fails,
ty will fall back to the default [`python-version`](./reference/configuration.md#python-version).

The Python version may also be explicitly specified using the
[`python-version`](./reference/configuration.md#python-version) setting or the
[`--python-version`](./reference/cli.md#ty-check--python-version) flag.

ty officially supports type checking code that targets Python 3.10 and later, though earlier
versions (Python 3.7 through 3.9) can still be selected as targets. When analyzing code under
`--python-version=3.7` or similar, ty will continue to check version-dependent syntax, perform
narrowing based on `sys.version_info`, and more, but may produce false positives or false
negatives for standard-library APIs as its bundled stubs do not fully describe those Python
versions.
