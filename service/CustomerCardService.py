# import random
# import string
from domain.CustomerCard import CustomerCard
from domain.CustomerCardValidator import CustomerCardValidator
from repository.GenericRepository import GenericRepository


class CustomerCardService:
    """
    The class for CustomerCard service
    """
    def __init__(self,
                 customer_card_repository: GenericRepository,
                 customer_card_validator: CustomerCardValidator,
                 transaction_repository: GenericRepository
                 ):
        """
        Initialization the customer card service
        :param customer_card_repository: customer card repository
        :param customer_card_validator: customer card validator
        :param transaction_repository: transaction repository
        """
        self.__customer_card_repository = customer_card_repository
        self.__customer_card_validator = customer_card_validator
        self.__transaction_repository = transaction_repository

    # CREATE

    def add_customer_card(self,
                          customer_card_id,
                          customer_name,
                          customer_first_name,
                          customer_cnp,
                          birth_date,
                          registration_date,
                          isRemoved):
        """
        Function creates a card
        :param customer_card_id: int
        :param customer_name: string
        :param customer_first_name: string
        :param customer_cnp: int
        :param birth_date: string
        :param registration_date: string
        :param isRemoved: bool
        """
        customer_card = CustomerCard(customer_card_id,
                                     customer_name,
                                     customer_first_name,
                                     customer_cnp,
                                     birth_date,
                                     registration_date,
                                     isRemoved)
        self.__customer_card_validator.validate_date(birth_date)
        self.__customer_card_validator.validate_date(registration_date)
        self.__customer_card_repository.ensure_unique_cnp(customer_card)
        self.__customer_card_validator.validate_customer_card(customer_card)
        self.__customer_card_repository.create(customer_card)

    # READ

    def getAll(self):
        """
        The functionality for getting all the object from file
        :return: all the object from file
        """
        return self.__customer_card_repository.read_all()

    # UPDATE

    def updateCard(self, ID, name, surname, CNP, dateBirth, dateRegistration, isRemoved):
        """
        Update an customer card object
        :param ID: int
        :param name: string
        :param surname: string
        :param CNP: int
        :param dateBirth: string
        :param dateRegistration: string
        :param isRemoved: bool
        :return: -
        """
        newCard = CustomerCard(ID, name, surname, CNP, dateBirth, dateRegistration, isRemoved)
        self.__customer_card_validator.validate_customer_card(newCard)
        self.__customer_card_repository.update(newCard)

    # DELETE

    def deleteCard(self, idCard):
        """
        Delete a card by a given id
        :param idCard: int
        :return: -
        """
        self.__customer_card_repository.delete(idCard)

    def get_list_of_customer_cards_that_match(self, stringC):
        """
        Function finds all the cards that have the given string in them
        :param stringC: string
        :return: a list of CustomerCards objects that contain the string
        """
        found_customer_cards = []
        for customer_card in self.__customer_card_repository.read_all():
            if stringC in customer_card.get_text_format():
                found_customer_cards.append(customer_card)
        return found_customer_cards

    def get_all_cards(self):
        """
        Gets all cards from repository
        :return: a list of CustomerCard objects
        """
        found_cards = []
        for card in self.__customer_card_repository.read_all():
            found_cards.append(card)
        return found_cards

    def search_text(self, string_cards):
        """
        Function finds all the cards that have the given string in them
        :param string_cards: string
        :return: a list of CustomerCards objects that contain the string
        """
        listC = []
        for cards in self.__customer_card_repository.read_all():
            if string_cards in cards.get_text_format():
                listC.append(cards)

        return listC

    def clear(self):
        """
        Clear the repository for card
        :return:
        """
        self.__customer_card_repository.clear()

    def showCardClientDescOrd(self):
        """
        Ordered customer cards in descending order by the value of the discounts obtained
        :return: sorted list
        """
        list_of_customer_cards = self.__customer_card_repository.read_all()
        max_per_id = {}
        for transaction in self.__transaction_repository.read_all():
            card_id_in_transaction = transaction.get_cardID()
            discount_for_card = transaction.get_discount()
            if card_id_in_transaction not in max_per_id:
                max_per_id[card_id_in_transaction] = 0
            max_per_id[card_id_in_transaction] += discount_for_card
        list_of_filtered_cards = []
        for cardD in list_of_customer_cards:
            if cardD.get_id_entity() in max_per_id:
                list_of_filtered_cards.append(cardD)
        return sorted(list_of_filtered_cards, key=lambda card: max_per_id[card.get_id_entity()], reverse=True)
