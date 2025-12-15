# Language server

You can generally expect ty to be a fully-featured [language server] for Python.
This page describes some of the key features provided by ty's IDE integration and includes
a reference table of supported LSP features at the end.
See the [editor integration](../editors.md) documentation for instructions on how to set up ty
with your editor.

## Diagnostics

<figure markdown="span">
  ![](screenshots/inline-diagnostics.png)
  <figcaption>Example of an inline diagnostic with code-span annotations</figcaption>
</figure>

ty reports type errors and other [diagnostics](./diagnostics.md) directly in your editor. Diagnostics
are updated as you type. You can use the
[`diagnosticMode`](../reference/editor-settings.md#diagnosticmode) setting to control if you want to
see diagnostics for the current file only or for your entire workspace.

!!! info

    ty supports both the "pull" and "push" diagnostic models. Most modern editors will use the "pull" model
    for better performance, where diagnostics are fetched on demand rather than pushed after every
    change.

## Code Navigation

<figure markdown="span">
  ![](screenshots/find-references.png)
  <figcaption>"Find references" shows usages across the entire workspace</figcaption>
</figure>

ty powers several language server features that allow you to navigate a Python codebase:

- **Go to Definition**: Jump to where a symbol is defined. ty resolves imports, function calls,
    class references, and more.
- **Go to Declaration**: Navigate to the declaration site of a symbol, which can differ from its
    definition (could be in a stub file).
- **Go to Type Definition**: Navigate to the type of a symbol. For example, this takes you to the class `Person`
    when invoked on a variable `user: Person`.
- **Find all references**: Find every usage of a function, class, or variable across your entire workspace.
- **Document and workspace symbols**: See an outline of or search through symbols in the current file, or across your entire workspace.

## Code completions

<figure markdown="span">
  ![Code completion example](screenshots/code-completion.png){ width="500" }
  <figcaption>Accepting this completion will automatically add a <code>subprocess</code> import at the top of the file.</figcaption>
</figure>

ty provides intelligent code completions as you type, offering suggestions for variables, functions, classes, and modules that are in scope.
For symbols that are not yet imported, ty suggests auto-import actions to add the necessary `import` statements.

## Code actions and refactorings

<figure markdown="span">
  ![Code action example](screenshots/quick-fix.png){ width="700" }
  <figcaption>ty offers to remove the unused suppression comment</figcaption>
</figure>

ty offers quick fixes and other code actions to help you resolve issues:

- **Add import**: Automatically add missing import statements
- **Quick fixes**: Some diagnostics come with quick fix suggestions to resolve the issue
- **Rename symbol**: Safely rename symbols across your entire codebase
- **Selection range**: Expand or shrink the text selection in your editor based on ty's understanding of Python syntax

## Contextual information

<figure markdown="span">
  ![Inlay hints](screenshots/inlay-hints.png)
  <figcaption>Gray inlay hints and hover information</figcaption>
</figure>

ty surfaces useful contextual information as you code:

- **Hover**: Hover over any symbol to see its type, documentation, function signatures, and other
    useful information like the variance of type parameters.
- **Inlay hints**: Display inline type hints for variables and parameters without explicit
    annotations, as well as parameter names at call sites. These hints can also be double-clicked
    to persist the type annotations in your source code. You can also click on parts of the inlay
    hints for go-to-definition navigation.
- **Signature help**: When calling a function, ty displays the function's parameters and their
    types. This appears automatically when you type `(` and updates as you navigate between arguments.
- **Document highlight**: When the cursor is on a symbol, ty highlights all occurrences of that
    symbol in the current file.
- **Semantic highlighting**: Syntax highlighting based on the underlying semantics and types.

## Notebook support

ty supports Jupyter notebooks (`.ipynb` files) with language server features. Each cell is
analyzed in context, with diagnostics, completions, and other features working across cells.

## Feature reference

<!-- markdownlint-disable MD060 -->

| Feature                                               | Status           | Notes                     |
| ----------------------------------------------------- | ---------------- | ------------------------- |
| [`callHierarchy/*`][callhierarchy]                    | ❌ Not supported |                           |
| [`notebookDocument/*`][notebookdocument]              | ✅ Supported     |                           |
| [`textDocument/codeAction`][codeaction]               | ✅ Supported     | Quick fixes               |
| [`textDocument/codeLens`][codelens]                   | ❌ Not supported |                           |
| [`textDocument/completion`][completion]               | ✅ Supported     |                           |
| [`textDocument/declaration`][declaration]             | ✅ Supported     |                           |
| [`textDocument/definition`][definition]               | ✅ Supported     |                           |
| [`textDocument/diagnostic`][diagnostic]               | ✅ Supported     |                           |
| [`textDocument/documentColor`][documentcolor]         | ❌ Not supported |                           |
| [`textDocument/documentHighlight`][documenthighlight] | ✅ Supported     |                           |
| [`textDocument/documentLink`][documentlink]           | ❌ Not supported |                           |
| [`textDocument/documentSymbol`][documentsymbol]       | ✅ Supported     |                           |
| [`textDocument/foldingRange`][foldingrange]           | ❌ Not supported |                           |
| [`textDocument/formatting`][formatting]               | —                | Use [Ruff] for formatting |
| [`textDocument/hover`][hover]                         | ✅ Supported     |                           |
| [`textDocument/implementation`][implementation]       | ❌ Not supported |                           |
| [`textDocument/inlayHint`][inlayhint]                 | ✅ Supported     |                           |
| [`textDocument/onTypeFormatting`][ontypeformatting]   | ❌ Not supported |                           |
| [`textDocument/prepareRename`][preparerename]         | ✅ Supported     |                           |
| [`textDocument/rangeFormatting`][rangeformatting]     | —                | Use [Ruff] for formatting |
| [`textDocument/references`][references]               | ✅ Supported     |                           |
| [`textDocument/rename`][rename]                       | ✅ Supported     |                           |
| [`textDocument/selectionRange`][selectionrange]       | ✅ Supported     |                           |
| [`textDocument/semanticTokens`][semantictokens]       | ✅ Supported     |                           |
| [`textDocument/signatureHelp`][signaturehelp]         | ✅ Supported     |                           |
| [`textDocument/typeDefinition`][typedefinition]       | ✅ Supported     |                           |
| [`typeHierarchy/*`][typehierarchy]                    | ❌ Not supported | [#534]                    |
| [`workspace/diagnostic`][workspacediagnostic]         | ✅ Supported     |                           |
| [`workspace/symbol`][workspacesymbol]                 | ✅ Supported     |                           |
| [`workspace/willRenameFiles`][willrenamefiles]        | ❌ Not supported | [#1560]                   |

[#1560]: https://github.com/astral-sh/ty/issues/1560
[#534]: https://github.com/astral-sh/ty/issues/534
[callhierarchy]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#callHierarchy_incomingCalls
[codeaction]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_codeAction
[codelens]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_codeLens
[completion]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_completion
[declaration]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_declaration
[definition]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_definition
[diagnostic]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_diagnostic
[documentcolor]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_documentColor
[documenthighlight]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_documentHighlight
[documentlink]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_documentLink
[documentsymbol]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_documentSymbol
[foldingrange]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_foldingRange
[formatting]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_formatting
[hover]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_hover
[implementation]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_implementation
[inlayhint]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_inlayHint
[language server]: https://microsoft.github.io/language-server-protocol/
[notebookdocument]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#notebookDocument_synchronization
[ontypeformatting]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_onTypeFormatting
[preparerename]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_prepareRename
[rangeformatting]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_rangeFormatting
[references]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_references
[rename]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_rename
[ruff]: https://docs.astral.sh/ruff/
[selectionrange]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_selectionRange
[semantictokens]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_semanticTokens
[signaturehelp]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_signatureHelp
[typedefinition]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_typeDefinition
[typehierarchy]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#typeHierarchy_supertypes
[willrenamefiles]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#workspace_willRenameFiles
[workspacediagnostic]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#workspace_diagnostic
[workspacesymbol]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#workspace_symbol
