# Editor integration

ty can be integrated with various editors to provide a seamless development experience.

Learn more about ty's editor features in the [language server](./features/language-server.md)
documentation.

## VS Code

The Astral team maintains an official VS Code extension.

Install the [ty extension](https://marketplace.visualstudio.com/items?itemName=astral-sh.ty) from the VS Code Marketplace.

The extension automatically disables the language server from the [Python
extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
to avoid running two Python language servers. This is done by setting
[`python.languageServer`](https://code.visualstudio.com/docs/python/settings-reference#_intellisense-engine-settings)
to `"None"` as a default configuration.

If you prefer to use ty only for type checking and want to use another language
server for capabilities like hover, auto-completions, etc., you can override
this by explicitly setting [`python.languageServer`](https://code.visualstudio.com/docs/python/settings-reference#_intellisense-engine-settings) and
[`ty.disableLanguageServices`](./reference/editor-settings.md#disablelanguageservices)
in your [`settings.json`](https://code.visualstudio.com/docs/configure/settings#_settings-json-file):

```jsonc
{
  "python.languageServer": "Pylance",
  "ty.disableLanguageServices": true,
}
```

## Neovim

The [nvim-lspconfig](https://github.com/neovim/nvim-lspconfig) extension is the
recommended way of using ty with Neovim (if you prefer not to install the extension,
you can copy [the ty configuration](https://github.com/neovim/nvim-lspconfig/blob/master/lsp/ty.lua)
manually instead). After installing the nvim-lspconfig extension, you need to enable
the language server (and can optionally configure additional settings). For Neovim >=0.11,
you can add the following snippet to your config file:

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

For Neovim \<0.11, you would use the configuration below instead (note that [you might need
to install an older version of nvim-lspconfig](https://github.com/neovim/nvim-lspconfig?tab=readme-ov-file#important-%EF%B8%8F)):

```lua
require('lspconfig').ty.setup({
  settings = {
    ty = {
      -- ty language server settings go here
    }
  }
})
```

## Zed

ty is included with Zed out of the box (no extension required), although the default primary LSP for Python is basedpyright.

You can enable ty and disable basedpyright by adding this to your `settings.json` file:

```json
{
  "languages": {
    "Python": {
      "language_servers": [
        // Enable ty and ruff,
        // Other built-in servers (basedpyright, pyright, pylsp)
        // are disabled by being omitted from this list.
        "ty",
        "ruff"
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

PyCharm has supported ty natively since 2025.3. In 2026.2, the ty settings moved to **External Tools**.

In PyCharm 2026.2 and 2026.3, open **Settings → Python → Tools → External Tools** and turn on the
switch in the **ty** row.

In **PyCharm 2026.3**, the **Lookup** column shows where PyCharm searches for ty, in this order:

1. **Env** checks for ty in the project environments.
1. **Path** uses an executable on `$PATH` or a path you specify.
1. **uvx** runs ty with [uv](https://docs.astral.sh/uv/) without installing it in a project environment.

Click the chevron next to **ty** or click the **ty** row to open its settings. See the
[PyCharm 2026.3 documentation](https://www.jetbrains.com/help/pycharm/2026.3/lsp-tools.html#external-tools-settings).

In **PyCharm 2026.2**, select a method in the **Lookup** column:

- **Sdk** looks for ty in the module's Python interpreter, then on `$PATH`, and falls back to `uvx`.
- **Path** looks for ty on `$PATH` and falls back to `uvx`.
- **uvx** runs ty with [uv](https://docs.astral.sh/uv/) without requiring ty in your project or on `$PATH`.

Click the gear icon in the **ty** row to open **Configure ty**. See the
[PyCharm 2026.2 documentation](https://www.jetbrains.com/help/pycharm/2026.2/lsp-tools.html#external-tools-settings).

In both versions, use **Features** in the ty settings to enable **Inspections**, **Completions**,
**Inlay hints**, and **Documentation**.

In PyCharm 2025.3 through 2026.1, open **Settings → Python → Tools → ty** and select **Enable**.
See the [PyCharm 2026.1 documentation](https://www.jetbrains.com/help/pycharm/2026.1/lsp-tools.html#ty).

## Emacs

ty can be utilized as a language server via the built-in [Eglot](https://www.gnu.org/software/emacs/manual/html_node/eglot/index.html) client, which is part of Emacs since version 29.

```elisp
(with-eval-after-load 'eglot
  (add-to-list 'eglot-server-programs
               '((python-base-mode :language-id "python") . ("ty" "server"))))

(add-hook 'python-base-mode-hook 'eglot-ensure)
```

If you prefer to view ty's diagnostics through [Flycheck](https://www.flycheck.org/), the
[flycheck-eglot](https://github.com/flycheck/flycheck-eglot) package bridges Eglot's diagnostics
to Flycheck.

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
