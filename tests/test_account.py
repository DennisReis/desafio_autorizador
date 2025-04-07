import unittest
from datetime import datetime

from desafio_autorizador.models.account import Account
from desafio_autorizador.models.transaction import Transaction


class TestAccount(unittest.TestCase):
    """
    Test suite for the Account class.
    """

    def setUp(self):
        """
        Sets up a default account instance for testing.
        """
        self.account = Account(active=True, available_limit=1000)

    def test_process_transaction_sufficient_limit(self):
        """
        Test that a transaction is approved when the available limit is sufficient.
        """
        transaction = Transaction(merchant="Loja A", amount=200, time=datetime.now())
        result = self.account.process_transaction(transaction)
        self.assertTrue(result)
        self.assertEqual(self.account.available_limit, 800)

    def test_process_transaction_insufficient_limit(self):
        """
        Test that a transaction is declined when the available limit is insufficient.
        """
        transaction = Transaction(merchant="Loja B", amount=1200, time=datetime.now())
        result = self.account.process_transaction(transaction)
        self.assertFalse(result)
        self.assertEqual(self.account.available_limit, 1000)

    def test_process_transaction_inactive_account(self):
        """
        Test that a transaction is declined when the account is inactive.
        """
        self.account.active = False
        transaction = Transaction(merchant="Loja C", amount=100, time=datetime.now())
        result = self.account.process_transaction(transaction)
        self.assertFalse(result)
        self.assertEqual(self.account.available_limit, 1000)

    def test_deactivate_account(self):
        """
        Test that the account can be deactivated.
        """
        self.account.deactivate()
        self.assertFalse(self.account.active)

    def test_str_representation(self):
        """
        Test the string representation of the account.
        """
        expected_str = "Account(active=True, available_limit=1000, history=[])"
        self.assertEqual(str(self.account), expected_str)


if __name__ == "__main__":
    unittest.main()
