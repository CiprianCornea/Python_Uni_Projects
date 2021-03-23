import unittest

from domain.Transaction import Transaction


class TransactionTest(unittest.TestCase):
    def test_equal(self):
        transaction_one = Transaction(1, 1, 1, 1000.0, 250.0, '01/01/2001', 60, 0.0)
        transaction_two = Transaction(1, 1, 1, 1000.0, 250.0, '01/01/2001', 60, 0.0)
        self.assertEqual(transaction_one, transaction_two)

    def test_not_equal(self):
        transaction_one = Transaction(1, 1, 1, 1000.0, 250.0, '01/01/2001', 60, 0.0)
        transaction_two = Transaction(1, 2, 1, 1000.0, 250.0, '01/01/2001', 60, 0.0)
        self.assertNotEqual(transaction_one, transaction_two)

    def test_getter(self):
        transaction_one = Transaction(1, 1, 1, 1000.0, 250.0, '01/01/2001', 60, 0.0)
        self.assertEqual(transaction_one.get_id_entity(), 1)
        self.assertEqual(transaction_one.get_carID(), 1)
        self.assertEqual(transaction_one.get_cardID(), 1)
        self.assertEqual(transaction_one.get_pieces_cost(), 1000.0)
        self.assertEqual(transaction_one.get_workmanship_cost(), 250.0)
        self.assertEqual(transaction_one.get_date(), '01/01/2001')
        self.assertEqual(transaction_one.get_hour(), 60)
        self.assertEqual(transaction_one.get_discount(), 0.0)

    def test_setter(self):
        transaction_one = Transaction(1, 1, 1, 1000.0, 250.0, '01/01/2001', 60, 0.0)
        transaction_two = Transaction(1, 2, 3, 1001.0, 251.0, '01/02/2001', 61, 0.1)
        transaction_two.set_carId(1)
        transaction_two.set_cardId(1)
        transaction_two.set_pieces_cost(1000.0)
        transaction_two.set_workmanshipCost(250.0)
        transaction_two.set_date('01/01/2001')
        transaction_two.set_hour(60)
        transaction_two.set_discount(0.0)
        self.assertEqual(transaction_one, transaction_two)

    def test_get_text_format(self):
        transaction_one = Transaction(1, 1, 1, 1000.0, 250.0, '01/01/2001', 60, 0.0)
        transactionString = transaction_one.get_text_in_format()
        self.assertEqual(transactionString, '1,1,1,1000.0,250.0,01/01/2001,60,0.0')
