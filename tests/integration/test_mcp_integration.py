import pytest
from xx_shell.core import Shell
from xx_shell.plugins import MCPPlugin

@pytest.mark.integration
class TestMCPIntegration:
    def test_mcp_plugin_loading(self, shell_instance):
        """Test MCP plugin initialization"""
        plugin = MCPPlugin()
        shell_instance.load_plugin(plugin)
        
        assert "mcp" in shell_instance.available_commands
        assert shell_instance.get_plugin("mcp") == plugin

    def test_mcp_command_execution(self, shell_instance, mcp_server):
        """Test basic MCP command execution"""
        # TODO: Implement with mock MCP server
        pass
