# Editor settings

The editor settings supported by ty's language server, as well as the settings specific to [ty's VS
Code extension][ty-vscode].

## `configuration`

In-editor configuration of ty's settings. The inline settings always take precedence over the settings from configuration files,
including the configuration specified with [`configurationFile`](#configurationfile).

Consult [the configuration reference](../configuration.md) for a list of all supported configuration options.

**Default value**: `null`

**Type**: `object`

**Example usage**:

=== "VS Code"

    ```json
    {
      "ty.configuration": {
        "rules": {
          "unresolved-reference": "warn"
        }
      }
    }
    ```

=== "Neovim"

    ```lua
    -- Neovim >=0.11:
    vim.lsp.config('ty', {
      settings = {
        ty = {
          configuration = {
            rules = {
              ["unresolved-reference"] = "warn"
            }
          }
        },
      },
    })

    -- Neovim <0.11:
    require('lspconfig').ty.setup({
      settings = {
        ty = {
          configuration = {
            rules = {
              ["unresolved-reference"] = "warn"
            }
          }
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
            "configuration": {
               "rules": {
                "unresolved-reference": "warn"
              }
            }
          }
        }
      }
    }
    ```

## `configurationFile`

The path to a `ty.toml` configuration file. ty will use the specified configuration over any automatically discovered configuration.
ty will expand a tilde `~` at the start of a string to the user's home directory, as well as variables like `$A` or `${A}`.

!!! info

    While ty configuration can be included in a `pyproject.toml` file, it is not allowed in this context.

**Default value**: `null`

**Type**: `string`

**Example usage**:

=== "VS Code"

    ```json
    {
      "ty.configurationFile": "./.config/ty.toml"
    }
    ```

=== "Neovim"

    ```lua
    -- Neovim >=0.11:
    vim.lsp.config('ty', {
      settings = {
        ty = {
          configurationFile = "./.config/ty.toml"
        },
      },
    })

    -- Neovim <0.11:
    require('lspconfig').ty.setup({
      settings = {
        ty = {
          configurationFile = "./.config/ty.toml"
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
            "configurationFile": "./.config/ty.toml"
          }
        }
      }
    }
    ```

______________________________________________________________________

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
    -- Neovim >=0.11:
    vim.lsp.config('ty', {
      settings = {
        ty = {
          disableLanguageServices = true,
        },
      },
    })

    -- Neovim <0.11:
    require('lspconfig').ty.setup({
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

## `diagnosticMode`

Determines the scope of the diagnostics reported by the language server.

Setting this to `off` is useful if you want to use ty exclusively for the language server features
like code completion, hover, go to definition, etc.

- `off`: Diagnostics are disabled.
- `openFilesOnly`: Diagnostics are reported only for files that are currently open in the editor.
- `workspace`: Diagnostics are reported for all files in the workspace.

**Default value**: `"openFilesOnly"`

**Type**: `"off" | "workspace" | "openFilesOnly"`

**Example usage**:

=== "VS Code"

    ```json
    {
      "ty.diagnosticMode": "workspace"
    }
    ```

=== "Neovim"

    ```lua
    -- Neovim >=0.11:
    vim.lsp.config('ty', {
      settings = {
        ty = {
          diagnosticMode = 'workspace',
        },
      },
    })

    -- Neovim <0.11:
    require('lspconfig').ty.setup({
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

## `showSyntaxErrors`

Whether to show syntax error diagnostics.

This is useful when using ty with other language servers, allowing the user to refer to syntax errors
from only one source.

**Default value**: `true`

**Type**: `bool`

**Example usage**:

=== "VS Code"

    ```json
    {
        "ty.showSyntaxErrors": false
    }
    ```

=== "Neovim"

    ```lua
    -- Neovim >=0.11:
    vim.lsp.config('ty', {
      settings = {
        ty = {
          showSyntaxErrors = false,
        },
      },
    })

    -- Neovim <0.11:
    require('lspconfig').ty.setup({
      settings = {
        ty = {
          showSyntaxErrors = false,
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
            "showSyntaxErrors": false
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
    -- Neovim >=0.11:
    vim.lsp.config('ty', {
      settings = {
        ty = {
          inlayHints = {
            variableTypes = false,
          },
        },
      },
    })

    -- Neovim <0.11:
    require('lspconfig').ty.setup({
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
    -- Neovim >=0.11:
    vim.lsp.config('ty', {
      settings = {
        ty = {
          inlayHints = {
            callArgumentNames = false,
          },
        },
      },
    })

    -- Neovim <0.11:
    require('lspconfig').ty.setup({
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
    -- Neovim >=0.11:
    vim.lsp.config('ty', {
      settings = {
        ty = {
          completions = {
            autoImport = true,
          },
        },
      },
    })

    -- Neovim <0.11:
    require('lspconfig').ty.setup({
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

### `completeFunctionParentheses`

Whether accepting a function, method, or class completion also inserts parentheses and places the
cursor inside them.

**Default value**: `false`

**Type**: `boolean`

**Example usage**:

=== "VS Code"

    ```json
    {
      "ty.completions.completeFunctionParentheses": true
    }
    ```

=== "Neovim"

    ```lua
    -- Neovim >=0.11:
    vim.lsp.config('ty', {
      settings = {
        ty = {
          completions = {
            completeFunctionParentheses = true,
          },
        },
      },
    })

    -- Neovim <0.11:
    require('lspconfig').ty.setup({
      settings = {
        ty = {
          completions = {
            completeFunctionParentheses = true,
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
              "completeFunctionParentheses": true
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

The following options are read when ty is initialized in an editor. Changing them requires
restarting the language server.

In VS Code, most of these options are available in the `ty.*` namespace. The extension sets
[`untrustedWorkspace`](#untrustedworkspace) automatically. In other editors, use the field for
language server initialization options. Refer to the examples below.

### `experimental.useUv`

Control how ty uses [uv](https://docs.astral.sh/uv/):

- `off`: Do not use uv.
- `scripts`: Use uv to create and update environments for standalone scripts with
    [PEP 723 inline metadata](https://peps.python.org/pep-0723/).
- `on`: Use uv for project discovery and standalone script environments.

This feature is experimental and may change. Enabling it requires
[uv to be installed](https://docs.astral.sh/uv/getting-started/installation/) and can download and
install dependencies. All uv integrations are disabled when
[`untrustedWorkspace`](#untrustedworkspace) is `true`.

If this option is not provided, the language server uses the `TY_UV` environment variable.
The VS Code extension sends `"off"` by default.

**Default value**: `"off"`

**Type**: `"off" | "scripts" | "on"`

**Example usage**:

=== "VS Code"

    ```json
    {
      "ty.experimental.useUv": "scripts"
    }
    ```

=== "Neovim"

    ```lua
    -- Neovim >=0.11:
    vim.lsp.config('ty', {
      init_options = {
        experimental = {
          useUv = 'scripts',
        },
      },
    })

    -- Neovim <0.11:
    require('lspconfig').ty.setup({
      init_options = {
        experimental = {
          useUv = 'scripts',
        },
      },
    })
    ```

=== "Zed"

    ```json
    {
      "lsp": {
        "ty": {
          "initialization_options": {
            "experimental": {
              "useUv": "scripts"
            }
          }
        }
      }
    }
    ```

______________________________________________________________________

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
    -- Neovim >=0.11:
    vim.lsp.config('ty', {
      init_options = {
        logFile = '/path/to/ty.log',
      },
    })

    -- Neovim <0.11:
    require('lspconfig').ty.setup({
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
    -- Neovim >=0.11:
    vim.lsp.config('ty', {
      init_options = {
        logLevel = 'debug',
      },
    })

    -- Neovim <0.11:
    require('lspconfig').ty.setup({
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

### `untrustedWorkspace`

Whether the language server should treat the workspace as untrusted. When `true`, ty does not run
external commands. This disables uv integrations and prevents ty from running Python interpreters
to discover environment information.

Set this option in trusted editor configuration before opening a workspace you do not trust.
Changing it requires restarting the language server.

**Default value**: `false`

**Type**: `boolean`

**Example usage**:

=== "VS Code"

    The extension sets this option automatically based on
    [Workspace Trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust).
    There is no `ty.untrustedWorkspace` setting. Open the workspace in Restricted Mode to mark it
    as untrusted.

=== "Neovim"

    ```lua
    -- Neovim >=0.11:
    vim.lsp.config('ty', {
      init_options = {
        untrustedWorkspace = true,
      },
    })

    -- Neovim <0.11:
    require('lspconfig').ty.setup({
      init_options = {
        untrustedWorkspace = true,
      },
    })
    ```

=== "Zed"

    ```json
    {
      "lsp": {
        "ty": {
          "initialization_options": {
            "untrustedWorkspace": true
          }
        }
      }
    }
    ```

[ty-vscode]: https://marketplace.visualstudio.com/items?itemName=astral-sh.ty
