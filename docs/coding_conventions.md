# XX Shell Mode Coding Conventions

## Project Structure
- Use src-layout pattern with `src/xx_shell` as main package
- Separate modules for:
  - `core/`: Core interpreter and execution logic
  - `commands/`: Command implementations
  - `plugins/`: Plugin system components
  - `session/`: Session management
  - `ui/`: User interface components
- Maintain dedicated directories for:
  - `tests/`: Unit and integration tests
  - `docs/`: Project documentation
  - `scripts/`: Development and build scripts

## Development Environment
### UV Integration
- Use `uv` for package management
- Create virtual environment: `uv venv .venv`
- Install dependencies: `uv pip install -r requirements.txt`
- Generate requirements: `uv pip freeze > requirements.txt`

## Testing
### pytest Framework
- Write tests in `tests/` directory with mirror structure
- Use fixtures for command execution setup
- Include tests for:
  - Command parsing and validation
  - Session state management
  - Plugin system integration
  - Cross-platform compatibility

## Documentation
### Tools
- Use Sphinx for API documentation
- MkDocs for user documentation
- Write docstrings in Google style
- Include examples in docstrings
- Document all public APIs and commands

## Code Quality
- Use pre-commit hooks for:
  - Black formatting
  - isort imports
  - flake8 linting
  - mypy type checking
- Follow PEP 8 with exceptions:
  - Allow line length up to 100 characters
  - Use descriptive variable names
  - Prefer explicit over implicit

## Session Management
### Code Organization
- Store session state in `~/.xx/sessions/`
- Use JSON format for session files
- Implement session classes in `session/` module
- Include versioning in session format

### Error Handling
- Use custom exceptions for session errors
- Implement proper cleanup on errors
- Include detailed error messages
- Maintain backward compatibility

## Command Implementation
### Style Guide
- Use snake_case for command names
- Implement commands as classes
- Include help text as class docstring
- Use type hints for command parameters
- Implement input validation

## Plugin System
### Development Guidelines
- Use plugin base class from `plugins/base.py`
- Implement required interface methods
- Include plugin metadata
- Document plugin configuration
- Handle errors gracefully

## Version Control
- Use conventional commits
- Include issue references in commit messages
- Create feature branches
- Review code before merging
- Tag releases with semantic versioning
