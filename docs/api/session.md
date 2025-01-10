# Session API Reference

## Classes
### Session
Manage shell session state

```python
class Session:
    def __init__(self, session_id: str):
        """Initialize session with unique ID"""
    
    def add_command(self, command: str, output: str) -> None:
        """Add command to history with metadata
        Args:
            command: The executed command string
            output: The command's output
        """
    
    def save(self, path: str):
        """Save session state to file"""
    
    def load(self, path: str):
        """Load session state from file"""
```

### SessionManager
Manage multiple sessions

```python
class SessionManager:
    def __init__(self):
        """Initialize session manager"""
    
    def create_session(self) -> Session:
        """Create new session"""
    
    def get_session(self, session_id: str) -> Session:
        """Get session by ID"""
```

## Command History Structure
Command history is stored as a list of dictionaries with the following structure:
```python
{
    "command": str,  # The executed command
    "output": str,   # Command output
    "timestamp": str # ISO format timestamp
}
```
