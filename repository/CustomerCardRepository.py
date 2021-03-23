import json

from domain.CustomerCard import CustomerCard


class CustomerCardRepository:
    def __init__(self, filename):
        self.__filename = filename
        self.__customer_card_storage = {}

    def __load_from_file(self):
        try:
            with open(self.__filename, "r") as f_read:
                saved_cards = json.load(f_read)
                self.__customer_card_storage.clear()
                for saved_card in saved_cards:
                    card = CustomerCard(*saved_card)
                    self.__customer_card_storage[card.get_id_entity()] = card
        except FileNotFoundError:
            self.__customer_card_storage = {}

    def __save_to_file(self):
        to_save = []
        for customer_card in self.__customer_card_storage.values():
            found_card = [customer_card.get_id_entity(),
                          customer_card.get_customer_name(),
                          customer_card.get_customer_first_name(),
                          customer_card.get_customer_cnp(),
                          customer_card.get_birth_date(),
                          customer_card.get_registration_date()]
            to_save.append(found_card)
        with open(self.__filename, "w") as f_write:
            json.dump(to_save, f_write)

    def __ensure_unique_cnp(self,
                            customer_card):
        for card_key in self.__customer_card_storage:
            if self.__customer_card_storage[card_key].get_customer_cnp() == customer_card.get_customer_cnp():
                raise ValueError("CNP {} already exists".format(customer_card.get_customer_cnp()))

    def create(self, customer_card):
        self.__load_from_file()
        if not isinstance(customer_card, CustomerCard):
            raise ValueError("This is not a CustomerCard type")
        key = customer_card.get_id_entity()
        if key in self.__customer_card_storage:
            raise ValueError("Id {} already exists".format(customer_card.get_id_entity()))
        self.__ensure_unique_cnp(customer_card)
        self.__customer_card_storage[key] = customer_card
        self.__save_to_file()

    def read_by_id(self, customer_card_id=None):
        self.__load_from_file()
        if customer_card_id in self.__customer_card_storage:
            return self.__customer_card_storage[customer_card_id]
        return None

    def read_all(self):
        self.__load_from_file()
        return self.__customer_card_storage.values()

    def update(self,
               customer_card):
        self.__load_from_file()
        if not isinstance(customer_card, CustomerCard):
            raise ValueError("This is not a medicine type")
        customer_card_id = customer_card.get_id_entity()
        if customer_card_id not in self.__customer_card_storage:
            raise ValueError("Id {} doesn't exist".format(customer_card.get_id_entity()))
        self.__ensure_unique_cnp(customer_card)
        self.__customer_card_storage[customer_card_id] = customer_card
        self.__save_to_file()

    def delete(self,
               customer_card_id):
        self.__load_from_file()
        if customer_card_id not in self.__customer_card_storage:
            raise ValueError("There's no ID = {}".format(customer_card_id))
        del self.__customer_card_storage[customer_card_id]
        self.__save_to_file()
