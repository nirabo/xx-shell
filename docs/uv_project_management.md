# Project Management with UV

## Overview
`uv` is a fast Python package and project manager written in Rust. It replaces tools like `pip`, `pip-tools`, `pipx`, and `poetry` while being significantly faster.

## Key Features
- **Package Management**: Install, uninstall, and manage Python packages.
- **Virtual Environments**: Create and manage isolated Python environments.
- **Dependency Resolution**: Fast and reliable dependency resolution.
- **Project Initialization**: Set up new Python projects quickly.
- **Script Support**: Run Python scripts with ease.

## Installation
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Quickstart
### Create a Virtual Environment
```bash
uv venv
```

### Install Packages
```bash
uv pip install <package>
```

### Freeze Requirements
```bash
uv pip freeze > requirements.txt
```

### Run a Script
```bash
uv run script.py
```

## Advanced Usage
### Dependency Management
- **Install from `requirements.txt`**:
  ```bash
  uv pip install -r requirements.txt
  ```
- **Upgrade Packages**:
  ```bash
  uv pip install --upgrade <package>
  ```

### Project Initialization
- **Create a New Project**:
  ```bash
  uv init <project_name>
  ```

### Script Execution
- **Run a Script with Arguments**:
  ```bash
  uv run script.py --arg1 value1 --arg2 value2
  ```

## Documentation
- [Official Documentation](https://docs.astral.sh/uv/)
- [GitHub Repository](https://github.com/astral-sh/uv)
