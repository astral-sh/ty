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

## Documentation

To preview any changes to the documentation locally run the development server with:

```shell
uvx --with-requirements docs/requirements.txt -- mkdocs serve -f mkdocs.yml
```

The documentation should then be available locally at
[http://127.0.0.1:8000/ty/](http://127.0.0.1:8000/ty/).

To update the documentation dependencies, edit `docs/requirements.in`, then run:

```shell
uv pip compile docs/requirements.in -o docs/requirements.txt --universal -p 3.12
```

Documentation is deployed automatically on release by publishing to the
[Astral documentation](https://github.com/astral-sh/docs) repository, which itself deploys via
Cloudflare Pages.

After making changes to the documentation, format the markdown files with:

```shell
npx prettier --prose-wrap always --write "**/*.md"
```

## Releasing ty

Releases can only be performed by Astral team members.

Preparation for the release is automated.

1. Install the prek hooks as described above, if you haven't already.

1. Checkout the `main` branch and run `git pull origin main --recurse-submodules --tags`.

1. Create and checkout a new branch for the release.

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
    440), e.g. `0.0.1-alpha.5` (not `0.0.1a5`). For stable releases, these formats are identical.

    The release will automatically be created on GitHub after the distributions are published.

1. Run `uv run --no-project ./scripts/update_schemastore.py`

    This script will prepare a branch to update the `ty.json` schema in the `schemastore`
    repository.

    Follow the link in the script's output to submit the pull request.

    The script is a no-op if there are no schema changes.

1. Update and release `ty-vscode`.

    The instructions are [in the `ty-vscode`
    repository](https://github.com/astral-sh/ty-vscode/blob/main/CONTRIBUTING.md#release).

## Updating ty's conformance results upstream

One way in which type checkers can be evaluated is by how well they do on the [typing conformance test suite](https://github.com/python/typing/tree/main/conformance),
which contains a number of assertions to test whether type checkers adhere to the rules laid out in
the typing spec. ty's results are uploaded to the upstream `python/typing` repo so that users can
compare ty's conformance score with other type checkers. Updating these results is partially, but
not fully, automated.

To update ty's conformance results upstream after a release:

1. Clone <https://github.com/python/typing> and checkout a new branch
1. Run `cd conformance`
1. Run `uv sync --update-package=ty`
1. Run `uv run python src/main.py`. This step may update generated fields in TOML files (see below) and/or the `results.html` file.
1. Check to see if any manual changes are required and apply them as necessary (see below for details).
1. If you had to make any manual changes as part of the previous step, run `uv run python src/main.py` again. This second run should not update any further TOML files, but is necessary for regenerating `results.html` again.
1. Make a PR to the upstream repo.

### Manual changes that may be required to `.toml` files

The TOML files that contain the results for each type checker are partially generated.

The `conformance_automated`, `output` and `errors_diff` fields are all generated; these should never be altered:

- `output` is the raw output of the type checker on that file.
- `errors_diff` provides one line of output for every Python line where a diagnostic was expected from ty but didn't occur, and one line of output for every Python line where a diagnostic was not expected from ty but did occur.
- `conformance_automated`: this will always either be "Pass" (if `errors_diff` is an empty string) or "Fail" (if it is a non-empty string).

The other fields are manually entered and may need to be updated if any of the generated fields in a TOML file are altered by running `uv run python src/main.py`:

- `conformant`: This should be one of three values:
    - "Unsupported": none of the major features in the Python file are supported by ty
    - "Partial": some, but not all, of the features and assertions in the Python file are supported by ty. If this is given as the current status, a non-empty `notes` field should be provided that describes which features are currently supported and which are not.
    - "Pass": this should generally only be used if ty passes all assertions in the Python file and the generated `errors_diff` field is an empty string. In some rare occasions, it *may* be appropriate to label ty as conformant even if there is a non-empty `errors_diff` field, but you will generally need to provide a non-empty `ignore_errors` field if so.
- `notes`: if the score is given as "Partial" in the `conformant` field, this field should describe which assertions fail and which features are currently unsupported.
- `ignore_errors`: this is only required if the generated `errors_diff` field is nonempty but the score is nonetheless given as "Conformant". It should be a list of strings. Each string should be an error message that appears in the `errors_diff` field but should nonetheless be ignored when considering whether ty is conformant or not. If ty's score is given as "Conformant" with a non-empty `errors_diff` field, a verification check in CI in the `python/typing` repository will fail unless each error message listed in `errors_diff` is listed in that TOML file's `ignore_errors` field.
