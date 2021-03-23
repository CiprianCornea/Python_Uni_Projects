import unittest

from domain.CarValidator import CarValidator
from domain.TransactionValidator import TransactionValidator
from repository.GenericRepository import GenericRepository
from service.CarService import CarService
from service.TransactionService import TransactionService


class TransactionServiceTest(unittest.TestCase):
    def test_add_transaction(self):
        car_repository = GenericRepository('test.pickle')
        customer_card_repository = GenericRepository('test.pickle')
        transaction_repository = GenericRepository('test.pickle')
        transaction_validator = TransactionValidator()
        car_validator = CarValidator()
        car_service = CarService(car_repository, car_validator, transaction_repository)
        transaction_service = TransactionService(transaction_repository, transaction_validator, customer_card_repository,
                                                 car_repository)

        car_service.add_car(2, 'logan', 2005, 20000, 'yes', False)
        transaction_service.add_transaction(1, 2, 3, 100.0, 25.0, '12/09/2009', 65.0, 0.0)
        car_repository.delete(2)
        self.assertEqual(len(transaction_service.get_all_transactions()), 1)
        transaction_repository.delete(1)

    def test_update_transaction(self):
        car_repository = GenericRepository('test.pickle')
        customer_card_repository = GenericRepository('test.pickle')
        transaction_repository = GenericRepository('test.pickle')
        transaction_validator = TransactionValidator()
        car_validator = CarValidator()
        car_service = CarService(car_repository, car_validator, transaction_repository)
        transaction_service = TransactionService(transaction_repository, transaction_validator,
                                                 customer_card_repository,
                                                 car_repository)
        car_service.add_car(2, 'logan', 2005, 20000, 'yes', False)
        transaction_service.add_transaction(1, 2, 3, 100.0, 25.0, '12/09/2009', 65.0, 0.0)
        transaction_service.update_transaction(1, 2, 4, 100.0, 25.0, '12/09/2009', 65.0, 0.0)
        car_repository.delete(2)
        transaction = transaction_repository.read_by_id(1)
        self.assertEqual(transaction.get_cardID(), 4)
        transaction_repository.delete(1)

    def test_delete_transaction(self):
        car_repository = GenericRepository('test.pickle')
        customer_card_repository = GenericRepository('test.pickle')
        transaction_repository = GenericRepository('test.pickle')
        transaction_validator = TransactionValidator()
        car_validator = CarValidator()
        car_service = CarService(car_repository, car_validator, transaction_repository)
        transaction_service = TransactionService(transaction_repository, transaction_validator,
                                                 customer_card_repository,
                                                 car_repository)

        car_service.add_car(2, 'logan', 2005, 20000, 'yes', False)
        transaction_service.add_transaction(1, 2, 3, 100.0, 25.0, '12/09/2009', 65.0, 0.0)
        car_repository.delete(2)
        transaction_repository.delete(1)
        self.assertEqual(len(transaction_service.get_all_transactions()), 0)

    def test_get_transaction_between_two_dates(self):
        car_repository = GenericRepository('test.pickle')
        customer_card_repository = GenericRepository('test.pickle')
        transaction_repository = GenericRepository('test.pickle')
        transaction_validator = TransactionValidator()
        car_validator = CarValidator()
        car_service = CarService(car_repository, car_validator, transaction_repository)
        transaction_service = TransactionService(transaction_repository, transaction_validator,
                                                 customer_card_repository,
                                                 car_repository)
        car_service.add_car(2, 'logan', 2005, 20000, 'yes', False)
        car_service.add_car(3, 'logan', 2005, 20000, 'yes', False)
        car_service.add_car(4, 'logan', 2005, 20000, 'yes', False)
        transaction_service.add_transaction(10, 2, 3, 100.0, 25.0, '12/09/2009', 65.0, 0.0)
        transaction_service.add_transaction(30, 3, 3, 100.0, 25.0, '13/09/2009', 65.0, 0.0)
        transaction_service.add_transaction(40, 4, 3, 100.0, 25.0, '14/09/2009', 65.0, 0.0)
        car_repository.delete(2)
        car_repository.delete(3)
        car_repository.delete(4)
        list_of_transaction = transaction_service.get_transactions_between_two_dates('11/09/2009', '14/09/2009')
        self.assertEqual(len(list_of_transaction), 2)
        transaction_repository.delete(10)
        transaction_repository.delete(30)
        transaction_repository.delete(40)
