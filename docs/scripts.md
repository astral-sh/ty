# Checking standalone scripts

ty can check a project and its standalone scripts together, even when they target different
Python versions or depend on different versions of the same package.

A script can declare its dependencies and Python version requirements using
[inline script metadata (PEP 723)](https://peps.python.org/pep-0723/). For example,
`package_report.py` declares `httpx>=0.28` for the `httpx.Client` used in the
[editor demo](#in-your-editor).

```python title="package_report.py"
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "attrs>=25.4",
#     "httpx>=0.28",
#     "idna>=3.10",
#     "rich>=14",
# ]
# ///
```

[uv](https://docs.astral.sh/uv/) uses those requirements when it
[runs `package_report.py`](https://docs.astral.sh/uv/guides/scripts/). ty discovers scripts with inline
metadata throughout your project and can ask uv to prepare an environment for each one.

!!! note "Preview"

    The uv integration is opt-in. The minimum supported versions are uv 0.12.3 and ty 0.0.76.

## In your editor

When you save `package_report.py`, ty can ask uv to install its declared dependencies in the
background. Completions and hover information for `httpx` then come from the version installed
for the script, even if the surrounding project uses `httpx` 0.27.

To enable this in your editor, set [`experimental.useUv`](./reference/editor-settings.md#experimentaluseuv)
to `"scripts"`.

<figure>
  <video src="https://astral.sh/static/MP4/ty-pep723-blog.mp4" controls playsinline preload="metadata"
         width="960" height="540" aria-labelledby="script-demo-caption"></video>
  <figcaption id="script-demo-caption">
    In <code>package_report.py</code>, Go to Definition on <code>client.get</code> opens the
    <code>httpx</code> implementation installed for the script.
    <a href="https://astral.sh/blog/uv-ty-integration">Watch on the Astral blog</a>.
  </figcaption>
</figure>

## On the command line

To check a project and its standalone scripts together, enable the uv integration when you run `ty check`.

```shell
TY_UV=scripts ty check
```

For `package_report.py`, ty checks against Python 3.12, the minimum version declared in the
script, even if the project targets Python 3.10.

To check just this script, run `TY_UV=scripts ty check package_report.py`. You can also use uv's
experimental [`uv check --script package_report.py`](https://docs.astral.sh/uv/reference/cli/#uv-check--script)
command to prepare the environment and run ty for you.

## Configuring a script

By default, a script uses the [project configuration](./configuration.md), including any
[`overrides`](./reference/configuration.md#overrides) that match its path. Its `requires-python`
takes precedence over the project's Python version.

An inline `[tool.ty]` table, even an empty one, replaces the project settings and overrides for
that script. Within the table, `environment.python-version` takes precedence over `requires-python`.
Script or project settings take precedence over user-level settings, and command-line settings
take precedence over both.
