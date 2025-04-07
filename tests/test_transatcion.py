import unittest
from desafio_autorizador.main import Transaction
from datetime import datetime

class TestTransaction(unittest.TestCase):
    def test_create_transaction(self):
        time_now = datetime.now()
        transaction = Transaction("Loja Z", 150, time_now)
        self.assertEqual(transaction.merchant, "Loja Z")
        self.assertEqual(transaction.amount, 150)
        self.assertEqual(transaction.time, time_now)

if __name__ == "__main__":
    unittest.main()
