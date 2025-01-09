# Session API Reference

## Classes
### Session
Manage shell session state

```python
class Session:
    def __init__(self, session_id: str):
        """Initialize session with unique ID"""
    
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

## Functions
### serialize_session
Serialize session state

```python
def serialize_session(session: Session) -> str:
    """Convert session to JSON string"""
```

### deserialize_session
Deserialize session state

```python
def deserialize_session(data: str) -> Session:
    """Create session from JSON string"""
```
