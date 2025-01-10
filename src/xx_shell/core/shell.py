"""Core shell implementation."""

from typing import TYPE_CHECKING, Any, Callable

if TYPE_CHECKING:
    from xx_shell.plugins import Plugin


class Shell:
    """Main shell class that handles command execution and state management."""

    def __init__(self) -> None:
        """Initialize a new shell instance."""
        from xx_shell.session import SessionManager
        self.session_manager = SessionManager(storage_path="~/.xx/sessions")
        self.session = self.session_manager.create_session()
        self.available_commands: dict[str, Callable[..., Any]] = {
            "help": self.show_help
        }
        self.plugins: dict[str, Plugin] = {}

    def show_help(self) -> None:
        """Show help information."""
        print("Available commands:")
        for cmd in sorted(self.available_commands):
            print(f"  {cmd}")

    def parse_command(self, command: str) -> list[str]:
        """Parse a command string into its components.

        Args:
            command: The command string to parse

        Returns:
            List of command components
        """
        import shlex
        return shlex.split(command)

    def validate_command(self, command: str) -> bool:
        """Validate if a command is supported.

        Args:
            command: The command to validate

        Returns:
            True if command is valid/supported, False otherwise
        """
        return command in self.available_commands

    def execute_command(self, command: str) -> str:
        """Execute a system command and return its output.

        Args:
            command: The command to execute

        Returns:
            The command output as a string
        """
        import subprocess
        try:
            result = subprocess.run(
                command,
                shell=True,
                check=True,
                text=True,
                capture_output=True
            )
            output = result.stdout
            self.session.add_command(command, output)
            return output
        except subprocess.CalledProcessError as e:
            output = e.stderr
            self.session.add_command(command, output)
            return output

    def load_plugin(self, plugin: "Plugin") -> None:
        """Load a plugin into the shell.

        Args:
            plugin: The plugin instance to load
        """
        self.plugins[plugin.name] = plugin
        self.available_commands.update(plugin.commands)

    def get_plugin(self, name: str) -> "Plugin":
        """Get a loaded plugin by name.

        Args:
            name: The name of the plugin to retrieve

        Returns:
            The plugin instance if found

        Raises:
            KeyError: If no plugin with the given name exists
        """
        return self.plugins[name]
