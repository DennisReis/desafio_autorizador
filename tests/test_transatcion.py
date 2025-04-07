import unittest
from datetime import datetime

from desafio_autorizador.models.transaction import Transaction


class TestTransaction(unittest.TestCase):
    """
    Test suite for the Transaction class.
    """

    def test_transaction_initialization(self):
        """
        Test that a transaction is correctly initialized with given attributes.
        """
        transaction = Transaction(
            merchant="Loja A", amount=150, time=datetime(2025, 4, 7, 10, 0, 0)
        )
        self.assertEqual(transaction.merchant, "Loja A")
        self.assertEqual(transaction.amount, 150)
        self.assertEqual(transaction.time, datetime(2025, 4, 7, 10, 0, 0))

    def test_str_representation(self):
        """
        Test the string representation of the transaction.
        """
        transaction = Transaction(
            merchant="Loja B", amount=200, time=datetime(2025, 4, 7, 11, 0, 0)
        )
        expected_str = (
            "Transaction(merchant='Loja B', amount=200, time=2025-04-07 11:00:00)"
        )
        self.assertEqual(str(transaction), expected_str)


if __name__ == "__main__":
    unittest.main()
