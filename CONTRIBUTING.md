# Contributing

## Repository structure

ty's Rust crates can be found in the [Ruff](https://github.com/astral-sh/ruff) project. While the
relationship between these projects will evolve over time, they currently share foundational crates
and it's easiest to use a single repository for development. To contribute changes to ty's core,
open a pull request on the Ruff repository.

The Ruff repository is included as a submodule to allow ty's release tags to reflect an exact
snapshot of the Ruff project. The submodule is only updated on release. To see the latest
development code, visit the Ruff repository.

The ty repository only includes code relevant to distributing the ty project.

## Getting started with the ty repository

Clone the repository:

```bash
git clone https://github.com/astral-sh/ty.git
```

Then, ensure the submodule is initialized:

```bash
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

```bash
uv build
```

## Updating the Ruff commit

To update the Ruff submodule to the latest commit:

```bash
git -C ruff pull origin main
```

Or, to update the Ruff submodule to a specific commit:

```bash
git -C ruff checkout <commit>
```

To commit the changes:

```bash
commit=$(git -C ruff rev-parse --short HEAD)
git switch -c "sync/ruff-${commit}"
git add ruff
git commit -m "Update ruff submodule to https://github.com/astral-sh/ruff/commit/${commit}"
```

To restore the Ruff submodule to a clean-state, reset, then update the submodule:

```
git -C ruff reset --hard
git submodule update
```

To restore the Ruff submodule to the commit from `main`:

```bash
git -C ruff reset --hard $(git ls-tree main -- ruff | awk '{print $3}')
git add ruff
```

## Releasing ty

Releases can only be performed by Astral team members.

Preparation for the release is automated. First, run:

```shell
./scripts/release.sh
```

The release script will:

- Update the Ruff submodule to the latest commit on `main` upstream
- Generate changelog entries based on pull requests here, and in Ruff
- Bump the versions in the `pyproject.toml` and `dist-workspace.toml`

After running the script, editorialize the `CHANGELOG.md` file to ensure entries are consistently
styled.

Then, open a pull request, e.g., `Bump version to ...`.

Binary builds will automatically be tested for the release.

After merging the pull request, run the
[release workflow](https://github.com/astral-sh/ty/actions/workflows/release.yml) with the version
tag. **Do not include a leading `v`**. The release will automatically be created on GitHub after
everything else publishes.

When running the release workflow for pre-release versions, use the Cargo version format (not PEP
440), e.g. `0.0.0-alpha.5` (not `0.0.0a5`). For stable releases, these formats are identical.
