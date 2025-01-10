"""Basic test cases for XX Shell package."""

from xx_shell import __version__


def test_version() -> None:
    """Test that the package version is properly set."""
    assert __version__ is not None
