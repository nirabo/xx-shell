"""Unit tests for session management functionality."""

import pytest


@pytest.mark.unit
class TestSessionManager:
    """Test cases for session management."""

    def test_session_creation(self, session_manager: SessionManager) -> None:
        """Test creating a new session."""
        session = session_manager.create_session()
        assert session.id is not None
        assert session_manager.get_session(session.id) == session

    def test_session_persistence(self, session_manager: SessionManager, tmp_path) -> None:
        """Test session save/load functionality."""
        # Create and save session
        session = session_manager.create_session()
        session.add_command("ls -la")
        session_manager.save_session(session)

        # Load session
        loaded = session_manager.load_session(session.id)
        assert loaded.id == session.id
        assert loaded.command_history == ["ls -la"]

    def test_session_listing(self, session_manager: SessionManager) -> None:
        """Test listing available sessions."""
        session1 = session_manager.create_session()
        session2 = session_manager.create_session()

        sessions = session_manager.list_sessions()
        assert len(sessions) == 2
        assert session1.id in sessions
        assert session2.id in sessions
