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


# Save the current typeshed source commit before updating ruff,
# so we can generate a typeshed diff link for the changelog later.
typeshed_commit_file="ruff/crates/ty_vendored/vendor/typeshed/source_commit.txt"
old_typeshed_commit=""
if [ -f "$typeshed_commit_file" ]; then
    old_typeshed_commit=$(cat "$typeshed_commit_file")
fi

echo "Updating Ruff to the latest commit..."
git -C ruff pull origin main
git add ruff

script_root="$(realpath "$(dirname "$0")")"
project_root="$(dirname "$script_root")"

echo "Running rooster..."
cd "$project_root"

# Generate the changelog and bump versions
uv run --isolated --only-group release \
    rooster release "$@"

# If the typeshed source commit changed and the changelog mentions a typeshed
# sync, append a link to the typeshed diff so reviewers can see what changed.
if [ -n "$old_typeshed_commit" ] && [ -f "$typeshed_commit_file" ]; then
    new_typeshed_commit=$(cat "$typeshed_commit_file")
    if [ "$old_typeshed_commit" != "$new_typeshed_commit" ]; then
        typeshed_diff_link="[Typeshed diff](https://github.com/python/typeshed/compare/${old_typeshed_commit}...${new_typeshed_commit})"
        # Match lines like "- Sync vendored typeshed stubs ([#NNNN](...))".
        # The pattern anchors on the trailing "))$" so it won't match lines
        # that already have a typeshed diff link appended.
        sed -i "s|\(- Sync vendored typeshed stubs (.*)\))$|\1). ${typeshed_diff_link}|" CHANGELOG.md
    fi
fi

"${script_root}/autogenerate_files.sh"
git add ./docs/reference
