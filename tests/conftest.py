"""Test configuration and fixtures for XX Shell tests."""

import pytest
from xx_shell.core import Shell
from xx_shell.session import SessionManager


@pytest.fixture
def shell_instance() -> Shell:
    """Fixture providing a clean shell instance."""
    return Shell()


@pytest.fixture
def session_manager(tmp_path: str) -> SessionManager:
    """Fixture providing a session manager with isolated storage."""
    return SessionManager(storage_path=tmp_path)


@pytest.fixture
def mcp_server() -> None:
    """Fixture providing a mock MCP server."""
    # TODO: Implement mock MCP server
    return None
