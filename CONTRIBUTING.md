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

```bash
git -C ruff reset --hard
git submodule update
```
