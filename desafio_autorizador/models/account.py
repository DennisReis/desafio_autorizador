from typing import List

from .transaction import Transaction


class Account:
    """
    Represents a bank account.

    Attributes:
        active (bool): Indicates whether the account is active.
        available_limit (int): Credit limit available on the account.
        history (List[Transaction]): History of transactions performed on the account.
    """

    def __init__(self, active: bool, available_limit: int):
        """
        Initialize an Account instance.

        Args:
            active (bool): Account initial state(ativa ou inativa).
            available_limit (int): Initial available account limit .
        """
        self.active = active
        self.available_limit = available_limit
        self.history: List[Transaction] = []

    def process_transaction(self, transaction: Transaction) -> bool:
        """
        Processes a transaction by debiting the amount from the available limit and adding it to the history.

        Args:
            transaction (Transaction): The transaction to be processed.

        Returns:
            bool: True if the transaction is approved, False otherwise.
        """
        if self.active and transaction.amount <= self.available_limit:
            self.available_limit -= transaction.amount
            self.history.append(transaction)
            return True
        return False

    def activate(self) -> None:
        """Activates the account, enabling new transactions."""
        self.active = True

    def deactivate(self) -> None:
        """Deactivates the account, preventing new transactions."""
        self.active = False

    def __repr__(self):
        """Returns a string representation of the account.

        Returns:
            str: Textual representation of the account.
        """
        return f"Account(active={self.active}, available_limit={self.available_limit}, history={self.history})"
