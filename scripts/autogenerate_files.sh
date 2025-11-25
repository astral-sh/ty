#!/usr/bin/env sh
#
# Generate files and copy documentation from Ruff.
#
# Usage
#
#   ./scripts/autogenerate-files.sh
#
set -eu

script_root="$(realpath "$(dirname "$0")")"
project_root="$(dirname "$script_root")"
cd "$project_root"
ruff_commit="$(git -C ruff rev-parse HEAD)"

echo "Updating lockfile..."
uv lock

echo "Copying reference documentation from Ruff..."
copy_docs() {
    src="$1"
    dest="$2"
    [[ -d "$dest" ]] && dest="$dest/$(basename "$src")"
    old_url="/github.com/astral-sh/ruff/blob/main/"
    new_url="/github.com/astral-sh/ruff/blob/$ruff_commit/"
    sed "s|$old_url|$new_url|g" "$src" > "$dest"
}
copy_docs ./ruff/crates/ty/docs/cli.md ./docs/reference/
copy_docs ./ruff/crates/ty/docs/configuration.md ./docs/reference/
copy_docs ./ruff/crates/ty/docs/rules.md ./docs/reference/
copy_docs ./ruff/crates/ty/docs/environment.md ./docs/reference/

echo "Documentation has been copied from Ruff submodule"
