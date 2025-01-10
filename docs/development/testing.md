# Testing Guide

## Test Structure
- Unit tests in `tests/unit/`
- Integration tests in `tests/integration/`
- End-to-end tests in `tests/e2e/`

## Running Tests
Run all tests:
```bash
pytest
```

Run specific test category:
```bash
pytest tests/unit/
pytest tests/integration/
pytest tests/e2e/
```

## Test Coverage
Generate coverage report:
```bash
pytest --cov
```

View HTML coverage report:
```bash
pytest --cov --cov-report=html
```

## Parallel Testing
Run tests in parallel:
```bash
pytest -n auto
```

## Common Test Patterns
### Testing Session Management
When testing session functionality, verify the command history structure:

```python
def test_session_history(session):
    session.add_command("ls -la", "output")
    history = session.command_history
    
    assert len(history) == 1
    assert history[0]["command"] == "ls -la"
    assert history[0]["output"] == "output"
    assert "timestamp" in history[0]
```

### Testing Persistence
When testing session persistence, verify the complete round-trip:

```python
def test_session_persistence(session_manager):
    # Create and save session
    session = session_manager.create_session()
    session.add_command("cmd", "output")
    session_manager.save_session(session)
    
    # Load and verify
    loaded = session_manager.load_session(session.session_id)
    assert loaded.command_history[0]["command"] == "cmd"
    assert loaded.command_history[0]["output"] == "output"
```

### Mocking
Use pytest-mock for mocking:
```python
def test_something(mocker):
    mock_func = mocker.patch('module.function')
    # test code
```

### Async Tests
Use pytest-asyncio for async tests:
```python
@pytest.mark.asyncio
async def test_async_function():
    result = await async_function()
    assert result == expected
```

## Test Configuration
- Configured in `pytest.ini`
- Includes default markers and options
- Supports parallel execution
