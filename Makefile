# Project Configuration
PROJECT_NAME := xx_shell
PYTHON := python3
UV := uv
VENV := .venv
PYTHONPATH := $(shell pwd)/src

# Targets
.PHONY: all install test lint format docs clean

all: install

# Virtual Environment
$(VENV)/bin/activate:
	$(UV) venv $(VENV)

venv: $(VENV)/bin/activate

# Installation
install: venv
	$(UV) pip install -r requirements.txt
	$(UV) pip install -r requirements-dev.txt
	$(PYTHON) -m pip install -e .
	$(PYTHON) -m pip install -e .

# Testing
test: venv
	$(UV) pip install -r requirements-dev.txt
	$(PYTHON) -m pytest tests/ --cov=$(PROJECT_NAME) --cov-report=xml

# Linting and Formatting
lint: venv
	. $(VENV)/bin/activate && $(PYTHON) -m flake8 src/ tests/
	. $(VENV)/bin/activate && $(PYTHON) -m mypy src/ tests/
	. $(VENV)/bin/activate && $(PYTHON) -m isort --check-only src/ tests/

format: venv
	$(PYTHON) -m black src/ tests/
	$(PYTHON) -m isort src/ tests/

# Documentation
docs: venv
	$(PYTHON) -m sphinx -b html docs/source docs/build
	$(PYTHON) -m mkdocs build

# Cleanup
clean:
	rm -rf $(VENV)
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf docs/build
	rm -rf dist
	rm -rf *.egg-info
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
