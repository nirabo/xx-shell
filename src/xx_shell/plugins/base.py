"""Base plugin implementation."""

from typing import Any, Callable, Dict


class Plugin:
    """Base class for all XX Shell plugins."""

    def __init__(self, name: str) -> None:
        """Initialize a new plugin instance.

        Args:
            name: The name of the plugin
        """
        self.name = name
        self.commands: Dict[str, Callable[..., Any]] = {}

    def register_command(self, name: str, handler: Callable[..., Any]) -> None:
        """Register a new command with the plugin.

        Args:
            name: The name of the command
            handler: The function to handle the command
        """
        self.commands[name] = handler
