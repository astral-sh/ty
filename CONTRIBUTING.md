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

1. Run `./scripts/release.sh`

```shell
./scripts/release.sh
```

The release script will:

- Update the Ruff submodule to the latest commit on `main` upstream
- Generate changelog entries based on pull requests here, and in Ruff
- Bump the versions in the `pyproject.toml` and `dist-workspace.toml`

1. Editorialize the `CHANGELOG.md` file to ensure entries are consistently styled.
1. Create a pull request with the changelog and version changes, e.g., `Bump version to ...`.
    Binary builds will automatically be tested for the release.
1. Merge the PR
1. Run the [release workflow](https://github.com/astral-sh/ty/actions/workflows/release.yml) with the version
    tag. **Do not include a leading `v`**. The release will automatically be created on GitHub after
    everything else publishes.
1. Run `uv run --no-project  ./scripts/update_schemastore.py` to prepare a PR to update the `ty.json` schema in the schemastore repository.
    Follow the link in the script's output to submit the PR. The script is a no-op if there are no schema changes.
1. If necessary, update and release [`ty-vscode`](https://github.com/astral-sh/ty-vscode).
    Follow the instructions in the `ty-vscode` repository. Updating the extension is required when:
    - for minor releases to bump the bundled ty version
    - for patch releases after fixing an important bug in `ty lsp` to bump the bundled ty version
    - when releasing new `ty lsp` features that require changes in `ty-vscode`

When running the release workflow for pre-release versions, use the Cargo version format (not PEP
440), e.g. `0.0.0-alpha.5` (not `0.0.0a5`). For stable releases, these formats are identical.
