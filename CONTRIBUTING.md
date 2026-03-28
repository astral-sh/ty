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

ty's command-line help text, and part of `docs/reference/`, are auto-generated from Rust code in the Ruff
repository, using generation scripts that live in
[`crates/ruff_dev/src/`](https://github.com/astral-sh/ruff/blob/main/crates/ruff_dev/src/):

- [Configuration options](https://docs.astral.sh/ty/reference/configuration/), from
    [ruff/crates/ty_project/src/metadata/options.rs](https://github.com/astral-sh/ruff/blob/main/crates/ty_project/src/metadata/options.rs)
- [Rules](https://docs.astral.sh/ty/reference/rules/), from
    [ruff/crates/ty_python_semantic/src/](https://github.com/astral-sh/ruff/blob/main/crates/ty_python_semantic/src/)
- [Command-line interface reference](https://docs.astral.sh/ty/reference/cli/), from
    [ruff/crates/ty/src/args.rs](https://github.com/astral-sh/ruff/blob/main/crates/ty/src/args.rs)

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

You can optionally install prek hooks to automatically run the validation checks
when making a commit:

```shell
uv tool install prek
prek install
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

To restore the Ruff submodule to a clean-state, reset, then update it:

```shell
git submodule update --init --recursive
```
