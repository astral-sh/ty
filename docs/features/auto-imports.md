# Auto imports

ty can automatically add import statements for symbols from the standard library and third-party
packages. Just start typing and select the desired symbol from the autocomplete suggestions. For
example, try adding a `@dataclass` decorator to the `Person` class in the following code snippet.
Once the import is added, the error should be resolved.

<link rel="stylesheet" href="https://shark.fish/ty-embed/ty-embed.css">
<script type="module" src="../../js/ty-editor.js"></script>

<div class="ty-editor" data-height="350px">
<script type="text/template">
class Person:
    name: str
    age: int | None

alice = Person("Alice", 30)
</script>

</div>
