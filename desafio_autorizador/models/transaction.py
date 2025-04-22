from datetime import datetime


class Transaction:
    """
    Represents a financial transaction.

    Attributes:
        merchant (str): Merchant's name where the transaction ocurred.
        amount (int): Transaction amount in monetary units.
        time (datetime): Date and time when the transaction occurred.
    """

    def __init__(self, merchant: str, amount: int, time: datetime):
        """
        Initializes a Transaction instance.

        Args:
            merchant (str): Merchant name.
            amount (int): Transaction amount.
            time (datetime): Date and time of the transaction.
        """
        self.merchant = merchant
        self.amount = amount
        self.time = time

    def __repr__(self):
        """
        Returns a string representation of the transaction.

        Returns:
            str: Textual representation of the transaction.
        """
        return f"Transaction(merchant='{self.merchant}', amount={self.amount}, time={self.time})"

    def __str__(self) -> str:
        """
        Returns a string representation of the transaction.

        Returns:
            str: Textual representation of the transaction.
        """
        return f"Transaction(merchant='{self.merchant}', amount={self.amount}, time={self.time.isoformat()})"
