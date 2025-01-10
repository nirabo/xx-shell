"""Session manager implementation."""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional, List, Dict
import json
import uuid


@dataclass
class Session:
    """Represents a shell session."""

    session_id: str
    command_history: List[str]

    def __post_init__(self) -> None:
        """Initialize session defaults."""
        if not hasattr(self, 'command_history'):
            object.__setattr__(self, 'command_history', [])

    def add_command(self, command: str) -> None:
        """Add a command to the session history.

        Args:
            command: The command to add to history
        """
        self.command_history.append(command)


class SessionManager:
    """Manages shell sessions and their persistence."""

    def __init__(self, storage_path: str) -> None:
        """Initialize the session manager.

        Args:
            storage_path: Path to store session files
        """
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)
        self.sessions: Dict[str, Session] = {}

    def create_session(self) -> Session:
        """Create a new session.

        Returns:
            The newly created session
        """
        session_id = str(uuid.uuid4())
        session = Session(session_id=session_id)
        self.sessions[session_id] = session
        return session

    def get_session(self, session_id: str) -> Optional[Session]:
        """Get a session by ID.

        Args:
            session_id: The ID of the session to retrieve

        Returns:
            The session if found, None otherwise
        """
        return self.sessions.get(session_id)

    def save_session(self, session: Session) -> None:
        """Save a session to disk.

        Args:
            session: The session to save
        """
        session_file = self.storage_path / f"{session.session_id}.json"
        with open(session_file, "w") as f:
            json.dump({
                "session_id": session.session_id,
                "command_history": session.command_history
            }, f)

    def load_session(self, session_id: str) -> Optional[Session]:
        """Load a session from disk.

        Args:
            session_id: The ID of the session to load

        Returns:
            The loaded session if found, None otherwise
        """
        session_file = self.storage_path / f"{session_id}.json"
        if not session_file.exists():
            return None

        with open(session_file, "r") as f:
            data = json.load(f)
            return Session(
                session_id=data["session_id"],
                command_history=data["command_history"]
            )

    def list_sessions(self) -> List[str]:
        """List all available session IDs.

        Returns:
            List of session IDs
        """
        return list(self.sessions.keys())
