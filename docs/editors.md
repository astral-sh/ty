# Editor integration

ty can be integrated with various editors to provide a seamless development experience.

Learn more about ty's editor features in the [language server](./features/language-server.md)
documentation.

## VS Code

The Astral team maintains an official VS Code extension.

Install the [ty extension](https://marketplace.visualstudio.com/items?itemName=astral-sh.ty) from the VS Code Marketplace.

Then disable the language server from the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) by adding the
following [setting](https://code.visualstudio.com/docs/python/settings-reference#_intellisense-engine-settings) to your `settings.json` to avoid running two language servers:

```json
{
  "python.languageServer": "None"
}
```

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
        // Disable basedpyright and enable ty, and otherwise
        // use the default configuration.
        "ty",
        "!basedpyright",
        "..."
      ]
    }
  }
}
```

You can override the `ty` executable Zed uses by setting `lsp.ty.binary`:

```json
{
  "lsp": {
    "ty": {
      "binary": {
        "path": "/home/user/.local/bin/ty",
        "arguments": ["server"]
      }
    }
  }
}
```

More information in [Zed's documentation](https://zed.dev/docs/languages/python#configure-python-language-servers-in-zed).

## PyCharm

Starting with version 2025.3, PyCharm users can enable native ty support in the settings:

1. Go to **Python | Tools | ty** in the Settings dialog.

1. Select the **Enable** checkbox.

1. In the Execution mode setting, select how PyCharm should search for the executable:

    **Interpreter** mode: PyCharm searches for an executable installed in your interpreter. To install the ty package for the selected interpreter, click _Install ty_.

    **Path** mode: PyCharm searches for an executable in `$PATH`. If the executable is not found, you can specify the path by clicking the Browse... icon.

1. Select which options should be enabled.

For more information, refer to [PyCharm documentation](https://www.jetbrains.com/help/pycharm/lsp-tools.html#ty).

## Other editors

ty can be used with any editor that supports the [language server
protocol](https://microsoft.github.io/language-server-protocol/).

To start the language server, use the `server` subcommand:

```shell
ty server
```

Refer to your editor's documentation to learn how to connect to an LSP server.

## Settings

See the [editor settings reference](./reference/editor-settings.md) for more details on configuring the language
server.
