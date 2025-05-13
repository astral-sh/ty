# Contributing

> [!IMPORTANT]
> If you want to contribute changes to ty's core, please check out the
> [dedicated `ty` contributing guide](https://github.com/astral-sh/ruff/blob/main/crates/ty/CONTRIBUTING.md).
> Keep reading if you want to contribute to ty's documentation or release process instead.

## Repository structure

This repository contains ty's documentation and release infrastructure. The core of ty's Rust codebase is
located in the [Ruff](https://github.com/astral-sh/ruff) repository. While the relationship between these
two projects will evolve over time, they currently share foundational crates and it's easiest to use a single
repository for the Rust development.

The Ruff repository is included as a submodule inside this repository to allow ty's release tags to reflect
an exact snapshot of the Ruff project. The submodule is only updated on release. To see the latest development
code, check out the `main` branch of the Ruff repository.

## Getting started with the ty repository

Clone the repository:

```shell
git clone https://github.com/astral-sh/ty.git
```

Then, ensure the submodule is initialized:

```shell
git submodule update --init --recursive
```

### Prerequisites

You'll need [uv](https://docs.astral.sh/uv/getting-started/installation/) (or `pipx` and `pip`) to
run Python utility commands.

You can optionally install pre-commit hooks to automatically run the validation checks
when making a commit:

```shell
uv tool install pre-commit
pre-commit install
```

## Building the Python package

The Python package can be built with any Python build frontend (Maturin is used as a backend), e.g.:

```shell
uv build
```

## Updating the Ruff commit

To update the Ruff submodule to the latest commit:

```shell
git -C ruff pull origin main
```

Or, to update the Ruff submodule to a specific commit:

```shell
git -C ruff checkout <commit>
```

To commit the changes:

```shell
commit=$(git -C ruff rev-parse --short HEAD)
git switch -c "sync/ruff-${commit}"
git add ruff
git commit -m "Update ruff submodule to https://github.com/astral-sh/ruff/commit/${commit}"
```

To restore the Ruff submodule to a clean-state, reset, then update the submodule:

```shell
git -C ruff reset --hard
git submodule update
```

To restore the Ruff submodule to the commit from `main`:

```shell
git -C ruff reset --hard $(git ls-tree main -- ruff | awk '{print $3}')
git add ruff
```

## Releasing ty

Releases can only be performed by Astral team members.

Preparation for the release is automated.

1. Run `./scripts/release.sh`.

    The release script will:

    - Update the Ruff submodule to the latest commit on `main` upstream
    - Generate changelog entries based on pull requests here, and in Ruff
    - Bump the versions in the `pyproject.toml` and `dist-workspace.toml`
    - Update the generated reference documentation in `docs/reference`

1. Editorialize the `CHANGELOG.md` file to ensure entries are consistently styled.

    This usually involves simple edits, like consistent capitalization and leading verbs like
    "Add ...".

1. Create a pull request with the changelog and version changes

    The pull requests are usually titled as: `Bump version to <version>`.

    Binary builds will automatically be tested for the release.

1. Merge the pull request.

1. Run the [release workflow](https://github.com/astral-sh/ty/actions/workflows/release.yml) with
    the version tag.

    **Do not include a leading `v`**.

    When running the release workflow for pre-release versions, use the Cargo version format (not PEP
    440), e.g. `0.0.0-alpha.5` (not `0.0.0a5`). For stable releases, these formats are identical.

    The release will automatically be created on GitHub after the distributions are published.

1. Run `uv run --no-project ./scripts/update_schemastore.py`

    This script will prepare a branch to update the `ty.json` schema in the `schemastore`
    repository.

    Follow the link in the script's output to submit the pull request.

    The script is a no-op if there are no schema changes.

1. If necessary, update and release [`ty-vscode`](https://github.com/astral-sh/ty-vscode).

    The instructions are in the `ty-vscode` repository.

    Updating the extension bumps the bundled ty version, which is used if ty is not installed.

    Updating the extension is required for:

    - Minor releases
    - Patch releases, if a critical bug in `ty server` is fixed
    - When releasing new `ty server` features that require changes in `ty-vscode`
