# Diagnostics

ty provides diagnostics that include snippets of your source code, annotations and helpful
explanations. It will sometimes also provide suggestions on how to fix the reported issues.

## Example: Typed dictionaries

In this first example, ty detected an invalid assignment to a `TypedDict` key. Notice how the
diagnostic includes both the context around the line with the error, as well as the reference to the
`age` item in the `TypedDict` definition:

![TypedDict invalid-assignment diagnostic](screenshots/diagnostics1.dark.png#only-dark)
![TypedDict invalid-assignment diagnostic](screenshots/diagnostics1.light.png#only-light)

When a `TypedDict` key is misspelled, ty will suggest the correct spelling. If you are using an
editor with language server support, you can also apply this suggestion as a quick fix:

![TypedDict misspelled-key diagnostic](screenshots/diagnostics2.dark.png#only-dark)
![TypedDict misspelled-key diagnostic](screenshots/diagnostics2.light.png#only-light)

## Example: Invalid arguments

Here, a file has been opened for writing in text mode, but we are trying to write bytes to it.
The diagnostic points out the type mismatch and also includes the corresponding parameter in the
function definition for `write`:

![Invalid arguments diagnostic](screenshots/diagnostics3.dark.png#only-dark)
![Invalid arguments diagnostic](screenshots/diagnostics3.light.png#only-light)

## Example: Backwards compatibility

Instead of just telling you that `tomllib` can not be found, ty will tell you *why* it is not
available for your project. In this case, your project is targeting Python 3.10, but `tomllib` was
only added in Python 3.11:

![Missing import diagnostic](screenshots/diagnostics4.dark.png#only-dark)
![Missing import diagnostic](screenshots/diagnostics4.light.png#only-light)
