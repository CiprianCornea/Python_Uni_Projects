import datetime

from domain.Transaction import Transaction
from domain.TransactionValidator import TransactionValidator
from repository.GenericRepository import GenericRepository
from exception.InvalidIdException import InvalidIdException


class TransactionServiceLab11:
    """
    The class for transaction service
    """
    def __init__(self,
                 transaction_repository: GenericRepository,
                 transaction_validator: TransactionValidator,
                 customer_card_repository: GenericRepository,
                 car_repository: GenericRepository):
        """
        Initialization for transaction service
        :param transaction_repository: transaction repository
        :param transaction_validator: transaction validator
        :param customer_card_repository: customer card repository
        :param car_repository: car repository
        """
        self.__transaction_repository = transaction_repository
        self.__transaction_validator = transaction_validator
        self.__customer_card_repository = customer_card_repository
        self.__car_repository = car_repository

    def get_cars_id(self):
        """
        Get id for all cars
        :return: list of id
        """
        found_id = []
        for car in self.__car_repository.read_all():
            found_id.append(car.get_id_entity())
        return found_id

    def add_transaction(self,
                        transactionID,
                        carID,
                        cardID,
                        piecesCost,
                        sumMan,
                        date,
                        hour,
                        reducedSum
                        ):
        """
        Add an transaction object
        :param transactionID: int
        :param carID: int
        :param cardID: int
        :param piecesCost: float
        :param sumMan: float
        :param date: string
        :param hour: float
        :param reducedSum: float
        :return: -
        """
        if carID not in self.get_cars_id():
            raise InvalidIdException("There is no such car with that id")
        for card in self.__customer_card_repository.read_all():
            if card.get_id_entity() == cardID:
                reducedSum += sumMan * 10 / 100
                sumMan = sumMan * 90 / 100
                break
        for cars in self.__car_repository.read_all():
            if cars.get_id_entity() == carID and cars.get_car_guarantee():
                reducedSum += piecesCost
                piecesCost = 0.0

        transaction = Transaction(transactionID, carID, cardID, piecesCost, sumMan, date, hour, reducedSum)
        self.__transaction_validator.validate_transaction(transaction)
        self.__transaction_repository.create(transaction)

    def get_all_transactions(self):
        """
        The functionality for getting all the object from file
        :return: all the transactions from storage
        """
        found_transactions = []
        for transaction in self.__transaction_repository.read_all():
            found_transactions.append(transaction)
        return found_transactions

    def get_transaction(self, transaction_id):
        """
        The functionality for getting an object by given id
        :param transaction_id: int
        :return: the Transaction object that has the given id
        """
        return self.__transaction_repository.read_by_id(transaction_id)

    def update_transaction(self,
                           new_transaction_id,
                           new_car_transacted_id,
                           new_customer_card_transaction_id,
                           new_pieces_cost,
                           new_workmanshipCost,
                           new_date,
                           new_time,
                           reducedSum):
        """
        Update an Transaction object
        :param new_transaction_id: int
        :param new_car_transacted_id: int
        :param new_customer_card_transaction_id: int
        :param new_pieces_cost: float
        :param new_workmanshipCost: float
        :param new_date: string
        :param new_time: float
        :param reducedSum: float
        :return:
        """
        new_time = float(new_time)
        if new_car_transacted_id not in self.get_cars_id():
            raise InvalidIdException("There is no such car with that id")
        for card in self.__customer_card_repository.read_all():
            if card.get_id_entity() == new_customer_card_transaction_id:
                reducedSum += new_workmanshipCost * 10 / 100
                new_workmanshipCost = new_workmanshipCost * 90 / 100
                break
        for cars in self.__car_repository.read_all():
            if cars.get_id_entity() == new_car_transacted_id and cars.get_car_guarantee():
                reducedSum += new_pieces_cost
                new_pieces_cost = 0.0
        transaction = Transaction(new_transaction_id,
                                  new_car_transacted_id,
                                  new_customer_card_transaction_id,
                                  new_pieces_cost,
                                  new_workmanshipCost,
                                  new_date,
                                  new_time,
                                  reducedSum)
        self.__transaction_validator.validate_transaction(transaction)
        self.__transaction_repository.update(transaction)

    def remove_transaction(self, transaction_id):
        """
        Deletes the Transaction object with the given id
        :param transaction_id: int
        """
        self.__transaction_repository.delete(transaction_id)

    def showTransactionWithSumInRange(self, lessSum, greaterSum):
        """
        Filtered transactions with the amount within a given range
        :param lessSum: start of range
        :param greaterSum: end of range
        :return: filtered list
        """
        return filter(lambda transaction: lessSum < transaction.get_workmanship_cost() + transaction.get_pieces_cost() < greaterSum,
                      self.__transaction_repository.read_all())

    """
    def showCardClientDescOrd(self):
        transactions = self.__transaction_repository.read_all()
        maxPerId = {}
        for transaction in transactions:
            idCard = transaction.get_cardID()
            sumDiscount = transaction.get_discount()
            if idCard not in maxPerId:
                maxPerId[idCard] = 0
            maxPerId[idCard] += sumDiscount
        newMaxPerId = sorted(maxPerId, key=maxPerId.__getitem__, reverse=True)
        return newMaxPerId
        """

    @staticmethod
    def __get_date_in_format(date):
        """
        Transforms a string that represents a date into datetime format
        :param date: string
        :return: a datetime date
        """
        date_list = date.split(sep="/")
        year = int(date_list[2])
        month = int(date_list[1])
        day = int(date_list[0])
        date_in_date_format = datetime.datetime(year, month, day)
        return date_in_date_format

    def get_transactions_between_two_dates(self, date_one, date_two):
        """
        Gets all the transactions made between two given dates
        :param date_one: string
        :param date_two: string
        :return: list of Transaction objects type
        """
        list_of_transactions = []
        self.__transaction_validator.validate_date(date_one)
        self.__transaction_validator.validate_date(date_two)
        date_one_obj = self.__get_date_in_format(date_one)
        date_two_obj = self.__get_date_in_format(date_two)
        difference = date_two_obj - date_one_obj
        for transaction in self.__transaction_repository.read_all():
            checked_date = self.__get_date_in_format(transaction.get_date())
            zero_days = datetime.timedelta(0)
            if difference > zero_days:
                if (checked_date - date_one_obj) > zero_days and \
                        (date_two_obj - checked_date) > zero_days:
                    list_of_transactions.append(transaction.get_id_entity())
            elif difference < zero_days:
                if (date_one_obj - checked_date) > zero_days and \
                        (checked_date - date_two_obj) > zero_days:
                    list_of_transactions.append(transaction.get_id_entity())
            elif difference == zero_days:
                list_of_transactions = []
        return list_of_transactions

    def remove_transactions_between_two_dates(self, date_one, date_two):
        """
        Deletes all the transactions made between two given dates
        :param date_one: string
        :param date_two: string
        """
        self.__transaction_validator.validate_date(date_one)
        self.__transaction_validator.validate_date(date_two)
        date_one_obj = self.__get_date_in_format(date_one)
        date_two_obj = self.__get_date_in_format(date_two)
        difference = date_two_obj - date_one_obj
        list_of_transaction_to_remove = []
        for transaction in self.__transaction_repository.read_all():
            checked_date = self.__get_date_in_format(transaction.get_date())
            zero_days = datetime.timedelta(0)
            if difference > zero_days:
                if (checked_date - date_one_obj) > zero_days and \
                        (date_two_obj - checked_date) > zero_days:
                    list_of_transaction_to_remove.append(transaction.get_id_entity())
            elif difference < zero_days:
                if (date_one_obj - checked_date) > zero_days and \
                        (checked_date - date_two_obj) > zero_days:
                    list_of_transaction_to_remove.append(transaction.get_id_entity())
            elif difference == zero_days:
                list_of_transaction_to_remove.append(transaction.get_id_entity())
        for i in range(len(list_of_transaction_to_remove)):
            self.remove_transaction(list_of_transaction_to_remove[i])
