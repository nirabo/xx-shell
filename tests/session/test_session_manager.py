"""Unit tests for session management functionality."""

import pytest

from xx_shell.session import SessionManager


@pytest.mark.unit
class TestSessionManager:
    """Test cases for session management."""

    def test_session_creation(self, session_manager: SessionManager) -> None:
        """Test creating a new session."""
        session = session_manager.create_session()
        assert session.session_id is not None
        assert session_manager.get_session(session.session_id) == session

    def test_session_persistence(
        self, session_manager: SessionManager, tmp_path: str
    ) -> None:
        """Test session save/load functionality.

        Verifies that sessions can be properly saved and loaded with
        their command history intact.
        """
        # Create and save session
        session = session_manager.create_session()
        session.add_command("ls -la", "dummy output")
        session_manager.save_session(session)

        # Load session
        loaded = session_manager.load_session(session.session_id)
        assert loaded is not None
        if loaded:  # Type guard
            assert loaded.session_id == session.session_id
            # Fix the assertion to check the command history structure
            assert len(loaded.command_history) == 1
            assert loaded.command_history[0]["command"] == "ls -la"
            assert loaded.command_history[0]["output"] == "dummy output"
            assert "timestamp" in loaded.command_history[0]

    def test_session_listing(self, session_manager: SessionManager) -> None:
        """Test listing available sessions."""
        session1 = session_manager.create_session()
        session2 = session_manager.create_session()

        sessions = session_manager.list_sessions()
        assert len(sessions) == 2
        assert session1.session_id in sessions
        assert session2.session_id in sessions
