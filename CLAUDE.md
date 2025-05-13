# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands Reference

### Project Setup and Management
```bash
# Install project and dependencies
make install

# Run tests
make test

# Run a specific test (use unittest pattern)
python -m unittest tests.test_account.TestAccount.test_process_transaction_sufficient_limit

# Lint the code
make lint

# Format the code
make format

# Build the project for distribution
make build

# Run the project from the built package
make run

# Clean up temporary files
make clean

# Create a commit using conventional commit format (guided)
make commit
```

## Project Architecture

This project implements a transaction authorization system with the following components:

### Core Models

1. **Account** (`desafio_autorizador/models/account.py`)
   - Represents a bank account with active status and available credit limit
   - Processes transactions, validating if they can be approved
   - Maintains a transaction history
   - Provides methods to query transaction history (highest/lowest amount, latest/oldest)

2. **Transaction** (`desafio_autorizador/models/transaction.py`)
   - Represents a financial transaction with merchant, amount, and timestamp

3. **DenyMerchants** (`desafio_autorizador/models/deny_merchants.py`)
   - Maintains a list of merchants whose transactions should be denied
   - Provides methods to add, remove, and check merchants

### Transaction Authorization Flow

1. The system receives a transaction request containing merchant, amount, and timestamp
2. It validates the transaction against three criteria:
   - Account must be active
   - Account must have sufficient available limit
   - Merchant must not be in the denied list
3. If the transaction is approved, it:
   - Reduces the account's available limit
   - Adds the transaction to the account's history
4. Returns a result object with approval status and reason (if declined)

### Development Tools

The project uses:
- `ruff`, `black`, and `isort` for code formatting and linting
- `unittest` for testing
- `uv` for package management and virtual environment
- `setuptools` for building and distribution
- `commitizen` for generating conventional commits

### Commit Guidelines

This repository follows the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- Format: `<type>[optional scope]: <description>`
- Common types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `build`, `ci`, `chore`
- Examples:
  - `feat: add new merchant validation`
  - `fix(transaction): prevent duplicate processing`
  - `refactor: simplify account validation logic`

Use `make commit` to create commits with the proper format using commitizen.