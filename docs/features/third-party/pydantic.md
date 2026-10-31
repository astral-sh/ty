# Pydantic

ty has built-in support for Pydantic v2 models. It uses a model's field declarations and settings
to check constructor calls and infer the types of model attributes.

Pydantic validates data while your program runs. Whether it accepts an input can depend on the
value itself or on what a custom validator does with it. ty checks your code before it runs, so it
can accept a call that fails at runtime or report an error for a call that succeeds.

## Constructor arguments in lax mode

In Pydantic's default *lax mode*, a constructor can accept several input types for the same field.
For example, Pydantic can convert a string to an integer.

```python
from pydantic import BaseModel


class RetryPolicy(BaseModel):
    attempts: int = 3


policy = RetryPolicy(attempts="5")
policy.attempts  # ty infers int. The value is 5.
```

In your editor, ty shows the `attempts` parameter as `LaxInt`. This is ty's name for the input
types it accepts for an `int` field in lax mode. It includes `str`, so ty also accepts
`RetryPolicy(attempts="five")`. Pydantic raises a `ValidationError` because it can't convert
`"five"` to an integer. [Pydantic's conversion table](https://docs.pydantic.dev/latest/concepts/conversion_table/)
lists the conditions for each conversion.

If you enable strict mode on the model with `model_config = ConfigDict(strict=True)` or on the
field with `Field(strict=True)`, ty reports an error for either string.

## Default values

ty checks a field's default against its declared type. For the `attempts: int` field above, ty
accepts `"5"` as a constructor argument but reports an error if you use the same string as the
default.

```python
from pydantic import BaseModel, Field


class RetryDefaults(BaseModel):
    attempts: int = Field(default="5")  # ty reports an invalid assignment.
```

By default, Pydantic skips validation when it uses a field's default value. `RetryDefaults().attempts`
would therefore be the string `"5"`, even though its annotation says `int`. Setting
`model_config = ConfigDict(validate_default=True)` makes Pydantic convert this default at runtime.
ty still flags the declaration. Use `5` as the default, or have a `default_factory` return an
`int`. See [Pydantic's guide to default validation](https://docs.pydantic.dev/latest/concepts/fields/#validate-default-values).

## Assignments and copies

ty also uses the declared field type when you update a model. It reports an error for
`policy.attempts = "5"`. By default, Pydantic stores the string as assigned. With
`validate_assignment=True`, Pydantic converts it to an integer, but ty still expects an `int` in
the assignment.

On Python 3.13 and later, ty checks the field names and values you pass to `copy.replace`. For
example, `copy.replace(policy, attempts="5")` is a type error. Pydantic copies the string without
validating it. If you use `policy.model_copy(update={...})` directly, ty doesn't check the entries
in the update dictionary against the model's fields.

## Unexpected keyword arguments

By default, Pydantic silently ignores unrecognized keyword arguments. For example,
`RetryPolicy(attempt=5)` succeeds despite the typo and uses the default of `3` for `attempts`.
ty warns about the discarded `attempt` argument. If you set `extra="allow"`, ty accepts extra
arguments. If you set `extra="forbid"`, it reports an error. See the
[discarded extra argument rule](../../reference/rules.md#pydantic-discarded-extra-argument).

## Known limitations

- **Field aliases.** ty recognizes a literal alias such as `Field(alias="retryCount")`. If you
    allow both the alias and the field name, ty can miss a required field when you omit both. If
    you use an alias generator, `AliasChoices`, or `AliasPath`, ty can report a missing argument for
    a call Pydantic accepts.
- **Dictionaries as model input.** In lax mode, you can pass a dictionary for a nested model. ty
    can accept an empty dictionary even when the nested model has required fields. Likewise, ty
    infers the return type of `RetryPolicy.model_validate(...)`, but it doesn't check the input
    dictionary field by field.
- **Custom validators.** If a field has a `@field_validator` with `mode="before"` or
    `mode="plain"`, ty accepts any input type for that constructor argument. The validator can still
    reject the value. Conversely, a wrap validator or a `BeforeValidator` in an `Annotated` field
    can accept inputs that ty rejects.
