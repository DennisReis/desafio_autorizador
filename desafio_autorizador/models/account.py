from dataclasses import dataclass
from typing import List, Optional

from .transaction import Transaction
from .deny_merchants import DenyMerchants


@dataclass
class TransactionResult:
    approved: bool
    reason: Optional[str] = None

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

    def process_transaction(self, transaction: Transaction, deny_merchants: DenyMerchants) -> bool:
        """
        Processes a transaction by debiting the amount from the available limit and adding it to the history.

        Args:
            transaction (Transaction): The transaction to be processed.

        Returns:
            bool: True if the transaction is approved, False otherwise.
        """
        if not self.active:
            return TransactionResult(False, "account-inactive")
        if transaction.amount > self.available_limit:
            return TransactionResult(False, "insufficient-limit")
        if deny_merchants.is_merchant_denied(transaction.merchant):
            return TransactionResult(False, "merchant-denied")

        self.available_limit -= transaction.amount
        self.history.append(transaction)
        return TransactionResult(True)

    def activate(self) -> None:
        """Activates the account, enabling new transactions."""
        self.active = True

    def deactivate(self) -> None:
        """Deactivates the account, preventing new transactions."""
        self.active = False

    def get_highest_transaction(self) -> Optional[Transaction]:
        """
        Returns the transaction with the highest amount in the account's history.

        Returns:
            Transaction | None: The transaction with the highest amount, or None if there are no transactions.
        """
        if not self.history:
            return None
        return max(self.history, key=lambda t: t.amount)

    def get_lowest_transaction(self) -> Optional[Transaction]:
        """
        Returns the transaction with the lowest amount in the account's history.

        Returns:
            Transaction | None: The transaction with the lowest amount, or None if there are no transactions.
        """
        if not self.history:
            return None
        return min(self.history, key=lambda t: t.amount)

    def get_latest_transaction(self) -> Optional[Transaction]:
        """
        Returns the most recent transaction based on the transaction timestamp.

        Returns:
            Optional[Transaction]: The most recent transaction, or None if no transactions exist.
        """
        if not self.history:
            return None
        return max(self.history, key=lambda t: t.time)

    def get_oldest_transaction(self) -> Optional[Transaction]:
        """
        Returns the oldest transaction based on the transaction timestamp.

        Returns:
            Optional[Transaction]: The oldest transaction, or None if no transactions exist.
        """
        if not self.history:
            return None
        return min(self.history, key=lambda t: t.time)

    def __repr__(self):
        """Returns a string representation of the account.

        Returns:
            str: Textual representation of the account.
        """
        return f"Account(active={self.active}, available_limit={self.available_limit}, history={self.history})"

    def __str__(self) -> str:
        """Returns a string representation of the account.

        Returns:
            str: Textual representation of the account.
        """
        return (
            f"Account(active={self.active}, available_limit={self.available_limit}, "
            f"transactions={len(self.history)} total)"
        )
