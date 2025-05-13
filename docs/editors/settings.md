# Settings

## Language server settings

### `experimental`

This setting is used to enable or disable experimental features in the language server.

#### `completions.enable`

Whether to enable completions from the language server.

**Default value**: `false`

**Type**: `boolean`

**Example usage**:

```json
{
  "ty.experimental.completions.enable": true
}
```

### `logFile`

Path to the log file to use for the language server.

If not set, logs will be written to stderr.

**Default value**: `null`

**Type**: `string`

**Example usage**:

```json
{
  "ty.logFile": "~/path/to/ty.log"
}
```

### `logLevel`

The log level to use for the language server.

**Default value**: `"info"`

**Type**: `"trace" | "debug" | "info" | "warn" | "error"`

**Example usage**:

```json
{
  "ty.logLevel": "debug"
}
```

### `trace.server`

The trace level for the language server. Refer to the [LSP
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

## VS Code specific

Additionally, the ty extension provides the following settings specific to VS Code. These settings
are not used by the language server and are only relevant to the extension.

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

### `path`

A list of path to `ty` executables.

The first executable in the list which is exists is used. This setting takes precedence over the
[`ty.importStrategy`](#importstrategy) setting.

**Default value**: `[]`

**Type**: `string[]`

**Example usage**:

```json
{
  "ty.path": ["/home/user/.local/bin/ty"]
}
```
