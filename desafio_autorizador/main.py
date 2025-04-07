from datetime import datetime

from desafio_autorizador.models.account import Account
from desafio_autorizador.models.transaction import Transaction


def main():
    """
    Função principal que demonstra a criação de uma conta e o processamento de uma transação.
    """
    # Criando uma conta com limite de 1000
    account = Account(active=True, available_limit=1000)

    # Criando uma transação de 100 para o comerciante 'Loja A' na data e hora atuais
    transaction = Transaction(merchant="Loja A", amount=100, time=datetime.now())

    # Processando a transação
    if account.process_transaction(transaction):
        print("Transação aprovada.")
    else:
        print("Transação recusada.")

    # Exibindo o estado atual da conta
    print(account)

    # Criando uma transação de 200 para o comerciante 'Loja B' na data e hora atuais
    transaction = Transaction(merchant="Loja B", amount=200, time=datetime.now())

    # Processando a transação
    if account.process_transaction(transaction):
        print("Transação aprovada.")
    else:
        print("Transação recusada.")

    # Exibindo o estado atual da conta
    print(account)

    # Criando uma transação de 800 para o comerciante 'Loja C' na data e hora atuais
    transaction = Transaction(merchant="Loja C", amount=800, time=datetime.now())

    # Processando a transação
    if account.process_transaction(transaction):
        print("Transação aprovada.")
    else:
        print("Transação recusada.")

    # Exibindo o estado atual da conta
    print(account)

    account.deactivate()  # Inativando a conta

    # Criando uma transação de 100 para o comerciante 'Loja D' na data e hora atuais em uma conta inativa
    transaction = Transaction(merchant="Loja D", amount=100, time=datetime.now())

    # Processando a transação
    if account.process_transaction(transaction):
        print("Transação aprovada.")
    else:
        print("Transação recusada.")

    # Exibindo o estado atual da conta
    print(account)


if __name__ == "__main__":
    main()
