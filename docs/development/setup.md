# Development Setup

## Prerequisites
- Python 3.10+
- UV package manager
- Git

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-org/xx-aider.git
   cd xx-aider
   ```

2. Create virtual environment:
   ```bash
   uv venv .venv
   ```

3. Activate environment:
   ```bash
   source .venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   uv pip install -r requirements.txt -r requirements-dev.txt
   ```

## Development Tools
- Formatting: `black` and `isort`
- Linting: `flake8`
- Type checking: `mypy`
- Testing: `pytest`

## Pre-commit Hooks
Install pre-commit hooks:
```bash
pre-commit install
```

## Running Tests
Run all tests:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov
```
