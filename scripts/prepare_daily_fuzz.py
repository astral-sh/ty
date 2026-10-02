# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

"""Select Ruff commits for the daily fuzzer."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Final

# The workflow and its checkpoint artifacts are in the ty repository.
REPOSITORY: Final = "astral-sh/ty"

# Bootstrap the first workflow run, which has no earlier run to compare against.
INITIAL_COMMIT: Final = "a4e7c20ca0d42f5cb41485210193548b98ee39c2"


def run(*command: str) -> None:
    """Run a command, sending its standard output to standard error.

    This keeps standard output reserved for the selected commits.
    Raise `subprocess.CalledProcessError` if the command exits with a nonzero status.
    """
    subprocess.run(command, check=True, stdout=sys.stderr)


def output(*command: str) -> str:
    """Run a command and return its stripped standard output.

    Raise `subprocess.CalledProcessError` if the command exits with a nonzero status.
    """
    return subprocess.check_output(command, text=True).strip()


def main() -> None:
    """Select the current and baseline Ruff commits for daily fuzzing.

    Read the current commit from the checkout passed via `--ruff-root`. Use
    `INITIAL_COMMIT` as the baseline for the first workflow run. For later runs,
    select the `main` commit recorded by the most recently created scheduled run
    in the last seven days that completed and has an unexpired checkpoint
    artifact. Fail if no such artifact exists. Require the baseline to be an
    ancestor of the current commit. Print both commits as GitHub Actions output
    entries.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ruff-root", type=Path, required=True)
    ruff_root = parser.parse_args().ruff_root

    runner_temp = Path(os.environ["RUNNER_TEMP"])
    assert runner_temp.is_dir()

    # Use the commit checked out by the workflow, even if Ruff's main branch
    # moves while the run is in progress.
    new_commit = output("git", "-C", str(ruff_root), "rev-parse", "HEAD")

    # GitHub numbers workflow runs from 1 and retains the number on re-runs.
    # The bootstrap commit is therefore used only for the first run and its re-runs.
    if os.environ["GITHUB_RUN_NUMBER"] == "1":
        old_commit = INITIAL_COMMIT
    else:
        cutoff = (datetime.now(UTC) - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ")

        # Completed runs include failures; a run that finds a new panic still
        # uploads a checkpoint so future runs can compare against it.
        # GitHub limits filtered workflow-run searches to 1,000 results.
        previous_runs_raw = output(
            "gh",
            "run",
            "list",
            "--repo",
            REPOSITORY,
            "--workflow",
            "daily_fuzz.yml",
            "--event",
            "schedule",
            "--status",
            "completed",
            "--created",
            f">={cutoff}",
            "--limit",
            "1000",
            "--json",
            "databaseId",
        )
        previous_runs = json.loads(previous_runs_raw)
        assert isinstance(previous_runs, list)

        # Runs are returned newest first. A run may have failed before uploading
        # a checkpoint, or its artifact may have expired, so check earlier runs.
        for previous_run in previous_runs:
            run_id = str(previous_run["databaseId"])
            run_artifacts_raw = output(
                "gh",
                "api",
                f"repos/{REPOSITORY}/actions/runs/{run_id}/artifacts?name=daily-fuzz-ruff-head",
            )

            run_artifacts = json.loads(run_artifacts_raw)
            assert isinstance(run_artifacts, dict)

            if not any(
                artifact["expired"] is False for artifact in run_artifacts["artifacts"]
            ):
                continue

            # Use the Ruff `main` commit recorded in the first available artifact
            # as the baseline.
            previous_fuzz = runner_temp / "previous-fuzz"
            run(
                "gh",
                "run",
                "download",
                run_id,
                "--repo",
                REPOSITORY,
                "--name",
                "daily-fuzz-ruff-head",
                "--dir",
                str(previous_fuzz),
            )
            old_commit = (previous_fuzz / "ruff-head").read_text().strip()
            break
        else:
            raise RuntimeError(
                "No available checkpoint from a completed daily fuzz run in the last seven days"
            )

    # Require a full commit ID in the current checkout's history before the
    # workflow uses these commits to build ty.
    if re.fullmatch(r"[0-9a-f]{40}", old_commit) is None:
        raise ValueError(f"Invalid Ruff commit: {old_commit!r}")

    # Fail if the baseline is not an ancestor of the current commit; otherwise,
    # differences between the builds may not come from changes made after the baseline.
    run(
        "git",
        "-C",
        str(ruff_root),
        "merge-base",
        "--is-ancestor",
        old_commit,
        new_commit,
    )

    # The workflow redirects stdout to GITHUB_OUTPUT; these entries become the
    # inputs for the build step.
    print(f"new_commit={new_commit}")
    print(f"old_commit={old_commit}")


if __name__ == "__main__":
    main()
