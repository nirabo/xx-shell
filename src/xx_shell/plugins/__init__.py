"""Plugin system for XX Shell."""

from .base import Plugin
from .mcp import MCPPlugin

__all__ = ["Plugin", "MCPPlugin"]
