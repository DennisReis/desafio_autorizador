.PHONY: install test run clean

precommit:
	pre-commit install
	pre-commit run --all-files

install:
	@echo "Instalando dependências..."
	uv venv .venv && uv pip install -e .
	@cd ..

test:
	@echo "Rodando testes..."
	@python3 -m unittest discover -s tests -v

run: install
	@echo "Executando Desafio Autorizador..."
	@desafio-autorizador

lint:
	ruff check desafio_autorizador tests

format:
	black desafio_autorizador tests
	isort desafio_autorizador tests


clean:
	@echo "Limpando arquivos desnecessários..."
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -name "*.pyc" -delete
