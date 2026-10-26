# Django

ty has built-in support for type inference of Django models when the `django-types` stub package is installed.

## Features

ty infers attribute types from Django model fields and recognizes attributes and methods
that Django generates.

We support the following features:

- Type inference and assignment checking for model fields, including nullable fields declared with `null=True`.
- Recognition of automatic `id` fields and the `pk` alias, whose type follows the model's primary key.
- Inference of types for forward foreign-key relationships and their generated `<field>_id` attributes.
    The ID type follows the related primary key or the field selected with `to_field`.
- Inference of return types for `get_<field>_display()` methods generated for fields with choices.
- Inference of return types for `get_next_by_<field>()` and `get_previous_by_<field>()` methods generated
    for non-nullable date and datetime fields.

### Fields and relationships

```python
from typing import reveal_type

from django.db import models


class Book(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=200)


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()


book = Book(isbn="9780140328721", title="Example")
review = Review(book=book, rating=5)
reveal_type(book.title)  # revealed: str
reveal_type(book.pk)  # revealed: str
reveal_type(review.book)  # revealed: Book
reveal_type(review.book_id)  # revealed: str
reveal_type(review.id)  # revealed: int
reveal_type(review.pk)  # revealed: int

book.title = 3  # error: [invalid-assignment]
```

### Generated methods

Django adds methods based on a field's options. ty infers their return types:

```python
class Article(models.Model):
    status = models.CharField(
        max_length=1, choices=[("D", "Draft"), ("P", "Published")]
    )
    published = models.DateField()


def show_generated_methods(article: Article) -> None:
    reveal_type(article.get_status_display())  # revealed: str
    reveal_type(article.get_next_by_published())  # revealed: Article
    reveal_type(article.get_previous_by_published())  # revealed: Article
```

## Setup

Install [`django-types`](https://github.com/sbdchd/django-types) in the
[Python environment ty uses for your project](../../modules.md#python-environment):

```shell
uv add --dev django-types
```

!!! note

    Support for the alternative `django-stubs` package is planned, but for now you must use `django-types` exclusively to avoid conflicting stub files.

## Differences from runtime behavior

Since ty checks your use of Django models statically, its results can sometimes differ from
Django's runtime behavior. The following sections describe notable instances of such behavior.

### Automatic primary keys

If you create an instance without supplying its automatic primary key, Django leaves `id` and
`pk` as `None` until the first save. ty gives these attributes type `int` throughout. For more
details, see [Django's guide to automatic primary keys](https://docs.djangoproject.com/en/5.2/ref/models/instances/#auto-incrementing-primary-keys).

### Assignments

Django accepts `book.title = 3` and converts the value to a string when saving it to the database.
The attribute on the instance remains an integer. ty reports an incompatible assignment because
it checks the value against the field's type.

## Known limitations

- ty does not yet check field values or field names in model constructors, or field names in queries.

- String references alone do not give ty enough information to infer a foreign key's target model.
    Rather, you must provide an explicit annotation to supply the target type:

    ```python
    class Review(models.Model):
        book: "models.ForeignKey[Book]" = models.ForeignKey(
            "Book", on_delete=models.CASCADE
        )
    ```

- ty does not recognize reverse relationship attributes, including those named with `related_name`.

- Field renaming with the `name` parameter is not fully reflected in attribute types.
