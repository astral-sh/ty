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
  init_options = {
    settings = {
      -- ty language server settings go here
    }
  }
})
```

For Neovim 0.11+ (with [`vim.lsp.config`](<https://neovim.io/doc/user/lsp.html#vim.lsp.config()>)):

```lua
-- Optional: Only required if you need to update the language server settings
vim.lsp.config('ty', {
  init_options = {
    settings = {
      -- ty language server settings go here
    }
  }
})

-- Required: Enable the language server
vim.lsp.enable('ty')
```

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
