"""Update ty.json in schemastore.

This script will clone astral-sh/schemastore, update the schema and push the changes
to a new branch tagged with the ty git hash. You should see a URL to create the PR
to schemastore in the CLI.
"""

from __future__ import annotations

import enum
import json
from pathlib import Path
from subprocess import check_call, check_output
from tempfile import TemporaryDirectory
from typing import NamedTuple, assert_never

TY_REPO = "https://github.com/astral-sh/ty"
TY_JSON = Path("schemas/json/ty.json")


class SchemastoreRepos(NamedTuple):
    fork: str
    upstream: str


class GitProtocol(enum.Enum):
    SSH = "ssh"
    HTTPS = "https"

    def schemastore_repos(self) -> SchemastoreRepos:
        match self:
            case GitProtocol.SSH:
                return SchemastoreRepos(
                    fork="git@github.com:astral-sh/schemastore.git",
                    upstream="git@github.com:SchemaStore/schemastore.git",
                )
            case GitProtocol.HTTPS:
                return SchemastoreRepos(
                    fork="https://github.com/astral-sh/schemastore.git",
                    upstream="https://github.com/SchemaStore/schemastore.git",
                )
            case _:
                assert_never(self)


def update_schemastore(
    schemastore_path: Path, schemastore_repos: SchemastoreRepos, root: Path
) -> None:
    if not schemastore_path.is_dir():
        check_call(
            ["git", "clone", schemastore_repos.fork, schemastore_path, "--depth=1"]
        )
        check_call(
            [
                "git",
                "remote",
                "add",
                "upstream",
                schemastore_repos.upstream,
            ],
            cwd=schemastore_path,
        )
    # Create a new branch tagged with the current ty commit up to date with the latest
    # upstream schemastore
    check_call(["git", "fetch", "upstream"], cwd=schemastore_path)
    current_sha = check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    branch = f"update-ty-{current_sha}"
    check_call(
        ["git", "switch", "-c", branch],
        cwd=schemastore_path,
    )
    check_call(
        ["git", "reset", "--hard", "upstream/master"],
        cwd=schemastore_path,
    )

    # Run npm install
    src = schemastore_path.joinpath("src")
    check_call(["npm", "install"], cwd=schemastore_path)

    # Update the schema and format appropriately
    schema = json.loads(root.joinpath("ruff/ty.schema.json").read_text())
    schema["$id"] = "https://json.schemastore.org/ty.json"
    src.joinpath(TY_JSON).write_text(
        json.dumps(dict(schema.items()), indent=2, ensure_ascii=False),
    )
    check_call(
        [
            "../node_modules/prettier/bin/prettier.cjs",
            "--plugin",
            "prettier-plugin-sort-json",
            "--write",
            TY_JSON,
        ],
        cwd=src,
    )

    # Check if the schema has changed
    # https://stackoverflow.com/a/9393642/3549270
    if check_output(["git", "status", "-s"], cwd=schemastore_path).strip():
        # Schema has changed, commit and push
        commit_url = f"{TY_REPO}/commit/{current_sha}"
        commit_body = f"This updates ty's JSON schema to [{current_sha}]({commit_url})"
        # https://stackoverflow.com/a/22909204/3549270
        check_call(
            [
                "git",
                "commit",
                "-a",
                "-m",
                "Update ty's JSON schema",
                "-m",
                commit_body,
            ],
            cwd=schemastore_path,
        )
        # This should show the link to create a PR
        check_call(
            ["git", "push", "--set-upstream", "origin", branch, "--force"],
            cwd=schemastore_path,
        )
    else:
        print("No changes")


def determine_git_protocol(argv: list[str] | None = None) -> GitProtocol:
    import argparse

    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--proto",
        choices=[proto.value for proto in GitProtocol],
        default="https",
        help="Protocol to use for git authentication",
    )
    args = parser.parse_args(argv)
    return GitProtocol(args.proto)


def main() -> None:
    root = Path(
        check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip(),
    )

    expected_ruff_revision = check_output(
        ["git", "ls-tree", "main", "--format", "%(objectname)", "ruff"]
    ).strip()
    actual_ruff_revision = check_output(
        ["git", "-C", "ruff", "rev-parse", "HEAD"]
    ).strip()

    if expected_ruff_revision != actual_ruff_revision:
        print(
            f"The ruff submodule is at {expected_ruff_revision} but main expects {actual_ruff_revision}"
        )
        match input(
            "How do you want to proceed (u=reset submodule, n=abort, y=continue)? "
        ):
            case "u":
                check_call(
                    ["git", "-C", "ruff", "reset", "--hard", expected_ruff_revision]
                )
            case "n":
                return
            case "y":
                ...
            case command:
                print(f"Invalid input '{command}', abort")
                return

    schemastore_repos = determine_git_protocol().schemastore_repos()
    schemastore_existing = root.joinpath("schemastore")
    if schemastore_existing.is_dir():
        update_schemastore(schemastore_existing, schemastore_repos, root)
    else:
        with TemporaryDirectory() as temp_dir:
            update_schemastore(
                Path(temp_dir).joinpath("schemastore"), schemastore_repos, root
            )


if __name__ == "__main__":
    main()
