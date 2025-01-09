# Installation

## Prerequisites
- Python 3.8 or higher
- pip or uv package manager

## Installation Methods

### Using pip
```bash
pip install xx-shell
```

### Using uv
```bash
uv pip install xx-shell
```

### From Source
1. Clone the repository:
   ```bash
   git clone https://github.com/your-org/xx-shell.git
   cd xx-shell
   ```

2. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```

3. Install the package:
   ```bash
   uv pip install -e .
   ```

## Verifying Installation
Run the following command to verify the installation:
```bash
xx-shell --version
```

## Troubleshooting
If you encounter any issues:
- Ensure Python is installed correctly
- Check your PATH environment variable
- Verify pip/uv is up to date
