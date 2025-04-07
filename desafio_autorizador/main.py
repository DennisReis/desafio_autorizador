from datetime import datetime
from typing import List
#from models.account import Account
#from models.transaction import Transaction

class Transaction:
    def __init__(self, merchant: str, amount: int, time: datetime):
        self.merchant = merchant
        self.amount = amount
        self.time = time

    def __repr__(self):
        return f"Transaction(merchant='{self.merchant}', amount={self.amount}, time={self.time})"

class Account:
    def __init__(self, active: bool, available_limit: int):
        self.active = active
        self.available_limit = available_limit
        self.history: List[Transaction] = []

    def process_transaction(self, transaction: Transaction):
        if self.active and transaction.amount <= self.available_limit:
            self.available_limit -= transaction.amount
            self.history.append(transaction)
            return True
        return False

    def __repr__(self):
        return f"Account(active={self.active}, available_limit={self.available_limit}, history={self.history})"


def main():
    # Criando uma conta com limite de 1000
    account = Account(active=True, available_limit=1000)
    print("Estado inicial da conta:", account)

    # Criando e adicionando uma transação
    transaction1 = Transaction("Loja X", 200, datetime.now())
    success = account.process_transaction(transaction1)
    print(f"Transação 1 {'aprovada' if success else 'negada'}: {transaction1}")
    print("Estado atualizado da conta:", account)

    # Criando e adicionando uma transação que ultrapassa o limite
    transaction2 = Transaction("Loja Y", 900, datetime.now())
    success = account.process_transaction(transaction2)
    print(f"Transação 2 {'aprovada' if success else 'negada'}: {transaction2}")
    print("Estado final da conta:", account)

if __name__ == "__main__":
    main()
