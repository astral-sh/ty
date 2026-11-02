# Versioning

ty uses a custom versioning scheme:

- **Patch releases** contain bug fixes, enhancements, and other non-breaking changes.
- **Minor releases** include typeshed updates and changes to type-checking behavior, configuration,
    rules, and the CLI. These releases may report new type errors.
- **Major releases** are reserved for breaking changes that we expect to have a significant impact
    on existing users. We consider both the number of affected users and the work required to upgrade
    when deciding whether a change warrants a major release.

## Preview features

Preview features are unstable and may change or be removed in any release, including patch releases.

## Crate versioning

The versioning policy above applies to the ty binary. The Rust interfaces of ty’s crates do not
follow semantic versioning.

Library crates published as part of ty releases provide **no stability guarantees**. Their Rust
interfaces are considered internal and unstable. Consequently, they are versioned as `0.0.x`. The
patch version is incremented on every ty release, regardless of changes to the crate.

## Minimum supported Rust version

The minimum supported Rust version required to compile ty is listed in the `rust-version` key of the
`[workspace.package]` section in `Cargo.toml`. It may change in any release (minor or patch). It
will never be newer than N-2 Rust versions, where N is the latest stable version. For example, if
the latest stable Rust version is 1.85, ty's minimum supported Rust version will be at most 1.83.

This is only relevant to users who build ty from source. Installing ty from the Python Package Index (PyPI)
usually installs a pre-built binary and does not require Rust compilation.

## Visual Studio Code Extension

Visual Studio Code
[doesn't support pre-release tags](https://code.visualstudio.com/api/working-with-extensions/publishing-extension#pre-release-extensions)
for extensions. Consequently, ty uses the following scheme to distinguish between stable and preview
releases:

Stable releases use even numbers in minor version component: `2024.30.0`, `2024.32.0`, `2024.34.0`,
… Preview releases use odd numbers in minor version component: `2024.31.0`, `2024.33.0`,
`2024.35.0`, …
