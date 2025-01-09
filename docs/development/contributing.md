# Contributing Guide

## Getting Started
1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR-USERNAME/xx-shell.git
   ```
3. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Workflow
1. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```
2. Make your changes following the coding conventions
3. Run tests:
   ```bash
   pytest
   ```
4. Commit your changes using conventional commits:
   ```bash
   git commit -m "feat: add new feature"
   git commit -m "fix: resolve issue with X"
   git commit -m "docs: update contributing guide"
   ```

## Pull Requests
1. Push your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
2. Create a pull request
3. Include:
   - Description of changes
   - Related issue number (if applicable)
   - Test coverage information
   - Documentation updates

## Code Style
- Follow PEP 8 with 100 character line length
- Use type hints for all public APIs
- Include docstrings in Google style format
- Write tests for all new features

## Issue Reporting
- Use the issue template
- Include:
  - Steps to reproduce
  - Expected behavior
  - Actual behavior
  - Environment details
