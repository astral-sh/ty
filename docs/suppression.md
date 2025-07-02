# Suppression

Rules can also be ignored in specific locations in your code (instead of disabling the rule
entirely) to silence false positives or permissible violations.

!!! note

    To disable a rule entirely, set it to the `ignore` level as described in [rule levels](#rule-levels).

## ty suppression comments

To suppress a rule violation inline add a `# ty: ignore[<rule>]` comment at the end of the line:

```py
a = 10 + "test"  # ty: ignore[unsupported-operator]
```

Rule violations spanning multiple lines can be suppressed by adding the comment at the end of the
violation's first or last line:

```py
def add_three(a: int, b: int, c: int): ...

# on the first line

add_three(  # ty: ignore[missing-argument]
    3,
    2
)

# or, on the last line

add_three(
    3,
    2
)  # ty: ignore[missing-argument]
```

To suppress multiple violations on a single line, enumerate each rule separated by a comma:

```python
add_three("one", 5)  # ty: ignore[missing-argument, invalid-argument-type]
```

!!! note

    Enumerating rule names (e.g., `[rule1, rule2]`) is optional. However, we strongly recommend
    including suppressing specific rules to avoid accidental suppression of other errors.

## Standard suppression comments

ty supports the standard [`type:ignore`](https://typing.python.org/en/latest/spec/directives.html#type-ignore-comments) comment
format introduced by PEP 484.

ty handles these similarly to `ty: ignore` comments, but suppresses all violations on that line,
even when `type: ignore[code]` is used.

```python
# Ignore all typing errors on the next line
add_three("one", 5)  # type: ignore
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

def add_three(a: int, b: int, c: int):
    a + b + c

@no_type_check
def main():
    add_three(3, 4)
```

Decorating a class with `@no_type_check` isn't supported.
