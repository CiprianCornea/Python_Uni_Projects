import random
import string

from domain.Car import Car
from domain.CarValidator import CarValidator
from repository.GenericRepository import GenericRepository
from myTools.MyTools import my_sorted

"""
class UserOperation:
    def __init__(self, action, reverse_action):
        self.__action = action
        self.__reverse_action = reverse_action
        self.__last_result = None

    def apply_action(self):
        self.__last_result = self.__action()

    def apply_reverse_action(self):
        self.__reverse_action(self.__last_result)
"""


class CarServiceLab11:
    """
    The class for car service
    """
    def __init__(self,
                 car_repository: GenericRepository,
                 car_validator: CarValidator,
                 transaction_repository: GenericRepository):
        """
        Initialization for car service
        :param car_repository: car repository
        :param car_validator: car validator
        :param transaction_repository: transaction repository
        """
        self.__car_repository = car_repository
        self.__car_validator = car_validator
        self.__transaction_repository = transaction_repository
        self.__undo = []
        self.__redo = []

    """
    def __apply_operation(self, operation: UserOperation):
        operation.apply_action()
        self.__operations_for_undo.append(operation)
    """

    # CREATE
    def add_car(self,
                car_id,
                car_model,
                car_year,
                car_km,
                car_guarantee,
                isRemoved):
        """
        Creates a car
        :param car_id: int
        :param car_model: string
        :param car_year: int
        :param car_km: int
        :param car_guarantee: bool
        :param isRemoved: bool
        """
        if car_guarantee not in ['yes', 'no']:
            raise ValueError('Guarantee must be yes or no')
        if car_guarantee == 'yes':
            car_guarantee = True
        else:
            car_guarantee = False
        car = Car(car_id, car_model, car_year, car_km, car_guarantee, isRemoved)
        self.__car_validator.validate_car(car)
        self.__car_repository.create(car)
        # self.__undo.append(lambda: self.delete_car(car_id))
        """
        add_operation = UserOperation(
            lambda: self.__car_repository.create(car),
            lambda action_result: self.__car_repository.delete(car_id)
        )
        
        self.__apply_operation(add_operation)
        """

    # READ

    def getAll(self):
        """
        The functionality for getting all the object from file
        :return: all object from file
        """
        return self.__car_repository.read_all()

    # UPDATE

    def update_car(self,
                   new_car_id,
                   new_car_model,
                   new_car_year,
                   new_car_km,
                   new_car_guarantee,
                   isRemoved):
        """
        Update a Car object
        :param new_car_id: int
        :param new_car_model: string
        :param new_car_year: int
        :param new_car_km: int
        :param new_car_guarantee: bool
        :param isRemoved: bool
        """
        oldCar = self.__car_repository.read_by_id(new_car_id)
        if new_car_guarantee not in ['yes', 'no']:
            raise ValueError('Guarantee must be yes or no')
        if new_car_guarantee == 'yes':
            new_car_guarantee = True
        else:
            new_car_guarantee = False
        car = Car(new_car_id, new_car_model, new_car_year, new_car_km, new_car_guarantee, isRemoved)
        self.__car_validator.validate_car(car)
        self.__car_repository.update(car)
        # self.__undo.append(lambda: self.__car_repository.update(oldCar))
        """
        car = self.__car_repository.read_by_id(new_car_id)
        prev_car_model = car.get_car_model()
        prev_car_year = car.get_car_year()
        prev_car_km = car.get_car_km()
        prev_car_guarantee = car.get_car_guarantee()
        prev_car_isRemoved = car.get_isRemoved()
        car = Car(new_car_id, new_car_model, new_car_year, new_car_km,
                  new_car_guarantee, isRemoved)
        car_prev = Car(new_car_id, prev_car_model, prev_car_year, prev_car_km,
                       prev_car_guarantee, prev_car_isRemoved)
        self.__car_validator.validate_car(car)
        add_operation = UserOperation(
            lambda: self.__car_repository.update(car),
            lambda action_result: self.__car_repository.update(car_prev)
        )
        self.__apply_operation(add_operation)
        """

    # DELETE

    def delete_car(self, car_id):
        """
        Delete an object by a given id
        :param car_id: int
        :return: -
        """
        """
        car_copy = self.__car_repository.read_by_id(car_id)
        remove_car_operation = UserOperation(
            lambda: self.__car_repository.delete(car_id),
            lambda transactions: self.reverse_delete_car_and_transactions(car_copy, transactions)
            )
        self.__apply_operation(remove_car_operation)
        """
        for car in self.__car_repository.read_all():
            if car.get_id_entity() == car_id:
                self.__undo.append(lambda: self.__car_repository.create(car))
                break
        self.__car_repository.delete(car_id)

    """
    def reverse_delete_car_and_transactions(self, car_copy, transactions):
        car_id = car_copy.get_id_entity()
        car_model = car_copy.get_car_model()
        car_year = car_copy.get_car_year()
        car_km = car_copy.get_car_km()
        car_guaranteeC = car_copy.get_car_guarantee()
        car_guarantee = 'no'
        if car_guaranteeC:
            car_guarantee = 'yes'
        car_isRemoved = car_copy.get_isRemoved()
        self.update_car(car_id, car_model, car_year, car_km, car_guarantee, car_isRemoved)
        for transaction in transactions:
            self.__transaction_repository.create(transaction)
    """

    def get_list_of_car_that_match(self, the_string):
        """
        Finds all thew cars that contains the given string into them
        :param the_string: string
        :return: a list of cars
        """
        found_car = []
        for car in self.__car_repository.read_all():
            if the_string in car.get_text_format():
                found_car.append(car)
        return found_car

    def populate(self, n):
        """
        Creates n Car objects
        :param n: int
        :return: list of all cars from storage
        """
        list_of_id = []
        for car in self.__car_repository.read_all():
            car_id = car.get_id_entity()
            list_of_id.append(car_id)
        sorted_list = sorted(list_of_id)
        start_id = sorted_list[-1] + 1
        letters = string.ascii_letters
        for index in range(n):
            car_model = ''.join(random.choice(letters) for i in range(15))
            car_year = int(random.randint(0, 100000))
            car_km = int(random.randint(0, 100000000))
            car_guarantee = random.choice(['yes', 'no'])
            car = Car(start_id, car_model, car_year, car_km, car_guarantee, False)
            self.__car_validator.validate_car(car)
            self.add_car(start_id, car_model, car_year, car_km, car_guarantee, False)
            start_id += 1
        return self.__car_repository.read_all()

    def clear(self):
        """
        Clear the repository
        :return: -
        """
        self.__car_repository.clear()

    def showCarsBasedOnSumMan(self):
        """
        Ordered cars in descending order by the amount obtained on the labor
        :return: sorted list
        """
        list_of_cars = self.__car_repository.read_all()
        max_per_id = {}
        for transaction in self.__transaction_repository.read_all():
            car_id_transaction = transaction.get_carID()
            workmanshipCost = transaction.get_workmanship_cost()
            if car_id_transaction not in max_per_id:
                max_per_id[car_id_transaction] = 0
            max_per_id[car_id_transaction] += workmanshipCost
        list_of_filtered_cars = []
        for carr in list_of_cars:
            if carr.get_id_entity() in max_per_id:
                list_of_filtered_cars.append(carr)
        final_list = my_sorted(list_of_filtered_cars,
                               key=lambda caR: max_per_id[caR.get_id_entity()],
                               reverse=True)
        list_of_sumMan = []
        for car in final_list:
            list_of_sumMan.append(max_per_id[car.get_id_entity()])
        list_of_car_and_sum_man = zip(final_list, list_of_sumMan)
        return list_of_car_and_sum_man

    def modifyGuarantee(self):
        """
        Update of the warranty on each car: a car is under warranty if and only if it is maximum 3 years and maximum 60 000 km
        :return: -
        """
        cars = self.__car_repository.read_all()
        for car in cars:
            date = 2019 - car.get_car_year()
            if car.get_car_km() <= 60000 and date <= 3:
                newCar = Car(car.get_id_entity(), car.get_car_model(), car.get_car_year(), car.get_car_km(),
                             True, car.get_isRemoved())
                self.__car_validator.validate_car(newCar)
                self.__car_repository.update(newCar)
            else:
                newCar = Car(car.get_id_entity(), car.get_car_model(), car.get_car_year(), car.get_car_km(),
                             False, car.get_isRemoved())
                self.__car_validator.validate_car(newCar)
                self.__car_repository.update(newCar)

    def get_car(self, id_car):
        """
        Get a car by id
        :param id_car: car id
        :return: car by id
        """
        return self.__car_repository.read_by_id(id_car)

    def delete_cars(self, cars):
        for car in cars:
            self.delete_carr(car.get_id_entity())

    def delete_carr(self, id_car):
        self.__car_repository.delete(id_car)

    def removePopulate_car(self, list_cars):
        for thing in list_cars:
            self.__car_repository.delete(thing.get_id_entity())
