# 💳 Transaction Authorizer Challenge

Python CLI project simulating a transaction authorization system, featuring modular structure, unit tests, and distribution packaging via `uv`.

---

## 📁 Project Structure

```bash
desafio_autorizador/
│
├── desafio_autorizador/        # Main module
│   ├── main.py                  # Authorizer execution
├── models/                     # Data structure definitions
│   ├── account.py              # Account data structure
│   ├── transaction.py          # Transaction data structure
│
├── tests/                      # Unit tests
│   ├── test_account.py
│   └── test_transaction.py
│
├── Makefile                    # Command automation
├── pyproject.toml              # PEP 621 configuration (setuptools)
└── README.md
```

---

## ✨ Installation

### Requirements

- Python >= 3.9
- [uv](https://github.com/astral-sh/uv) installed globally

### Installation via Makefile

```bash
make install
```

This command will:

- Create a `.venv` virtual environment
- Install dependencies and the package in editable mode (`pip install -e .`)

---

## 🔧 Using the Authorizer

After installation, run:

```bash
desafio-autorizador
```

---

## 🥪 Running Tests

```bash
make test
```

Or manually with:

```bash
python3 -m unittest discover -s tests -v
```

---

## 🧱 Building the Project

To build the project into `.whl` and `.tar.gz` formats:

```bash
make build
```

The artifacts will be created inside the `dist/` folder.

To install one of the generated packages:

```bash
uv pip install dist/<your_package_name>.whl
```

Or:

```bash
uv pip install dist/<your_package_name>.tar.gz
```

To run the project from the built package, use:

```bash
make run
```

Note: `make run` automatically triggers `make build` if needed.

---

## 🧰 Available targets in the Makefile

| Command           | Description                                              |
|-------------------|----------------------------------------------------------|
| `make version`    | Show project version, directory and name                |
| `make help`       | Show this help                                           |
| `make precommit`  | Installs and runs pre-commit hooks                      |
| `make install`    | Installs project dependencies                           |
| `make test`       | Runs the tests                                           |
| `make build`      | Builds the project into distributable formats           |
| `make run`        | Runs the project from the built package (requires build) |
| `make lint`       | Lints the code                                           |
| `make format`     | Formats the code                                         |
| `make clean`      | Cleans up unnecessary files                             |

---

## ✅ Status

- [x] Modular structure with models
- [ ] Functional CLI with `argparse`
- [x] Unit tests with `unittest`
- [x] Build and distribution with `setuptools`
- [x] Management via `Makefile` and `uv`

---

## 👤 Author

Dennis Reis
📧 [dmpreis@gmail.com](mailto:dmpreis@gmail.com)

---

## 📄 License

MIT
