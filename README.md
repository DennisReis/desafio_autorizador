# 💳 Desafio Autorizador

Projeto de CLI em Python para simular um sistema de autorização de transações, com estrutura modular, testes unitários e empacotamento como pacote instalável via `uv`.

---

## 📁 Estrutura do Projeto

```bash
desafio_autorizador/
│
├── desafio_autorizador/        # Módulo principal
│   ├── main.py                  # Execução do Autorizador
│
├── tests/                      # Testes unitários
│   ├── test_account.py
│   └── test_transaction.py
│
├── Makefile                    # Automação de comandos
├── pyproject.toml              # Configuração PEP 621 (usando setuptools)
└── README.md
```

---

## ✨ Instalação

### Requisitos

- Python >= 3.9
- [uv](https://github.com/astral-sh/uv) instalado globalmente

### Instalação via Makefile

```bash
make install
```

Este comando irá:

- Criar um ambiente virtual `.venv`
- Instalar dependências e o pacote em modo editável (`pip install -e .`)

---

## 🧰 Comandos disponíveis

| Comando           | Descrição                                              |
|-------------------|--------------------------------------------------------|
| `make install`    | Cria o venv e instala o projeto no ambiente            |
| `make test`       | Roda os testes unitários com `unittest`               |
| `make run`        | Executa o a versao do autorizador gerada pelo `make install`  |
| `make clean`      | Remove diretórios e arquivos temporários              |

---

## 🔧 Uso da Autorizador

Após a instalação, execute:

```bash
desafio-autorizador
```

---

## 🥪 Executando os Testes

```bash
make test
```

Ou manualmente com:

```bash
python3 -m unittest discover -s tests -v
```

---

## ✅ Status

- [] Estrutura modular com models
- [] CLI funcional com `argparse`
- [x] Testes unitários com `unittest`
- [] Build e distribuição com `setuptools`
- [x] Gerenciamento com `Makefile` e `uv`

---

## 👤 Autor

Dennis Reis
📧 [dmpreis@gmail.com](mailto:dmpreis@gmail.com)

---

## 📄 Licença

MIT
