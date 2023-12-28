"""Test file."""

from opinionated_python.main import add


def test_add() -> None:
    """Tests the add function."""
    assert add(a=2, b=5) == 7
