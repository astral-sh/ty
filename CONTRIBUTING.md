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

```
git clone https://github.com/astral-sh/ty.git
```

Then, ensure the submodule is initialized:

```
git submodule update --init --recursive
```
