# Excluding files

ty automatically discovers all Python files in your project. You can customize where ty searches by using the [`src.include`](./reference/configuration.md#include) and [`src.exclude`](./reference/configuration.md#exclude) settings.

For example, with the following configuration, ty checks all Python files in the `src` and `tests` directories except those in the `src/generated` directory:

```toml
[tool.ty.src]
include = ["src", "tests"]
exclude = ["src/generated"]
```

By default, ty excludes a [variety of commonly ignored directories](./reference/configuration.md#exclude). If you want to include one of these directories, you can do so by adding a negative `exclude`:

```toml
[tool.ty.src]
# Remove `build` from the excluded directories.
exclude = ["!**/build/"]
```

By default, ty ignores files listed in an `.ignore` or `.gitignore` file. To disable this functionality, set [`respect-ignore-files`](./reference/configuration.md#respect-ignore-files) to `false`.

You may also explicitly pass the paths that ty should check, e.g.:

```shell
ty check src scripts/benchmark.py
```

Paths that are passed as positional arguments to `ty check` are included even if they would otherwise be ignored through `exclude` filters or an ignore-file.

## Include and exclude syntax

Both `include` and `exclude` support gitignore like glob patterns:

- `src/` matches a directory (including its contents) named `src`.
- `src` matches a file or directory (including its contents) named `src`.
- `*` matches any (possibly empty) sequence of characters (except `/`).
- `**` matches zero or more path components.
    This sequence **must** form a single path component, so both `./**a` and `./b**/` are invalid and will result in an error.
    A sequence of more than two consecutive `*` characters is also invalid.
- `?` matches any single character except `/`
- `[abc]` matches any character inside the brackets. Character sequences can also specify ranges of characters, as ordered by Unicode,
    so e.g. `[0-9]` specifies any character between `0` and `9` inclusive. An unclosed bracket is invalid.

All patterns are anchored: The pattern `src` only includes `<project_root>/src` but not something like `<project_root>/test/src`. To include any directory named `src`, use the prefix match `**/src`. The same applies for exclude patterns where `src` only excludes `<project_root>/src` but not something like `<project_root>/test/src`.

> [!NOTE]
> A prefix include pattern like `**/src` can notably slow down the Python file discovery.

All fields accepting patterns use the reduced portable glob syntax from [PEP 639](https://peps.python.org/pep-0639/#add-license-FILES-key), with the addition that characters can be escaped with a backslash.
