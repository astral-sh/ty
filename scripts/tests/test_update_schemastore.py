"""Tests for scripts/update_schemastore.py."""

from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import patch

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

import update_schemastore  

SHA_EXPECTED = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
SHA_ACTUAL = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"


def _fake_check_output(cmd: list, **kwargs: object) -> str:
    """Return a predictable SHA string for each git command."""
    if "ls-tree" in cmd:
        return SHA_EXPECTED + "\n"
    if "rev-parse" in cmd:
        return SHA_ACTUAL + "\n"
    raise AssertionError(f"Unexpected command: {cmd}")


def test_revision_mismatch_message_contains_no_bytes_repr(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """
    When the ruff submodule is out of sync, the printed message must show
    plain SHA strings — not Python bytes repr (b'...').

    Before the fix, check_output was called without text=True, so
    actual_ruff_revision and expected_ruff_revision were bytes objects.
    Interpolating them into the f-string printed e.g.
    "b'bbbb...'" instead of "bbbb...".
    """
    monkeypatch.setattr(update_schemastore, "check_output", _fake_check_output)

    # Simulate the user choosing 'n' (abort) so main() returns without side-effects.
    with patch("builtins.input", return_value="n"):
        update_schemastore.main()

    captured = capsys.readouterr()

    # The raw bytes repr must never appear in the output.
    assert "b'" not in captured.out, f"Output contains bytes repr: {captured.out!r}"
    # The actual SHA strings must appear cleanly.
    assert SHA_ACTUAL in captured.out
    assert SHA_EXPECTED in captured.out
