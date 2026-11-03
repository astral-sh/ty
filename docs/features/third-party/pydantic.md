# Pydantic

ty has built-in support for type inference of Pydantic v2 models.

## Features

ty infers constructor parameters and attribute types from your model fields. It checks for
missing required arguments and incompatible values while accounting for Pydantic's input
conversions and configuration.

We support the following features:

- Recognition of required fields, default values, and default factories.
- Recognition of literal field aliases and field metadata declared with `Field` or `Annotated`.
- Support for implicit conversions in lax mode and strict mode configured for a model
    or an individual field.
- Support for the model's `extra` configuration, including warnings about arguments Pydantic would discard.
- Rejection of assignments to read-only fields declared with `frozen=True` on a model or field.
- Support for inherited fields, generic models, and nested models.
- Support for `RootModel`, settings models derived from `pydantic_settings.BaseSettings`, and Pydantic
    dataclasses.

### Constructor arguments in lax mode

In Pydantic's default _lax mode_, a constructor can accept several input types for the same field.
For example, ty accepts a string for an integer field while inferring `int` for the resulting attribute:

```python
from typing import reveal_type

from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int = 0


user = User(name="Alice", age="30")
reveal_type(user)  # revealed: User
reveal_type(user.name)  # revealed: str
reveal_type(user.age)  # revealed: int

User()  # error: [missing-argument]
User(name="Alice", age=None)  # error: [invalid-argument-type]
```

Please consult [Pydantic's conversion table](https://docs.pydantic.dev/latest/concepts/conversion_table/) for comprehensive documentation of its runtime conversions.

### Strict mode

ty respects strict mode configured for an entire model with `model_config` or for an individual
field with `Field`. In strict mode, ty requires the declared field type and reports an error for
inputs that would require conversion:

```python
from pydantic import BaseModel, ConfigDict, Field


class StrictRetryPolicy(BaseModel):
    model_config = ConfigDict(strict=True)

    attempts: int = 3


class FieldStrictRetryPolicy(BaseModel):
    attempts: int = Field(default=3, strict=True)


StrictRetryPolicy(attempts="5")  # error: [invalid-argument-type]
FieldStrictRetryPolicy(attempts="5")  # error: [invalid-argument-type]
```

### Unexpected keyword arguments

ty warns about unrecognized constructor keyword arguments that Pydantic would silently discard.
This helps catch typos such as `attempt` instead of `attempts`:

```python
from pydantic import BaseModel


class RetryPolicy(BaseModel):
    attempts: int = 3


RetryPolicy(attempt=5)  # error: [pydantic-discarded-extra-argument]
```

At runtime, Pydantic ignores `attempt` and initializes `attempts` with its default value of `3`.
[ty warns by default about the discarded argument](../../reference/rules.md#pydantic-discarded-extra-argument).
ty also respects the model's `extra` configuration: `extra="allow"` accepts extra arguments,
while `extra="forbid"` reports an error.

## Differences from runtime behavior

Since ty checks your use of Pydantic models statically, its results can sometimes differ from Pydantic's runtime validation. The following sections describe notable instances of such behavior.

### Invalid values in lax mode

ty checks the types of constructor arguments, but does not perform Pydantic's runtime validation.
For example, it accepts `User(name="Alice", age="thirty")` in lax mode even though Pydantic cannot
convert `"thirty"` to an integer. Numeric field constraints such as `Field(gt=0)` are also checked
only at runtime. With [strict mode](#strict-mode) enabled, ty rejects string arguments for the
integer field.

### Default values

ty checks a field's default value against its declared type, even in lax mode:

```python
from pydantic import BaseModel, Field


class RetryPolicy(BaseModel):
    attempts: int = Field(default="5")  # error: [invalid-assignment]
```

This contrasts with the default runtime behavior of Pydantic, which skips validation and conversion of a field's default value entirely. You can change Pydantic's behavior in that respect by setting
`model_config = ConfigDict(validate_default=True)`, although ty will still emit an error for a non-integer default value. To avoid the ty error entirely, you must use an integer for the default.

### Assignments

As with [default values](#default-values), ty also uses the declared field type rather than a lax field type when you update a model:

```python
from pydantic import BaseModel


class RetryPolicy(BaseModel):
    attempts: int = 3


policy = RetryPolicy()
policy.attempts = "5"  # error: [invalid-assignment]
```

This contrasts with Pydantic's default behavior, which accepts the string assignment. You can change Pydantic's behavior in that respect by setting `validate_assignment=True` (in which case Pydantic will attempt conversion to an integer), but ty will still require an integer for the assignment.

## Known limitations

- Alias handling is incomplete when both field names and aliases are enabled, or when aliases
    use generators, `AliasChoices`, or `AliasPath`.
- ty does not check dictionary contents field by field when constructing nested models,
    calling `model_validate`, or updating a model with `model_copy`.
- ty does not fully model the input types accepted by custom validators.
