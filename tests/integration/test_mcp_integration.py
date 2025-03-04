"""Integration tests for MCP functionality."""

import pytest

from xx_shell.core import Shell
from xx_shell.plugins import MCPPlugin


@pytest.mark.integration
class TestMCPIntegration:
    """Test cases for MCP integration."""

    def test_mcp_plugin_loading(self, shell_instance: Shell) -> None:
        """Test MCP plugin initialization."""
        plugin = MCPPlugin()
        shell_instance.load_plugin(plugin)

        assert "mcp" in shell_instance.available_commands
        assert shell_instance.get_plugin("mcp").name == "mcp"

    def test_mcp_command_execution(
        self, shell_instance: Shell, mcp_server: None
    ) -> None:
        """Test basic MCP command execution.

        Verifies that MCP commands can be properly executed through
        the shell interface.
        """
        # TODO: Implement with mock MCP server
        pass
