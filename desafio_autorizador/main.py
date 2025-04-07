from datetime import datetime

from desafio_autorizador.models.account import Account
from desafio_autorizador.models.transaction import Transaction


def main():
    """
    Main function that demonstrates the creation of an account and the processing of transactions.
    """
    # Creating an account with a limit of 1000
    account = Account(active=True, available_limit=1000)

    # Creating a transaction of 100 for merchant 'Loja A' at the current date and time
    transaction = Transaction(merchant="Loja A", amount=100, time=datetime.now())

    # Processing the transaction
    if account.process_transaction(transaction):
        print("Transação aprovada.")
    else:
        print("Transação recusada.")

    # Displaying the current state of the account
    print(account)

    # Creating a transaction of 200 for merchant 'Loja B' at the current date and time
    transaction = Transaction(merchant="Loja B", amount=200, time=datetime.now())

    # Processing the transaction
    if account.process_transaction(transaction):
        print("Transação aprovada.")
    else:
        print("Transação recusada.")

    # Displaying the current state of the account
    print(account)

    # Creating a transaction of 800 for merchant 'Loja C' at the current date and time
    transaction = Transaction(merchant="Loja C", amount=800, time=datetime.now())

    # Processing the transaction
    if account.process_transaction(transaction):
        print("Transação aprovada.")
    else:
        print("Transação recusada.")

    # Displaying the current state of the account
    print(account)

    account.deactivate()  # Deactivating the account

    # Creating a transaction of 100 for merchant 'Loja D' at the current date and time in a deactivated account
    transaction = Transaction(merchant="Loja D", amount=100, time=datetime.now())

    # Processing the transaction
    if account.process_transaction(transaction):
        print("Transação aprovada.")
    else:
        print("Transação recusada.")

    # Displaying the current state of the account
    print(account)


if __name__ == "__main__":
    main()
