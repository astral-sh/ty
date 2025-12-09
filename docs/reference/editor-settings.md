# Editor settings

The editor settings supported by ty's language server, as well as the settings specific to [ty's VS
Code extension][ty-vscode].

## `disableLanguageServices`

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
            "disableLanguageServices": true
          }
        }
      }
    }
    ```

______________________________________________________________________

## `python.ty.disableLanguageServices`

!!! warning "Deprecated"

    This option has been deprecated. Use [`ty.disableLanguageServices`](#disablelanguageservices) instead.

Whether to disable the language services that ty provides like code completion, hover, go to
definition, etc.

This is useful if you want to use ty exclusively for type checking in combination with another
language server for features like code completion, hover, go to definition, etc.

**Default value**: `false`

**Type**: `boolean`

**Example usage**:

```json
{
  "python.ty.disableLanguageServices": true
}
```

______________________________________________________________________

## `diagnosticMode`

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
            "diagnosticMode": "workspace"
          }
        }
      }
    }
    ```

______________________________________________________________________

## `inlayHints`

These settings control the inline hints that ty provides in an editor.

### `variableTypes`

Whether to show the types of variables as inline hints.

**Default value**: `true`

**Type**: `boolean`

**Example usage**:

=== "VS Code"

    ```json
    {
      "ty.inlayHints.variableTypes": false
    }
    ```

=== "Neovim"

    ```lua
    require('lspconfig').ty.setup({
      settings = {
        ty = {
          inlayHints = {
            variableTypes = false,
          },
        },
      },
    })

    -- For Neovim 0.11.0 and later:
    vim.lsp.config('ty', {
      settings = {
        ty = {
          inlayHints = {
            variableTypes = false,
          },
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
            "inlayHints": {
              "variableTypes": false
            }
          }
        }
      }
    }
    ```

### `callArgumentNames`

Whether to show argument names in call expressions as inline hints.

**Default value**: `true`

**Type**: `boolean`

**Example usage**:

=== "VS Code"

    ```json
    {
      "ty.inlayHints.callArgumentNames": false
    }
    ```

=== "Neovim"

    ```lua
    require('lspconfig').ty.setup({
      settings = {
        ty = {
          inlayHints = {
            callArgumentNames = false,
          },
        },
      },
    })

    -- For Neovim 0.11.0 and later:
    vim.lsp.config('ty', {
      settings = {
        ty = {
          inlayHints = {
            callArgumentNames = false,
          },
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
            "inlayHints": {
              "callArgumentNames": false
            }
          }
        }
      }
    }
    ```

______________________________________________________________________

## `completions`

These settings control how code completions offered by ty work.

### `autoImport`

Whether to include auto-import suggestions in code completions. That is, code completions will
include symbols not currently in scope but available in your environment.

**Default value**: `true`

**Type**: `boolean`

**Example usage**:

=== "VS Code"

    ```json
    {
      "ty.completions.autoImport": true
    }
    ```

=== "Neovim"

    ```lua
    require('lspconfig').ty.setup({
      settings = {
        ty = {
          completions = {
            autoImport = true,
          },
        },
      },
    })

    -- For Neovim 0.11.0 and later:
    vim.lsp.config('ty', {
      settings = {
        ty = {
          completions = {
            autoImport = true,
          },
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
            "completions": {
              "autoImport": true
            }
          }
        }
      }
    }
    ```

______________________________________________________________________

## `experimental`

These settings control the experimental language features that ty provides in an editor.

### `rename`

Whether to enable the experimental support for renaming symbols in the editor.

**Default value**: `false`

**Type**: `boolean`

**Example usage**:

=== "VS Code"

    ```json
    {
      "ty.experimental.rename": true
    }
    ```

=== "Neovim"

    ```lua
    require('lspconfig').ty.setup({
      settings = {
        ty = {
          experimental = {
            rename = true,
          },
        },
      },
    })

    -- For Neovim 0.11.0 and later:
    vim.lsp.config('ty', {
      settings = {
        ty = {
          experimental = {
            rename = true,
          },
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
            "experimental": {
              "rename": true
            }
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

The detail level at which messages between the language server and the editor (client) are logged.

This setting is useful for debugging issues with the language server. Refer to the [troubleshooting
guide](https://github.com/astral-sh/ty-vscode/blob/6cf16b4e87342a49f2bec1310a730cde8229e1d9/TROUBLESHOOTING.md)
in [ty's VS Code extension][ty-vscode] for more information.

**Default value**: `"off"`

**Type**: `"off" | "messages" | "verbose"`

**Example usage**:

```json
{
  "ty.trace.server": "messages"
}
```

______________________________________________________________________

## Initialization options

The following settings are required when ty is initialized in an editor. These settings are
static so changing them requires restarting the editor to take effect.

For VS Code users, these settings are defined in the `ty.*` namespace as usual, but for other
editors, they would need to be provided in a separate field of the configuration that corresponds to
the initialization options. Refer to the examples below for how to set these options in different
editors.

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

[ty-vscode]: https://marketplace.visualstudio.com/items?itemName=astral-sh.ty
