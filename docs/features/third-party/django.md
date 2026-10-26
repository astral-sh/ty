# Django

Django adds attributes and methods to model classes when it loads an application. Since version
0.0.92, ty can infer many of these from the model's field declarations, including primary keys,
foreign key IDs, and methods generated for individual fields. Some relationships depend on how
Django connects models across the application, so ty can report a missing attribute that exists
at runtime.

## Setup

Install [`django-types`](https://github.com/sbdchd/django-types) in the
[Python environment ty uses for your project](../../modules.md#python-environment). This package
provides type stubs that describe Django's classes and their methods. In a uv project, add it as
a development dependency.

```shell
uv add --dev django-types
```

If you also use mypy with `django-stubs`, keep the two stub packages in separate environments.
They install files at the same paths.

## Model fields and relationships

```python
from django.db import models


class Author(models.Model):
    code = models.CharField(max_length=12, primary_key=True)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

For a `Book` instance, ty infers `Author` for `book.author` and `str` for `book.author_id`, because
the foreign key stores the author's `code`. If you specify `to_field`, the ID takes the type of
that field. With `null=True`, both the related object and its ID can be `None`.

`Book` has no explicit primary key, so ty infers `int` for both `book.id` and `book.pk`. It gives
them that type even on a new `Book()` instance, where Django leaves the automatic key as `None`
until the first save. See [Django's guide to automatic primary keys](https://docs.djangoproject.com/en/5.2/ref/models/instances/#auto-incrementing-primary-keys).
Since version 0.0.93, ty also recognizes that an abstract model doesn't get an automatic `id` of
its own.

ty also recognizes methods Django generates for individual fields. If you add a `status` field
with `choices` to `Book`, ty infers `str` for `book.get_status_display()`. For a non-nullable
`DateField` or `DateTimeField` named `published`, it infers `Book` for `book.get_next_by_published()`
and `book.get_previous_by_published()`.

## Field assignments, constructors, and queries

ty checks the type of a value assigned to a field. For example, it reports an error for
`book.title = 3` because `title` is a `CharField`. It doesn't yet check the same value passed to
the model constructor, so it accepts `Book(title=3)`.

ty can also miss an unknown field name in a constructor or query. For example, ty accepts both
`Book(writer=author)` and `Book.objects.filter(writer=author)`. Django raises a `TypeError` for
the constructor and a `FieldError` for the query because `Book` has no `writer` field.

## Known limitations

- **String references.** If you write `ForeignKey("Author", ...)`, Django resolves the model
    name when it loads the application. ty infers `Unknown` for both `book.author` and
    `book.author_id` from the string alone. You can keep the string reference and give ty the
    target type with an explicit field annotation.

    ```python
    author: "models.ForeignKey[Author]" = models.ForeignKey(
        "Author", on_delete=models.CASCADE
    )
    ```

- **Reverse relationships.** Django adds `author.book_set` so you can look up an author's books.
    ty reports that the attribute is missing. It also misses a reverse relationship named
    explicitly with `related_name`.

- **Renamed fields.** If you declare `views = models.IntegerField(name="view_count")`, Django
    exposes the field as `view_count`. ty recognizes `views` and reports an error when you use
    `view_count`.
