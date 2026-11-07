# Checking standalone scripts

A Python script can declare its dependencies and Python version requirements using
[inline script metadata (PEP 723)](https://peps.python.org/pep-0723/).
[uv](https://docs.astral.sh/uv/) uses this metadata to prepare an environment when you run a
script. ty can ask uv to prepare that environment for type checking, too.

ty discovers scripts with inline metadata throughout your project. With the uv integration
enabled, ty checks each script against its own requirements, even when scripts in the same
project need different versions of Python or of a package.

!!! note "Preview"

    The uv integration is opt-in. The minimum supported versions are uv 0.12.3 and ty 0.0.76.

## On the command line

Adapted from the [uv scripts guide](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies),
`example.py` fetches PEP titles with `requests` and displays them with `rich`. Its inline metadata
declares both dependencies and requires Python 3.12 or later.

```python title="example.py"
# /// script
# requires-python = ">=3.12"
# dependencies = ["requests<3", "rich"]
# ///

import requests
from rich.console import Console
from rich.pretty import pprint

response = requests.get("https://peps.python.org/api/peps.json")
peps = response.json()
Console().rule("Python Enhancement Proposals")
pprint([(number, pep["title"]) for number, pep in peps.items()][:10])
```

Save the script as `example.py` and enable the uv integration when you run `ty check`. ty asks uv
to install the declared dependencies before checking the script.

```shell
TY_UV=scripts ty check example.py
```

Omit the file name to check the project and its scripts together.

```shell
TY_UV=scripts ty check
```

You can also check a single script with uv's experimental
[`uv check --script example.py`](https://docs.astral.sh/uv/reference/cli/#uv-check--script) command,
which enables the integration automatically.

## In your editor

Set [`experimental.useUv`](./reference/editor-settings.md#experimentaluseuv) to `"scripts"`.
ty uses uv to prepare the script's environment in the background and updates it when you save
changes to the script's dependencies.

<figure>
  <video src="../assets/scripts-editor-demo.mp4" controls playsinline preload="metadata"
         width="1440" height="900" style="max-width: 100%; height: auto;"
         aria-labelledby="script-editor-demo-caption">
    <a href="../assets/scripts-editor-demo.mp4">Download the editor demo</a>.
  </video>
  <figcaption id="script-editor-demo-caption">
    Save <code>example.py</code> after adding <code>rich</code> to its dependencies. Once the
    environment sync finishes, accepting the <code>Console</code> completion adds its import.
    ty can then complete <code>rule</code>, show its signature on hover, and jump to its definition.
  </figcaption>
</figure>

## Configuring a script

A script inherits the [project configuration](./configuration.md), including any
[`overrides`](./reference/configuration.md#overrides) that match its path. For example, an override
for `scripts/*.py` applies to `scripts/example.py`. Scripts have their own
[`environment.root`](./reference/configuration.md#root), which defaults to an empty list.

To configure a script independently, add a `[tool.ty]` table to its inline script metadata.
Use the same syntax as in `pyproject.toml`, such as `[tool.ty.rules]` to configure rule
severity. An inline table, even an empty one, replaces the project settings and overrides for
that script.

The script's `requires-python` takes precedence over the inherited Python version. For example,
ty checks `example.py` against Python 3.12 even in a project that targets Python 3.10. An inline
`environment.python-version` takes precedence over `requires-python`.

Script or project settings take precedence over user-level configuration. Command-line settings
take precedence over both. Use `--config-file` to select a configuration file in place of the
project or inline configuration.
