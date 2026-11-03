# pytest

pytest uses the name of a parameter to a test function to determine which fixture supplies its value. In your editor,
ty lets you jump from that parameter to its fixture definition, and it also lets you find the tests and other fixtures that use a given fixture.

## Navigating between fixtures and tests

Suppose `tests/conftest.py` defines a fixture named `database_path`. It uses pytest's built-in
[`tmp_path` fixture](https://docs.pytest.org/en/stable/how-to/tmp_path.html), which provides a unique
temporary directory for each test as a `pathlib.Path`.

```python title="tests/conftest.py"
from pathlib import Path

import pytest


@pytest.fixture
def database_path(tmp_path: Path) -> Path:
    return tmp_path / "test.db"
```

A test in `tests/test_database.py` requests the fixture by declaring a parameter with the same
name.

```python title="tests/test_database.py"
from pathlib import Path


def test_create_database_file(database_path: Path) -> None:
    database_path.touch()
    assert database_path.is_file()
```

To help navigate between those definitions, ty supports the following functionality:

- **Go to Definition** (`textDocument/definition`) on the test's `database_path` parameter jumps
    to the fixture function in `conftest.py`.

    ```text
     --> tests/test_database.py:4:31
      |
    4 | def test_create_database_file(database_path: Path) -> None:
      |                               ^^^^^^^^^^^^^ Selected parameter

     --> tests/conftest.py:7:5
      |
    7 | def database_path(tmp_path: Path) -> Path:
      |     ------------- Fixture definition
    ```

- **Find All References** (`textDocument/references`) on the fixture's function name finds the
    requesting test parameter and its uses.

    ```text
     --> tests/test_database.py:4:31
      |
    4 | def test_create_database_file(database_path: Path) -> None:
      |                               -------------
    5 |     database_path.touch()
      |     -------------
    6 |     assert database_path.is_file()
      |            -------------
    ```

    If the fixture declares an explicit name (i.e., `@pytest.fixture(name="database_path")`),
    invoking **Find All References** on the quoted name produces the same result.

## Where ty looks for fixtures

For a test parameter, ty searches for fixture definitions at the following locations (in order):

1. The test class and its base classes, if the test is a method.
1. The test module.
1. `conftest.py` files, starting in the test's directory and working up through its parent
    directories in the project.
1. The core plugins in your pytest installation.

## Known limitations

- When one fixture requests another, ty searches from the requesting fixture's definition. As a result, it can
    miss an override of the fixture that is visible only from the test from which the fixture is requested.
- ty does not yet discover fixtures registered by third-party plugins.
