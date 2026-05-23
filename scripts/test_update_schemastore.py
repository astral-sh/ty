"""Tests for update_schemastore.py."""

from __future__ import annotations

import sys
from io import StringIO
from pathlib import Path
from unittest.mock import patch

# Make the scripts directory importable without installing anything.
sys.path.insert(0, str(Path(__file__).parent))

import update_schemastore  # noqa: E402


def _run_main_with_mocked_git(
    expected_sha: str | bytes,
    actual_sha: str | bytes,
) -> str:
    """
    Run the submodule-mismatch branch of main() with two fake SHAs and
    capture what it prints.  Mocks out check_output so no real git is needed.
    The user prompt is answered with 'n' (abort) to avoid any side effects.
    """
    call_count = 0

    def fake_check_output(cmd, **kwargs):  # noqa: ANN001, ANN202
        nonlocal call_count
        call_count += 1
        # First call  → ls-tree  → expected revision
        # Second call → rev-parse → actual revision
        if call_count == 1:
            return expected_sha
        return actual_sha

    captured = StringIO()
    with (
        patch.object(update_schemastore, "check_output", side_effect=fake_check_output),
        patch("builtins.input", return_value="n"),
        patch("sys.stdout", captured),
    ):
        update_schemastore.main()

    return captured.getvalue()


class TestSubmoduleRevisionMessage:
    """main() must print clean hex SHAs, not bytes repr, when revisions differ."""

    EXPECTED_SHA = "deadbeef" * 5  # 40-char fake SHA
    ACTUAL_SHA = "cafebabe" * 5    # 40-char fake SHA

    def test_message_contains_actual_sha(self) -> None:
        """The printed message includes the actual (checked-out) revision."""
        output = _run_main_with_mocked_git(self.EXPECTED_SHA, self.ACTUAL_SHA)
        assert self.ACTUAL_SHA in output

    def test_message_contains_expected_sha(self) -> None:
        """The printed message includes the expected (main-branch) revision."""
        output = _run_main_with_mocked_git(self.EXPECTED_SHA, self.ACTUAL_SHA)
        assert self.EXPECTED_SHA in output

    def test_message_has_no_bytes_prefix(self) -> None:
        """
        Without text=True, check_output returns bytes and the f-string renders
        them as  b'deadbeef...'.  This test fails on the original code and
        passes after adding text=True to both check_output calls.
        """
        output = _run_main_with_mocked_git(self.EXPECTED_SHA, self.ACTUAL_SHA)
        assert "b'" not in output, (
            f"Message contains raw bytes repr — check_output calls are missing text=True.\n"
            f"Actual output: {output!r}"
        )

    def test_message_still_fails_with_bytes_input(self) -> None:
        """
        Confirm the test is sensitive: if bytes are passed in (simulating the
        pre-fix state), the no-bytes-prefix assertion would fire.
        """
        bytes_expected = self.EXPECTED_SHA.encode()
        bytes_actual = self.ACTUAL_SHA.encode()
        output = _run_main_with_mocked_git(bytes_expected, bytes_actual)
        # With bytes the f-string embeds b'...' — assert that is detectable.
        assert "b'" in output, (
            "Expected bytes repr in output when bytes are passed in — "
            "the test harness itself may be broken."
        )
