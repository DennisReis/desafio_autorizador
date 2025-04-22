from datetime import datetime

from desafio_autorizador.models.account import Account
from desafio_autorizador.models.transaction import Transaction
from desafio_autorizador.models.deny_merchants import DenyMerchants


def main():
    """
    Main function that demonstrates the creation of an account and the processing of transactions.
    """
    deny_merchants = DenyMerchants()
    deny_merchants.add_merchant("Loja D")  # Adding 'Loja D' to the denied merchants list

    # Creating an account with a limit of 1000
    account = Account(active=True, available_limit=1000)

    transaction = Transaction(merchant="Loja A", amount=150, time=datetime.now())
    account.process_transaction(transaction, deny_merchants)

    transaction = Transaction(merchant="Loja B", amount=200, time=datetime.now())
    account.process_transaction(transaction, deny_merchants)

    transaction = Transaction(merchant="Loja C", amount=800, time=datetime.now())
    account.process_transaction(transaction, deny_merchants)

    account.deactivate()
    transaction = Transaction(merchant="Loja D", amount=100, time=datetime.now())
    account.process_transaction(transaction, deny_merchants)

    account.activate()
    transaction = Transaction(merchant="Loja D", amount=100, time=datetime.now())
    account.process_transaction(transaction, deny_merchants)

    # Final account status
    print("\nResumo:")
    print(account)

    highest = account.get_highest_transaction()
    if highest:
        print(f"Maior transação: {highest}")
    else:
        print("Nenhuma transação registrada.")

    lowest = account.get_lowest_transaction()
    if lowest:
        print(f"Menor transação: {lowest}")
    else:
        print("Nenhuma transação registrada.")

    latest = account.get_latest_transaction()
    if latest:
        print(f"Transação mais recente: {latest}")
    else:
        print("Nenhuma transação registrada.")

    oldest = account.get_oldest_transaction()
    if oldest:
        print(f"Transação mais antiga: {oldest}")
    else:
        print("Nenhuma transação registrada.")


if __name__ == "__main__":
    main()
