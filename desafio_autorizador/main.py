from datetime import datetime
from typing import List


class Transaction:
    """
    Representa uma transação financeira.

    Attributes:
        merchant (str): Nome do comerciante onde a transação foi realizada.
        amount (int): Valor da transação em unidades monetárias.
        time (datetime): Data e hora em que a transação ocorreu.
    """

    def __init__(self, merchant: str, amount: int, time: datetime):
        """
        Inicializa uma instância de Transaction.

        Args:
            merchant (str): Nome do comerciante.
            amount (int): Valor da transação.
            time (datetime): Data e hora da transação.
        """
        self.merchant = merchant
        self.amount = amount
        self.time = time

    def __repr__(self):
        """
        Retorna uma representação em string da transação.

        Returns:
            str: Representação textual da transação.
        """
        return f"Transaction(merchant='{self.merchant}', amount={self.amount}, time={self.time})"


class Account:
    """
    Representa uma conta bancária.

    Attributes:
        active (bool): Indica se a conta está ativa.
        available_limit (int): Limite de crédito disponível na conta.
        history (List[Transaction]): Histórico de transações realizadas na conta.
    """

    def __init__(self, active: bool, available_limit: int):
        """
        Inicializa uma instância de Account.

        Args:
            active (bool): Estado inicial da conta (ativa ou inativa).
            available_limit (int): Limite de crédito inicial disponível.
        """
        self.active = active
        self.available_limit = available_limit
        self.history: List[Transaction] = []

    def process_transaction(self, transaction: Transaction) -> bool:
        """
        Processa uma transação, debitando o valor do limite disponível e adicionando ao histórico.

        Args:
            transaction (Transaction): A transação a ser processada.

        Returns:
            bool: True se a transação for aprovada, False caso contrário.
        """
        if self.active and transaction.amount <= self.available_limit:
            self.available_limit -= transaction.amount
            self.history.append(transaction)
            return True
        return False

    def deactivate(self) -> None:
        """Inativa a conta, impedindo novas transações."""
        self.active = False

    def __repr__(self):
        """
        Retorna uma representação em string da conta.

        Returns:
            str: Representação textual da conta.
        """
        return f"Account(active={self.active}, available_limit={self.available_limit}, history={self.history})"


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
