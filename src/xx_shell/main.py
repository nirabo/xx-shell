"""XX Shell main entry point."""

import argparse
from typing import Optional, Sequence

from xx_shell.version import __version__


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    """Parse command line arguments.

    Args:
        argv: Optional sequence of arguments to parse

    Returns:
        Parsed arguments namespace
    """
    parser = argparse.ArgumentParser(
        description="XX Shell - The Intelligent Command Shell"
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"xx-shell {__version__}"
    )
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> None:
    """Execute the xx-shell command line interface.

    Args:
        argv: Optional sequence of arguments to pass
    """
    # Parse args to handle --version and --help flags
    parse_args(argv)
    print(f"XX Shell {__version__} - Welcome!")

    # Start interactive shell if no specific commands were provided
    if not argv:
        from xx_shell.core import Shell
        shell = Shell()
        shell.show_help()
        print("Type 'exit' to quit")

        while True:
            try:
                command = input("xx> ")
                if command == "exit":
                    break
                # TODO: Process command through shell
            except (EOFError, KeyboardInterrupt):
                print("\nExiting...")
                break
