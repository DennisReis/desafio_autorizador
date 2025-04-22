class DenyMerchants:
    """
    Represents a financial transaction.

    Attributes:
        merchant (str): Merchant's name where the transaction ocurred.
        amount (int): Transaction amount in monetary units.
        time (datetime): Date and time when the transaction occurred.
    """

    def __init__(self):
        """
        Initializes a Transaction instance.

        Args:
            merchant (str): Merchant name.
            amount (int): Transaction amount.
            time (datetime): Date and time of the transaction.
        """
        self.merchants = set()


    def add_merchant(self, merchant: str) -> None:
        """
        Adds a merchant to the list of denied merchants.

        Args:
            merchant (str): Merchant name to be added.
        """
        self.merchants.add(merchant)

    def remove_merchant(self, merchant: str) -> None:
        """
        Removes a merchant from the list of denied merchants.

        Args:
            merchant (str): Merchant name to be removed.
        """
        self.merchants.remove(merchant)

    def is_merchant_denied(self, merchant: str) -> bool:
        """
        Checks if a merchant is in the list of denied merchants.

        Args:
            merchant (str): Merchant name to be checked.

        Returns:
            bool: True if the merchant is denied, False otherwise.
        """
        return merchant in self.merchants

    def __repr__(self):
        """
        Returns a string representation of the transaction.

        Returns:
            str: Textual representation of the transaction.
        """
        return f"Transaction(merchants='{self.merchants}')"

    def __str__(self) -> str:
        """
        Returns a string representation of the transaction.

        Returns:
            str: Textual representation of the transaction.
        """
        return f"Transaction(merchants='{self.merchants}')"
