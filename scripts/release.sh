#!/usr/bin/env sh
#
# Prepare a release.
#
# Usage
#
#   ./scripts/release.sh [rooster-args ...]
#
set -eu

echo "Checking Ruff submodule status..."
if git -C ruff diff --quiet; then
    echo "Ruff submodule is clean; continuing..."
else
    echo "Ruff submodule has uncommitted changes; aborting!"
    exit 1
fi

ruff_head=$(git -C ruff rev-parse --abbrev-ref HEAD)
case "${ruff_head}" in
    "HEAD")
        echo "Ruff submodule has detached HEAD; switching to main..."
        git -C ruff checkout main > /dev/null 2>&1
        ;;
    "main")
        echo "Ruff submodule is on main branch; continuing..."
        ;;
    *)
        echo "Ruff submodule is on branch ${ruff_head} but must be on main; aborting!"
        exit 1
        ;;
esac


echo "Updating Ruff to the latest commit..."
git -C ruff pull origin main
git add ruff

script_root="$(realpath "$(dirname "$0")")"
project_root="$(dirname "$script_root")"

echo "Running rooster..."
cd "$project_root"

# Generate the changelog and bump versions
uv run --only-group release \
    rooster release "$@"

"${script_root}/autogenerate_files.sh"
git add ./docs/reference
