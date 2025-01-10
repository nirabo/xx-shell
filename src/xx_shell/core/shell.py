"""Core shell implementation."""


class Shell:
    """Main shell class that handles command execution and state management."""

    def __init__(self):
        """Initialize a new shell instance."""
        self.session = None
        self.available_commands = {}
        self.plugins = {}

    def parse_command(self, command: str) -> list[str]:
        """Parse a command string into its components.

        Args:
            command: The command string to parse

        Returns:
            List of command components
        """
        return command.split()

    def validate_command(self, command: str) -> bool:
        """Validate if a command is supported.

        Args:
            command: The command to validate

        Returns:
            True if command is valid/supported, False otherwise
        """
        return command in self.available_commands

    def load_plugin(self, plugin) -> None:
        """Load a plugin into the shell.

        Args:
            plugin: The plugin instance to load
        """
        self.plugins[plugin.name] = plugin
        self.available_commands.update(plugin.commands)
