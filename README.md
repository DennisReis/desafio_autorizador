# 💳 Desafio Autorizador

Python CLI project to simulate a transaction authorization system, with a modular structure, unit tests, and packaging as an installable package via `uv`.

---

## 📁 Project Structure

```bash
desafio_autorizador/
│
├── desafio_autorizador/        # Main module
│   ├── main.py                 # Authorizer execution
├── models/                     # Module with data structure definitions
│   ├── account.py              # Account data structure
│   ├── transaction.py          # Transaction data structure
│
├── tests/                      # Unit tests
│   ├── test_account.py
│   └── test_transaction.py
│
├── Makefile                    # Command automation
├── pyproject.toml              # PEP 621 configuration (using setuptools)
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

- Create a virtual environment `.venv`
- Install dependencies and the package in editable mode (`pip install -e .`)

---

## 🧰 Available Commands

| Command           | Description                                              |
|-------------------|----------------------------------------------------------|
| `make version`    | Show project version, directory and name                |
| `make help`       | Show this help                                           |
| `make precommit`  | Installs and runs pre-commit hooks                       |
| `make install`    | Installs project dependencies                            |
| `make test`       | Runs the tests                                           |
| `make build`      | Builds the project                                       |
| `make run`        | Runs the project from the built package                 |
| `make lint`       | Lints the code                                           |
| `make format`     | Formats the code                                         |
| `make clean`      | Cleans up unnecessary files                              |

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

## ✅ Status

- [x] Modular structure with models
- [ ] Functional CLI with `argparse`
- [x] Unit tests with `unittest`
- [x] Build and distribution with `setuptools`
- [x] Project management with `Makefile` and `uv`

---

Dennis Reis
📧 [dmpreis@gmail.com](mailto:dmpreis@gmail.com)

---

## 📄 License

MIT
