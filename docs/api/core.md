# Core API Reference

## Classes
### Shell
Main shell class implementing core functionality

```python
class Shell:
    def __init__(self, config: dict = None):
        """Initialize shell with optional configuration"""
    
    def run(self, command: str) -> str:
        """Execute a shell command"""
```

### Command
Base command class for implementing commands

```python
class Command:
    def __init__(self, name: str, help_text: str):
        """Initialize command with name and help text"""
    
    def execute(self, args: list) -> str:
        """Execute command with provided arguments"""
```

## Functions
### parse_command
Parse input command string

```python
def parse_command(input: str) -> tuple[str, list]:
    """Parse command string into command name and arguments"""
```

### format_output
Format command output

```python
def format_output(output: str, style: str = "plain") -> str:
    """Format command output with specified style"""
```
