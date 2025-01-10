"""Basic test cases for XX Shell package."""

from xx_shell.version import __version__
from xx_shell.main import parse_args


def test_version() -> None:
    """Test that the package version is properly set."""
    assert __version__ is not None


def test_argparse_version(capsys) -> None:
    """Test version argument parsing."""
    try:
        parse_args(["--version"])
    except SystemExit:
        pass
    captured = capsys.readouterr()
    assert __version__ in captured.out


def test_argparse_help(capsys) -> None:
    """Test help argument parsing."""
    try:
        parse_args(["--help"])
    except SystemExit:
        pass
    captured = capsys.readouterr()
    assert "XX Shell - The Intelligent Command Shell" in captured.out
