# Suppression

Rules can also be ignored in specific locations in your code (instead of disabling the rule
entirely) to silence false positives or permissible violations.

!!! note

    To disable a rule entirely, set it to the `ignore` level as described in [rule levels](rules.md/#rule-levels).

## ty suppression comments

To suppress a rule violation inline add a `# ty: ignore[<rule>]` comment at the end of the line:

```py
a = 10 + "test"  # ty: ignore[unsupported-operator]
```

After Python code has begun, you can also place the comment on its own line before the affected
statement. It applies to the following logical line:

```py
a = 10
# ty: ignore[unsupported-operator]
b = a + "test"
```

Inside a multiline statement, an own-line comment applies only to the next non-comment physical
line.

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

`type: ignore` suppresses all violations on the same line. A standalone `# type: ignore` before
any Python code, including docstrings and imports, suppresses all violations in the file.

`type: ignore[ty:<rule>]` only suppresses the matching rule. Codes without a `ty:` prefix are
ignored, which makes it possible to combine suppressions for multiple type checkers in a single
comment. A standalone `# type: ignore[ty:<rule>]` before any Python code suppresses the matching
rule for the entire file.

Unlike `ty: ignore`, a standalone `type: ignore` after Python code has begun does not suppress the
following line.

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

If enabled, the [`unused-ignore-comment`](./reference/rules.md#unused-ignore-comment) rule reports
unused `ty: ignore` comments, and [`unused-type-ignore-comment`](./reference/rules.md#unused-type-ignore-comment)
reports unused `type: ignore` comments.

These violations can be suppressed by explicitly naming `unused-ignore-comment`, using either
`# ty: ignore[unused-ignore-comment]` or `# type: ignore[ty:unused-ignore-comment]`. A bare
`# ty: ignore` or `# type: ignore` does not suppress them.

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
