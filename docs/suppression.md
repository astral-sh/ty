# Suppression

Rules can also be ignored in specific locations in your code (instead of disabling the rule
entirely) to silence false positives or permissible violations.

!!! note

    To disable a rule entirely, set it to the `ignore` level as described in [rule levels](rules.md#rule-levels).

## ty suppression comments

To suppress a rule violation inline, add a `# ty: ignore[<rule>]` comment at the end of the line:

```py
a = 10 + "test"  # ty: ignore[unsupported-operator]
```

Rule violations spanning multiple lines can be suppressed by adding the comment at the end of the
violation's first or last line:

<!-- fmt:off -->

```py
def sum_three_numbers(a: int, b: int, c: int) -> int: ...

# on the first line

sum_three_numbers(  # ty: ignore[missing-argument]
    3,
    2
)

# or, on the last line

sum_three_numbers(
    3,
    2
)  # ty: ignore[missing-argument]
```

<!-- fmt:on -->

To suppress multiple violations on a single line, enumerate each rule separated by a comma:

```python
sum_three_numbers("one", 5)  # ty: ignore[missing-argument, invalid-argument-type]
```

To suppress specific rules for an entire file, place a `# ty: ignore[<rule>]` comment on its own
line before any Python code:

```python
# ty: ignore[invalid-argument-type]

sum_three_numbers(3, 2, "1")
```

!!! note

    Enumerating rule names (e.g., `[rule1, rule2]`) is optional. However, we strongly recommend
    including specific rules to avoid accidental suppression of other errors.

## Standard suppression comments

ty supports the standard [`type: ignore`](https://typing.python.org/en/latest/spec/directives.html#type-ignore-comments) comment
format introduced by PEP 484.

`type: ignore` suppresses all violations on that line.

`type: ignore[ty:<rule>]` behaves like `ty: ignore[<rule>]` and only suppresses the matching
rule. Codes without a `ty:` prefix are ignored, which makes it possible to combine
suppressions for multiple type checkers in a single comment.

```python
# Ignore all typing errors on the next line
sum_three_numbers("one", 5)  # type: ignore

# Ignore a mypy code and a ty rule in the same comment
sum_three_numbers("one", 5, 2)  # type: ignore[arg-type, ty:invalid-argument-type]
```

## Multiple suppression comments

To suppress a typing error on a line that already has a suppression comment from another tool,
add the `# ty: ignore` comment to the same line.

For example, to suppress a type error and disable formatting for a specific line:

```python
result = calculate()  # ty: ignore[invalid-argument-type]  # fmt: skip

# or
result = calculate()  # fmt: off  # ty: ignore[invalid-argument-type]
```

## Unused suppression comments

If the [`unused-ignore-comment`](./reference/rules.md#unused-ignore-comment) rule is enabled, ty
will report unused `ty: ignore` and `type: ignore` comments.

`unused-ignore-comment` violations can only be suppressed using `# ty: ignore[unused-ignore-comment]`.
They cannot be suppressed using `# ty: ignore` without a rule code or `# type: ignore`.

## `@no_type_check` directive

ty supports the
[`@no_type_check`](https://typing.python.org/en/latest/spec/directives.html#no-type-check) decorator
to suppress all violations inside a function.

```python
from typing import no_type_check


def sum_three_numbers(a: int, b: int, c: int) -> int:
    return a + b + c


@no_type_check
def main():
    sum_three_numbers(1, 2)  # no error for the missing argument
```

Decorating a class with `@no_type_check` isn't supported.

## Baselines

!!! note "Preview"

    Baselines require ty 0.0.93 or later. The file format may change during preview. If ty can't
    read your baseline after an upgrade, [regenerate it](#create-a-baseline) with `--update-baseline`.

When you introduce ty to an existing project or enable a new rule, you may have more rule violations
than you can fix at once. One option is to run [`ty check --add-ignore`](./reference/cli.md#ty-check--add-ignore)
to suppress them all with inline ignore comments.

If you prefer to keep these suppressions out of your source files, use a baseline. A baseline is
a JSON file that records existing rule violations. On subsequent runs, `ty check` skips matching
violations so you can focus on those introduced by new or modified code.

In your editor, ty still shows matching violations as hints so you can fix them as you work on
the relevant code. If there's no practical fix for a violation, prefer an
[inline ignore comment](#ty-suppression-comments) to acknowledge it.

### Create a baseline

Run `ty check` with `--update-baseline` from the project root to record existing violations.

```shell
ty check --update-baseline --baseline ty-baseline.json
```

To use this baseline on subsequent checks, pass
[`--baseline ty-baseline.json`](./reference/cli.md#ty-check--baseline) to `ty check` or set
[`baseline`](./reference/configuration.md#baseline) in your `pyproject.toml` or `ty.toml`.

=== "pyproject.toml"

    ```toml
    [tool.ty]
    baseline = "ty-baseline.json"
    ```

=== "ty.toml"

    ```toml
    baseline = "ty-baseline.json"
    ```

Commit the baseline with your configuration so other contributors and CI use the same file.

If you want GitHub to collapse the baseline diff by default in pull requests, mark `ty-baseline.json` as
generated in the `.gitattributes` file at the repository root.

```gitattributes
/ty-baseline.json linguist-generated=true
```

### When to update the baseline

Update the baseline after you fix a violation or if one reappears in `ty check` output, for
example after a file rename. You can also update it to suppress existing violations of a newly
enabled rule.

First run `ty check` to review any new violations. Then run `ty check --update-baseline` to
add them to the baseline and remove entries for violations you've fixed.

ty's baseline support was inspired by
[basedpyright](https://docs.basedpyright.com/latest/benefits-over-pyright/baseline/).
