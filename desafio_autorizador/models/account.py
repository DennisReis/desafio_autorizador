from typing import List

from .transaction import Transaction


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
