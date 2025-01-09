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
