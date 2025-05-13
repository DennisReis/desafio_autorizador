# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-05-13

### Added
- Conventional commits setup with commitizen
- Commit linting with commitlint
- Pre-commit hooks for enforcing commit format
- First stable release with full transaction authorization functionality

## [0.1.0] - Initial Version

### Added
- Basic transaction authorization system
- Account model with active status and available limit
- Transaction model with merchant, amount, and timestamp
- Transaction processing with validation
- DenyMerchants data structure for merchant blacklisting
- Methods for querying transaction history (highest/lowest, latest/oldest)
- Unit tests for core functionality