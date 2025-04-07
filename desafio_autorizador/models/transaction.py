from datetime import datetime


class Transaction:
    """
    Representa uma transação financeira.

    Attributes:
        merchant (str): Nome do comerciante onde a transação foi realizada.
        amount (int): Valor da transação em unidades monetárias.
        time (datetime): Data e hora em que a transação ocorreu.
    """

    def __init__(self, merchant: str, amount: int, time: datetime):
        """
        Inicializa uma instância de Transaction.

        Args:
            merchant (str): Nome do comerciante.
            amount (int): Valor da transação.
            time (datetime): Data e hora da transação.
        """
        self.merchant = merchant
        self.amount = amount
        self.time = time

    def __repr__(self):
        """
        Retorna uma representação em string da transação.

        Returns:
            str: Representação textual da transação.
        """
        return f"Transaction(merchant='{self.merchant}', amount={self.amount}, time={self.time})"
