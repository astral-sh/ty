# ty CLI Documentation

`ty` is an extremely fast Python type checker and language server, written in Rust. This document describes the command-line interface for the `ty` tool.

## Installation

```shell
uv tool install ty
```

## Commands

The `ty` CLI has the following main commands:

### `ty check`

Check Python files for type errors.

```shell
ty check [OPTIONS] [PATHS]...
```

#### Arguments

- `PATHS`: Files or directories to check. If not specified, the current directory is used.

#### Options

- `--project PATH`: Run within a given project directory.
- `--python PATH`: Path to Python installation for resolving type information.
- `--typeshed PATH`: Custom directory for stdlib typeshed stubs.
- `--extra-search-path PATH`: Additional module-resolution source paths.
- `--python-version VERSION`: Python version to assume when resolving types (e.g., "3.10").
- `--python-platform PLATFORM`: Target platform to assume when resolving types.
- `--output-format FORMAT`: Format for printing diagnostic messages (`full` or `concise`).
- `--color WHEN`: Control when colored output is used (`auto`, `always`, or `never`).
- `--error-on-warning`: Use exit code 1 if there are warning-level diagnostics.
- `--exit-zero`: Always use exit code 0, even with error-level diagnostics.
- `--watch`, `-W`: Watch files for changes and recheck changed files.
- `--respect-ignore-files`: Respect file exclusions via `.gitignore` and similar files.

#### Rule Configuration

- `--error RULE`: Treat rule as having severity 'error'.
- `--warn RULE`: Treat rule as having severity 'warn'.
- `--ignore RULE`: Disable a rule.

### `ty server`

Start the language server, which can be used with editors that support the Language Server Protocol (LSP).

```shell
ty server [OPTIONS]
```

## Examples

### Type check a single file

```shell
ty check myfile.py
```

### Type check an entire project

```shell
ty check .
```

### Type check with specific Python version

```shell
ty check --python-version 3.9 myproject/
```

### Watch mode for continuous checking

```shell
ty check --watch myproject/
```

### Ignore specific rules

```shell
ty check --ignore untyped-def --ignore unreachable myproject/
```

## Configuration

The behavior of `ty` can be configured using a `pyproject.toml` file in your project root. See the main documentation for details on configuration options.
