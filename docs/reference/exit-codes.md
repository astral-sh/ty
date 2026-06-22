# Exit codes

The ty command line interface uses the following exit codes:

| Exit code | Description                                                |
| :-------- | :--------------------------------------------------------- |
| `0`       | no violations with severity `warning` or higher were found |
| `1`       | violations with severity `warning` or higher were found    |
| `2`       | invalid CLI options, invalid configuration, or IO errors   |
| `101`     | internal error                                             |

ty supports three command line arguments that change how exit codes work:

- `--exit-zero`: ty will exit with `0` even if violations were found.
- `--error-on-warning`: ty will exit with `1` if it finds any violations with severity `warning` or
    higher. This is usually the default behaviour, but can be overridden using a configuration file.
- `--exit-zero-on-warning`: ty will only exit with `1` if it finds violations with severity `error` or higher.

`--error-on-warning` cannot be supplied at the same time as `--exit-zero` or `--exit-zero-on-warning`.
