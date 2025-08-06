# Editor settings

The editor settings supported by ty's language server, as well as the settings specific to [ty's VS
Code extension][ty-vscode].

## Runtime settings

These settings define the behavior of the language server while it is running. They can be changed
dynamically without needing to restart the server.

### `disableLanguageServices`

Whether to disable the language services for the ty language server like code completion, hover,
go to definition, etc.

This is useful if you want to use ty exclusively for type checking and want to use another language
server for features like code completion, hover, go to definition, etc.

**Default value**: `false`

**Type**: `boolean`

**Example usage**:

=== "VS Code"

    ```json
    {
      "ty.disableLanguageServices": true
    }
    ```

=== "Neovim"

    ```lua
    require('lspconfig').ty.setup({
      settings = {
        ty = {
          disableLanguageServices = true,
        },
      },
    })

    -- For Neovim 0.11.0 and later:
    vim.lsp.config('ty', {
      settings = {
        ty = {
          disableLanguageServices = true,
        },
      },
    })
    ```

=== "Zed"

    ```json
    {
      "lsp": {
        "ty": {
          "settings": {
            "ty": {
              "disableLanguageServices": true
            }
          }
        }
      }
    }
    ```

______________________________________________________________________

### `python.ty.disableLanguageServices`

!!! warning "Deprecated"

    This option has been deprecated. Use [`ty.disableLanguageServices`](#disablelanguageservices) instead.

Whether to disable the language services for the ty language server like code completion, hover,
go to definition, etc.

This is useful if you want to use ty exclusively for type checking and want to use another language
server for features like code completion, hover, go to definition, etc.

**Default value**: `false`

**Type**: `boolean`

**Example usage**:

```json
{
  "python.ty.disableLanguageServices": true
}
```

______________________________________________________________________

### `diagnosticMode`

Determines the scope of the diagnostics reported by the language server.

- `openFilesOnly`: Diagnostics are reported only for files that are currently open in the editor.
- `workspace`: Diagnostics are reported for all files in the workspace.

**Default value**: `"openFilesOnly"`

**Type**: `"workspace" | "openFilesOnly"`

**Example usage**:

=== "VS Code"

    ```json
    {
      "ty.diagnosticMode": "workspace"
    }
    ```

=== "Neovim"

    ```lua
    require('lspconfig').ty.setup({
      settings = {
        ty = {
          diagnosticMode = 'workspace',
        },
      },
    })

    -- For Neovim 0.11.0 and later:
    vim.lsp.config('ty', {
      settings = {
        ty = {
          diagnosticMode = 'workspace',
        },
      },
    })
    ```

=== "Zed"

    ```json
    {
      "lsp": {
        "ty": {
          "settings": {
            "ty": {
              "diagnosticMode": "workspace"
            }
          }
        }
      }
    }
    ```

______________________________________________________________________

## Initialization options

The following settings are the initialization options that can be provided to the language server
during startup. These settings are static and cannot be changed while the server is running. Any
change to these settings requires a server restart to take effect.

### `logFile`

Path to the file to which the language server writes its log messages. By default, ty writes log messages to stderr.

**Default value**: `null`

**Type**: `string`

**Example usage**:

=== "VS Code"

    ```json
    {
      "ty.logFile": "/path/to/ty.log"
    }
    ```

=== "Neovim"

    ```lua
    require('lspconfig').ty.setup({
      init_options = {
        logFile = '/path/to/ty.log',
      },
    })

    -- For Neovim 0.11.0 and later:
    vim.lsp.config('ty', {
      init_options = {
        logFile = '/path/to/ty.log',
      },
    })
    ```

=== "Zed"

    ```json
    {
      "lsp": {
        "ty": {
          "initialization_options": {
            "logFile": "/path/to/ty.log"
          }
        }
      }
    }
    ```

______________________________________________________________________

### `logLevel`

The log level to use for the language server.

**Default value**: `"info"`

**Type**: `"trace" | "debug" | "info" | "warn" | "error"`

**Example usage**:

=== "VS Code"

    ```json
    {
      "ty.logLevel": "debug"
    }
    ```

=== "Neovim"

    ```lua
    require('lspconfig').ty.setup({
      init_options = {
        logLevel = 'debug',
      },
    })

    -- For Neovim 0.11.0 and later:
    vim.lsp.config('ty', {
      init_options = {
        logLevel = 'debug',
      },
    })
    ```

=== "Zed"

    ```json
    {
      "lsp": {
        "ty": {
          "initialization_options": {
            "logLevel": "debug"
          }
        }
      }
    }
    ```

______________________________________________________________________

## VS Code specific

The following settings are specific to [ty's VS Code extension][ty-vscode].

### `importStrategy`

Strategy for loading the `ty` executable.

- `fromEnvironment` finds ty in the environment, falling back to the bundled version
- `useBundled` uses the version bundled with the extension

**Default value**: `"fromEnvironment"`

**Type**: `"fromEnvironment" | "useBundled"`

**Example usage**:

```json
{
  "ty.importStrategy": "useBundled"
}
```

______________________________________________________________________

### `interpreter`

A list of paths to Python interpreters. Even though this is a list, only the first interpreter is
used.

The interpreter path is used to find the `ty` executable when
[`ty.importStrategy`](#importstrategy) is set to `fromEnvironment`.

**Default value**: `[]`

**Type**: `string[]`

**Example usage**:

```json
{
  "ty.interpreter": ["/home/user/.local/bin/python"]
}
```

______________________________________________________________________

### `path`

A list of path to `ty` executables.

The extension uses the first executable that exists. This setting takes precedence over the
[`ty.importStrategy`](#importstrategy) setting.

**Default value**: `[]`

**Type**: `string[]`

**Example usage**:

```json
{
  "ty.path": ["/home/user/.local/bin/ty"]
}
```

______________________________________________________________________

### `trace.server`

The detail level at which messages between the language server and the editor (client) are logged. Refer to the [LSP
specification](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#traceValue)
for more information.

**Default value**: `"off"`

**Type**: `"off" | "messages" | "verbose"`

**Example usage**:

```json
{
  "ty.trace.server": "messages"
}
```

[ty-vscode]: https://github.com/astral-sh/ty-vscode/
