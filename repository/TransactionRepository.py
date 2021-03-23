import json

from domain.Transaction import Transaction


class TransactionRepository:
    def __init__(self, filename):
        self.__filename = filename
        self.__transaction_storage = {}

    def __load_from_file(self):
        try:
            with open(self.__filename, "r") as f_read:
                saved_transactions = json.load(f_read)
                self.__transaction_storage.clear()
                for saved_transaction in saved_transactions:
                    transaction = Transaction(*saved_transaction)
                    self.__transaction_storage[transaction.get_id_entity()] = transaction
        except FileNotFoundError:
            self.__transaction_storage = {}

    def __save_to_file(self):
        to_save = []
        for transaction in self.__transaction_storage.values():
            found_transaction = [transaction.get_id_entity(),
                                 transaction.get_medicine_transacted_id(),
                                 transaction.get_customer_card_transaction_id(),
                                 transaction.get_pieces_cost(),
                                 transaction.get_workmanship_cost(),
                                 transaction.get_date(),
                                 transaction.get_time()]
            to_save.append(found_transaction)
        with open(self.__filename, "w") as f_write:
            json.dump(to_save, f_write)

    def create(self, transaction):
        self.__load_from_file()
        if not isinstance(transaction,
                          Transaction):
            raise ValueError("Is not a transaction type")
        key = transaction.get_id_entity()
        if key in self.__transaction_storage:
            raise ValueError("Id = {} already exists".format(key))
        self.__transaction_storage[key] = transaction
        self.__save_to_file()

    def read_by_id(self, transaction_id: int):
        self.__load_from_file()
        if transaction_id in self.__transaction_storage:
            return self.__transaction_storage[transaction_id]
        return None

    def read_all(self):
        self.__load_from_file()
        return self.__transaction_storage.values()

    def update(self, transaction):
        self.__load_from_file()
        if not isinstance(transaction, Transaction):
            raise ValueError("This is not a medicine type")
        transaction_id = transaction.get_id_entity()
        if transaction_id not in self.__transaction_storage:
            raise KeyError("Id {} doesn't exist".format(transaction.get_id_entity()))
        self.__transaction_storage[transaction_id] = transaction
        self.__save_to_file()

    def delete(self, transaction_id):
        self.__load_from_file()
        if transaction_id not in self.__transaction_storage:
            raise KeyError("There's no ID = {}".format(transaction_id))
        del self.__transaction_storage[transaction_id]
        self.__save_to_file()
