"""Unit tests for core shell functionality."""

import pytest

from xx_shell.core.shell import Shell


@pytest.mark.unit
class TestShellCore:
    """Test cases for core shell functionality."""

    def test_shell_initialization(self, shell_instance: Shell) -> None:
        """Test basic shell initialization."""
        assert shell_instance is not None
        assert shell_instance.session is not None

    def test_command_parsing(self, shell_instance: Shell) -> None:
        """Test basic command parsing."""
        test_cases = [
            ("ls -la", ["ls", "-la"]),
            ("find . -name '*.py'", ["find", ".", "-name", "*.py"]),
            ("xx mcp start", ["xx", "mcp", "start"]),
        ]

        for cmd, expected in test_cases:
            result = shell_instance.parse_command(cmd)
            assert result == expected, f"Failed parsing: {cmd}"

    @pytest.mark.parametrize("cmd,expected", [
        ("help", True),
        ("invalid_command", False)
    ])
    def test_command_validation(
        self, shell_instance: Shell, cmd: str, expected: bool
    ) -> None:
        """Test command validation."""
        assert shell_instance.validate_command(cmd) == expected

    def test_command_execution(self, shell_instance: Shell) -> None:
        """Test basic command execution."""
        output = shell_instance.execute_command("echo hello")
        assert "hello" in output
        assert len(shell_instance.session.command_history) == 1
        history = shell_instance.session.command_history[0]
        assert history["command"] == "echo hello"
        assert "hello" in shell_instance.session.command_history[0]["output"]

    def test_command_execution_error(self, shell_instance: Shell) -> None:
        """Test command execution with error."""
        output = shell_instance.execute_command("invalid_command")
        output_lower = output.lower()
        assert "not found" in output_lower or "not recognized" in output_lower
        assert len(shell_instance.session.command_history) == 1
        history = shell_instance.session.command_history[0]
        assert history["command"] == "invalid_command"
