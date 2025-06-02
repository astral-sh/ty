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

echo "Updating lockfile..."
uv lock

echo "Generating TOC for documentation..."
uv run --script scripts/update_docs_toc.py

echo "Copying reference documentation from Ruff..."
cp ruff/crates/ty/docs/cli.md ./docs/reference/
cp ruff/crates/ty/docs/configuration.md ./docs/reference/
cp ./ruff/crates/ty/docs/rules.md ./docs/reference/

echo "Documentation has been copied from Ruff submodule"
