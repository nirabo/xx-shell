# Help banner
.PHONY: help
help:
	@echo "XX Shell Development Makefile"
	@echo
	@echo "Available targets:"
	@echo "  help         Show this help message"
	@echo "  install      Install project dependencies"
	@echo "  test         Run tests with coverage"
	@echo "  lint         Run code linting and type checking"
	@echo "  format       Format code with black and isort"
	@echo "  docs         Build and serve documentation locally"
	@echo "  docs-build   Build documentation for deployment"
	@echo "  clean        Clean build artifacts and caches"
	@echo "  venv         Create virtual environment"
	@echo
	@echo "Environment:"
	@echo "  VENV         $(VENV)"
	@echo "  PYTHONPATH   $(PYTHONPATH)"
	@echo
	@echo "Run 'make <target>' to execute a specific command"

# Project Configuration
PROJECT_NAME := xx_shell
PYTHON := python3
UV := uv
VENV := .venv
PYTHONPATH := $(shell pwd)/src

# Targets
.PHONY: all install test lint format docs docs-build serve-docs clean help venv

all: help

# Virtual Environment
$(VENV)/bin/activate:
	$(UV) venv $(VENV)

venv: $(VENV)/bin/activate

# Installation
install: venv
	. $(VENV)/bin/activate && $(UV) pip install -r requirements.txt
	. $(VENV)/bin/activate && $(UV) pip install -r requirements-dev.txt
	. $(VENV)/bin/activate && $(UV) pip install -e .

# Testing
test: venv
	. $(VENV)/bin/activate && $(UV) pip install -r requirements-dev.txt
	PYTHONPATH=$(PYTHONPATH) \
	. $(VENV)/bin/activate && $(PYTHON) -m pytest tests/ --cov=$(PROJECT_NAME) --cov-report=xml

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
	. $(VENV)/bin/activate && $(UV) pip install -r requirements-docs.txt
	. $(VENV)/bin/activate && $(PYTHON) -m mkdocs serve

docs-build: venv
	. $(VENV)/bin/activate && $(UV) pip install -r requirements-docs.txt
	. $(VENV)/bin/activate && $(PYTHON) -m mkdocs build

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
