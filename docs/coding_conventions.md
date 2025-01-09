# Python Project Best Practices and Coding Conventions

## Project Structure
- Use PyScaffold for project initialization and structure
- Follow the src-layout pattern
- Maintain clear separation between source code, tests, and documentation
- Keep configuration in dedicated config files

## Development Environment
### UV (astral-sh/uv)
- Use `uv` as a faster alternative to pip
- Create virtual environments with: `uv venv`
- Install packages: `uv pip install <package>`
- Generate requirements: `uv pip freeze > requirements.txt`

## Testing
### pytest Framework
- Write tests in `tests/` directory
- Use fixtures for test setup
- Aim for high test coverage (>80%)
- Include unit, integration, and end-to-end tests
- Use parametrized tests when testing similar scenarios

## Documentation
### Tools
- Use Sphinx for API documentation
- MkDocs for project documentation
- Write docstrings in Google style
- Keep README.md up to date
- Document all public APIs

## Code Quality
- Use pre-commit hooks
- Follow PEP 8 style guide
- Use type hints (PEP 484)
- Implement proper logging
- Use pylint/flake8 for linting

## GitHub Workflow
### Continuous Integration
- Run tests on every pull request
- Enforce code quality checks
- Automate documentation builds
- Use semantic versioning
- Implement branch protection rules

### GitHub Actions
- Test on multiple Python versions
- Run security scans
- Deploy documentation
- Automate PyPI releases

## PyPI Distribution
- Use `pyproject.toml` for build configuration
- Include proper package metadata
- Sign releases with GPG
- Use GitHub Actions for automated releases
- Include proper license and documentation

## Security
- Keep dependencies updated
- Run security scans regularly
- Use environment variables for secrets
- Implement proper input validation
- Follow security best practices

## Version Control
- Use meaningful commit messages
- Follow conventional commits specification
- Create detailed pull request descriptions
- Review code before merging
- Tag releases properly

## Project Management
- Use GitHub Issues for task tracking
- Implement project boards
- Set up templates for issues and PRs
- Document release process
- Maintain a changelog
