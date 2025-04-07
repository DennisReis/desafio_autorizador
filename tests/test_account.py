import unittest
from datetime import datetime, timedelta

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

    def test_activate_account(self):
        """
        Test that the account can be activated.
        """
        self.account.deactivate()
        self.account.activate()
        self.assertTrue(self.account.active)

    def test_str_representation(self):
        """
        Test the string representation of the account.
        """
        expected_str = "Account(active=True, available_limit=1000, history=[])"
        self.assertEqual(str(self.account), expected_str)

    def test_get_highest_transaction(self):
        """
        Test that the method returns the transaction with the highest amount.
        """
        account = Account(active=True, available_limit=1000)

        t1 = Transaction(merchant="Loja A", amount=100, time=datetime.now())
        t2 = Transaction(merchant="Loja B", amount=300, time=datetime.now())
        t3 = Transaction(merchant="Loja C", amount=200, time=datetime.now())

        account.process_transaction(t1)
        account.process_transaction(t2)
        account.process_transaction(t3)

        highest = account.get_highest_transaction()

        assert highest is not None
        assert highest.amount == 300
        assert highest.merchant == "Loja B"

    def test_get_lowest_transaction(self):
        """
        Test that the method returns the transaction with the lowest amount.
        """
        account = Account(active=True, available_limit=1000)

        t1 = Transaction(merchant="Loja A", amount=100, time=datetime.now())
        t2 = Transaction(merchant="Loja B", amount=300, time=datetime.now())
        t3 = Transaction(merchant="Loja C", amount=200, time=datetime.now())

        account.process_transaction(t1)
        account.process_transaction(t2)
        account.process_transaction(t3)

        highest = account.get_lowest_transaction()

        assert highest is not None
        assert highest.amount == 100
        assert highest.merchant == "Loja A"

    def test_get_latest_transaction(self):
        """
        Test that the method returns the oldest transaction based on the transaction timestamp.
        """
        account = Account(active=True, available_limit=1000)

        t1 = Transaction(
            merchant="Loja A", amount=100, time=datetime.now() - timedelta(days=2)
        )
        t2 = Transaction(
            merchant="Loja B", amount=300, time=datetime.now() - timedelta(days=1)
        )
        t3 = Transaction(merchant="Loja C", amount=200, time=datetime.now())

        account.process_transaction(t1)
        account.process_transaction(t2)
        account.process_transaction(t3)

        latest = account.get_latest_transaction()

        assert latest is not None
        self.assertEqual(latest.time, t3.time)

    def test_get_oldest_transaction(self):
        """
        Test that the method returns the oldes transaction based on the transaction timestamp.
        """
        account = Account(active=True, available_limit=1000)

        t1 = Transaction(
            merchant="Loja A", amount=100, time=datetime.now() - timedelta(days=2)
        )
        t2 = Transaction(
            merchant="Loja B", amount=300, time=datetime.now() - timedelta(days=1)
        )
        t3 = Transaction(merchant="Loja C", amount=200, time=datetime.now())

        account.process_transaction(t1)
        account.process_transaction(t2)
        account.process_transaction(t3)

        oldest = account.get_oldest_transaction()

        assert oldest is not None
        self.assertEqual(oldest.time, t1.time)


if __name__ == "__main__":
    unittest.main()
