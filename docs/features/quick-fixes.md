# Quick fixes

For certain types of diagnostics, ty can provide automatic quick fixes to help you resolve issues.
Quick fixes are available in editors that support the Language Server Protocol (LSP), such as VS Code
with the ty extension.

## How to use quick fixes

When ty detects an issue that has an available quick fix, your editor will typically display a
lightbulb icon or similar indicator. You can try it out here with the following code snippet:

<link rel="stylesheet" href="https://shark.fish/ty-embed/ty-embed.css">
<script type="module" src="../../js/ty-editor.js"></script>

<div class="ty-editor" data-height="370px">
<script type="text/template">
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int | None

def greet(person: Person):
    print("Hello", person["naem"])

greet({"name": "Alice", "age": 30})
</script>

</div>

Hover over the misspelled key, select "Quick Fix", and then "Fix invalid key". You can also try
deleting the `import` statement, and using the quick fix to add the missing import.
