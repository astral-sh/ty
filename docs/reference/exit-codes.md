# Exit codes

The ty command line interface uses the following exit codes:

- `0` if no violations with severity `error` or higher were found.
- `1` if any violations with severity `error` were found.
- `2` if ty terminates abnormally due to invalid CLI options.
- `101` if ty terminates abnormally due to an internal error.

ty supports two command line arguments that change how exit codes work:

- `--exit-zero`: ty will exit with `0` even if violations were found.
- `--error-on-warning`: ty will exit with `1` if it finds any violations with severity `warning` or
    higher.
