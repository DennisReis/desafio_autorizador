import unittest
from datetime import datetime

from desafio_autorizador.main import Account, Transaction


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(active=True, available_limit=100)

    def test_account_creation(self):
        self.assertTrue(self.account.active)
        self.assertEqual(self.account.available_limit, 100)
        self.assertEqual(len(self.account.history), 0)

    def test_successful_transaction(self):
        tx = Transaction("Loja A", 30, datetime.now())
        success = self.account.process_transaction(tx)
        self.assertTrue(success)
        self.assertEqual(self.account.available_limit, 70)
        self.assertEqual(len(self.account.history), 1)

    def test_transaction_insufficient_funds(self):
        tx = Transaction("Loja B", 150, datetime.now())
        success = self.account.process_transaction(tx)
        self.assertFalse(success)
        self.assertEqual(self.account.available_limit, 100)
        self.assertEqual(len(self.account.history), 0)

    def test_transaction_account_inactive(self):
        self.account.active = False
        tx = Transaction("Loja C", 20, datetime.now())
        success = self.account.process_transaction(tx)
        self.assertFalse(success)
        self.assertEqual(self.account.available_limit, 100)
        self.assertEqual(len(self.account.history), 0)


if __name__ == "__main__":
    unittest.main()
