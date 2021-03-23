import unittest

from domain.CustomerCardValidator import CustomerCardValidator
from repository.GenericRepository import GenericRepository
from service.CustomerCardService import CustomerCardService


class CustomerCardServiceTest(unittest.TestCase):
    def test_add_customer_card(self):
        customer_card_validator = CustomerCardValidator()
        customer_card_repository = GenericRepository('test.pickle')
        # car_repository = GenericRepository('test.pickle')
        transaction_repository = GenericRepository('test.pickle')
        customer_card_service = CustomerCardService(customer_card_repository,
                                                    customer_card_validator,
                                                    transaction_repository
                                                    )
        customer_card_service.add_customer_card(1, 'Cornea', 'Ciprian', 5010628055083, '28/06/2001', '27/09/2019',
                                                False)
        self.assertEqual(len(customer_card_service.getAll()), 1)
        customer_card_repository.delete(1)

    def test_update_customer_card(self):
        customer_card_validator = CustomerCardValidator()
        customer_card_repository = GenericRepository('test.pickle')
        # car_repository = GenericRepository('test.pickle')
        transaction_repository = GenericRepository('test.pickle')
        customer_card_service = CustomerCardService(customer_card_repository,
                                                    customer_card_validator,
                                                    transaction_repository
                                                    )
        customer_card_service.add_customer_card(1, 'Cornea', 'Ciprian', 5010628055083, '28/06/2001', '27/09/2019',
                                                False)
        customer_card_service.updateCard(1, 'Cornea', 'Andrei', 5010628055083, '28/06/2001', '27/09/2019',
                                         False)
        card = customer_card_repository.read_by_id(1)
        self.assertEqual(card.get_customer_first_name(), 'Andrei')
        customer_card_repository.delete(1)

    def test_delete_customer_card(self):
        customer_card_validator = CustomerCardValidator()
        customer_card_repository = GenericRepository('test.pickle')
        # car_repository = GenericRepository('test.pickle')
        transaction_repository = GenericRepository('test.pickle')
        customer_card_service = CustomerCardService(customer_card_repository,
                                                    customer_card_validator,
                                                    transaction_repository
                                                    )
        customer_card_service.add_customer_card(1, 'Cornea', 'Ciprian', 5010628055083, '28/06/2001', '27/09/2019',
                                                False)
        customer_card_repository.delete(1)
        self.assertEqual(len(customer_card_service.getAll()), 0)

    def test_get_list_of_customer_cards_that_match(self):
        customer_card_validator = CustomerCardValidator()
        customer_card_repository = GenericRepository('test.pickle')
        # car_repository = GenericRepository('test.pickle')
        transaction_repository = GenericRepository('test.pickle')
        customer_card_service = CustomerCardService(customer_card_repository,
                                                    customer_card_validator,
                                                    transaction_repository
                                                    )
        customer_card_service.add_customer_card(1, 'Cornea', 'Ciprian', 5010628055083, '28/06/2001', '27/09/2019',
                                                False)
        customer_card_service.add_customer_card(2, 'Delia', 'Ciprian', 5010628055084, '28/06/2001', '27/09/2019',
                                                False)
        customer_card_service.add_customer_card(3, 'Delia', 'Ciprian', 5010628055085, '28/06/2001', '27/09/2019',
                                                False)
        list_of_cards = customer_card_service.get_list_of_customer_cards_that_match('Delia')
        self.assertEqual(len(list_of_cards), 2)
        customer_card_repository.delete(1)
        customer_card_repository.delete(2)
        customer_card_repository.delete(3)

    def test_showCardClientDescOrd(self):
        customer_card_validator = CustomerCardValidator()
        customer_card_repository = GenericRepository('test.pickle')
        # car_repository = GenericRepository('test.pickle')
        transaction_repository = GenericRepository('test.pickle')
        customer_card_service = CustomerCardService(customer_card_repository,
                                                    customer_card_validator,
                                                    transaction_repository
                                                    )
        customer_card_service.add_customer_card(1, 'Cornea', 'Ciprian', 5010628055083, '28/06/2001', '27/09/2019',
                                                False)
        customer_card_service.add_customer_card(2, 'Delia', 'Ciprian', 5010628055084, '28/06/2001', '27/09/2019',
                                                False)
        customer_card_service.add_customer_card(3, 'Delia', 'Ciprian', 5010628055085, '28/06/2001', '27/09/2019',
                                                False)
        storage = customer_card_service.getAll()
        self.assertEqual(len(storage), 3)
        customer_card_repository.delete(1)
        customer_card_repository.delete(2)
        customer_card_repository.delete(3)
