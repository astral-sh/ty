# ty Repository

## Development

`.github/workflows/release.yml` is maintained manually. Edit it or the referenced reusable workflows directly. `cargo-dist` still uses `dist-workspace.toml` to plan releases and build artifacts, but regenerating the workflow can overwrite manual customizations. If you regenerate it, review the diff carefully and preserve those customizations.
