# Environment variables

ty defines and respects the following environment variables:

## `TY_LOG`

If set, ty will use this value as the log level for its `--verbose` output. Accepts any filter compatible with the `tracing_subscriber` crate. For example:

- `TY_LOG=uv=debug` is the equivalent of `-vv` to the command line
- `TY_LOG=trace` will enable all trace-level logging.

See the [tracing documentation](https://docs.rs/tracing-subscriber/latest/tracing_subscriber/filter/struct.EnvFilter.html#example-syntax) for more.

## `TY_MAX_PARALLELISM`

Specifies an upper limit for the number of tasks ty is allowed to run in parallel. For example, how many files should be checked in parallel.

This isn’t the same as a thread limit. ty may spawn additional threads when necessary, e.g. to watch for file system changes or a dedicated UI thread.

## Externally defined variables

ty also reads the following externally defined environment variables:

### `RAYON_NUM_THREADS`

Specifies an upper limit for the number of threads ty uses when performing work in parallel. Equivalent to `TY_MAX_PARALLELISM`.

### `VIRTUAL_ENV`

Used to detect an activated virtual environment.

### `XDG_CONFIG_HOME`

Path to user-level configuration directory on Unix systems.
