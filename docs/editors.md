# Editor integration

ty can be integrated with various editors to provide a seamless development experience.

## VS Code

The Astral team maintains an official VS Code extension.

Install the [ty extension](https://marketplace.visualstudio.com/items?itemName=astral-sh.ty) from the VS Code Marketplace.

See the extension's [README](https://github.com/astral-sh/ty-vscode) for more details on usage.

## Neovim

For Neovim 0.10 or earlier (with [`nvim-lspconfig`](https://github.com/neovim/nvim-lspconfig)):

```lua
require('lspconfig').ty.setup({
  settings = {
    ty = {
      -- ty language server settings go here
    }
  }
})
```

For Neovim 0.11+ (with [`vim.lsp.config`](<https://neovim.io/doc/user/lsp.html#vim.lsp.config()>)):

```lua
-- Optional: Only required if you need to update the language server settings
vim.lsp.config('ty', {
  settings = {
    ty = {
      -- ty language server settings go here
    }
  }
})

-- Required: Enable the language server
vim.lsp.enable('ty')
```

## Zed

ty is included with Zed out of the box (no extension required), although the default primary LSP for Python is basedpyright.

You can enable ty and disable basedpyright by adding this to your `settings.json` file:

```json
{
  "languages": {
    "Python": {
      "language_servers": [
        // Disable basedpyright and enable Ty, and otherwise
        // use the default configuration.
        "ty",
        "!basedpyright",
        "..."
      ]
    }
  }
}
```

More information in [Zed's documentation](https://zed.dev/docs/languages/python#configure-python-language-servers-in-zed).

## Other editors

ty can be used with any editor that supports the [language server
protocol](https://microsoft.github.io/language-server-protocol/).

To start the language server, use the `server` subcommand:

```shell
ty server
```

Refer to your editor's documentation to learn how to connect to an LSP server.

See the [editor settings](./reference/editor-settings.md) for more details on configuring the language
server.
