.PHONY: install test run clean

install:
	@echo "Instalando dependências..."
	@cd desafio_autorizador \
	uv venv .venv && uv pip install -e .
	@cd ..

test:
	@echo "Rodando testes..."
	@python3 -m unittest discover -s tests -v

run: install
	@echo "Executando Desafio Autorizador..."
	@desafio-autorizador

clean:
	@echo "Limpando arquivos desnecessários..."
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -name "*.pyc" -delete
