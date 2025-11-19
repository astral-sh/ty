# Exit codes

The ty command line interface uses the following exit codes:

| Exit code | Description                                              |
| :-------- | :------------------------------------------------------- |
| `0`       | no violations with severity `error` or higher were found |
| `1`       | violations with severity `error` or higher were found    |
| `2`       | invalid CLI options, invalid configuration, or IO errors |
| `101`     | internal error                                           |

ty supports two command line arguments that change how exit codes work:

- `--exit-zero`: ty will exit with `0` even if violations were found.
- `--error-on-warning`: ty will exit with `1` if it finds any violations with severity `warning` or
    higher.
