import unittest

from domain.CustomerCard import CustomerCard


class CustomerCardTest(unittest.TestCase):
    def test_equal(self):
        card_one = CustomerCard(1, 'Cornea', 'Ciprian', 5010628055083, '28/06/2001', '27/09/2019', False)
        card_two = CustomerCard(1, 'Cornea', 'Ciprian', 5010628055083, '28/06/2001', '27/09/2019', False)
        self.assertEqual(card_one, card_two)

    def test_not_equal(self):
        card_one = CustomerCard(1, 'Cornea', 'Ciprian', 5010628055083, '28/06/2001', '27/09/2019', False)
        card_two = CustomerCard(1, 'Cornea', 'Ciprian', 5010628055082, '28/06/2001', '27/09/2019', False)
        self.assertNotEqual(card_one, card_two)

    def test_getter(self):
        card_one = CustomerCard(1, 'Cornea', 'Ciprian', 5010628055083, '28/06/2001', '27/09/2019', False)
        self.assertEqual(card_one.get_id_entity(), 1)
        self.assertEqual(card_one.get_customer_name(), 'Cornea')
        self.assertEqual(card_one.get_customer_first_name(), 'Ciprian')
        self.assertEqual(card_one.get_customer_cnp(), 5010628055083)
        self.assertEqual(card_one.get_birth_date(), '28/06/2001')
        self.assertEqual(card_one.get_registration_date(), '27/09/2019')
        self.assertEqual(card_one.get_isRemoved(), False)

    def test_setter(self):
        card_one = CustomerCard(1, 'Cornea', 'Ciprian', 5010628055083, '28/06/2001', '27/09/2019', False)
        card_two = CustomerCard(1, 'John', 'Smith', 5010628055082, '28/06/2002', '27/09/2018', True)
        card_two.set_customer_name('Cornea')
        card_two.set_customer_first_name('Ciprian')
        card_two.set_customer_cnp(5010628055083)
        card_two.set_birth_date('28/06/2001')
        card_two.set_registration_date('27/09/2019')
        card_two.set_isRemoved(False)
        self.assertEqual(card_one, card_two)

    def test_get_text_in_format(self):
        card_one = CustomerCard(1, 'Cornea', 'Ciprian', 5010628055083, '28/06/2001', '27/09/2019', False)
        cardString = card_one.get_text_format()
        self.assertEqual(cardString, '1,Cornea,Ciprian,5010628055083,28/06/2001,27/09/2019,False')
