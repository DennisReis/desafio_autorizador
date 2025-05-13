SHELL = /bin/bash
VERSION ?= $$(cat pyproject.toml | grep version | cut -d'=' -f2 | tr -d ' "' | head -n 1)
PROJECT_NAME = desafio_autorizador
PROJECT_DIR = $(shell pwd)

.PHONY: precommit install test build run lint format clean commit
.ONESHELL:
.EXPORT_ALL_VARIABLES:

.DEFAULT_GOAL := help

version:  ## Show project version, directory and name
	@echo "[INFO] Project version: $(VERSION)"
	@echo "[INFO] Project DIR....: $(PROJECT_DIR)"
	@echo "[INFO] Project name...: $(PROJECT_NAME)"

help:  ## Show this help
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/:.*##/;/' | column -t -s ';'

precommit:  ## Installs and runs pre-commit hooks
	@echo "[INFO] Installing pre-commit..."
	@pre-commit install
	@pre-commit run --all-files

install:  ## Installs project dependencies with dev requirements
	@echo "[INFO] Installing dependencies..."
	uv venv .venv && uv pip install -e ".[dev]"

test:  ## Runs the tests
	@echo "[INFO] Running tests..."
	@python3 -m unittest discover -s tests -v

build: test  ## Builds the project
	@echo "[INFO] Building the project using UV..."
	uv build

run: build  ## Runs the project from the built package
	@echo "[INFO] Executing "Desafio do Autorizador" using built project..."
	@uv run --with $(PROJECT_DIR)/dist/$(PROJECT_NAME)-$(VERSION)-py3-none-any.whl --no-project -- desafio-autorizador

lint:  ## Lints the code
	@ruff check desafio_autorizador tests

format:  ## Formats the code
	@black desafio_autorizador tests
	@isort desafio_autorizador tests


clean:  ## Cleans up unnecessary files
	@echo "Cleaning up unnecessary files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -name "*.pyc" -delete

commit:  ## Create a commit using commitizen (follows Conventional Commits)
	@echo "[INFO] Creating a commit using conventional commit format..."
	@cz commit
