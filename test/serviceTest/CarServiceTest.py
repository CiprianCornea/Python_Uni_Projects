import unittest

from domain.CarValidator import CarValidator
from repository.GenericRepository import GenericRepository
from service.CarService import CarService


class CarServiceTest(unittest.TestCase):
    def test_add_car(self):
        car_repository = GenericRepository('test.pickle')
        transaction_repository = GenericRepository('test1.pickle')
        car_validator = CarValidator()
        car_service = CarService(car_repository, car_validator, transaction_repository)
        car_service.add_car(1, 'logan', 2006, 20000, 'no', False)
        self.assertEqual(len(car_repository.read_all()), 1)
        self.assertEqual(len(car_service.getAll()), 1)
        car_repository.delete(1)

    def test_update_car(self):
        car_repository = GenericRepository('test.pickle')
        transaction_repository = GenericRepository('test.pickle')
        car_validator = CarValidator()
        car_service = CarService(car_repository, car_validator, transaction_repository)
        car_service.add_car(1, 'logan', 2006, 20000, 'no', False)
        car_service.update_car(1, 'audi', 2005, 20000, 'no', False)
        car = car_service.get_car(1)
        self.assertEqual(car.get_car_model(), 'audi')
        self.assertEqual(car.get_car_year(), 2005)
        car_repository.delete(1)

    def test_get_all_drugs_that_match(self):
        car_repository = GenericRepository('test.pickle')
        transaction_repository = GenericRepository('test.pickle')
        car_validator = CarValidator()
        car_service = CarService(car_repository, car_validator, transaction_repository)
        car_service.add_car(1, 'logan', 2006, 20000, 'no', False)
        car_service.add_car(2, 'bmw', 2006, 20000, 'no', False)
        car_service.add_car(3, 'bmw', 2006, 20000, 'no', False)
        list_of_cars = car_service.get_list_of_car_that_match("bmw")
        self.assertEqual(len(list_of_cars), 2)
        car_repository.delete(1)
        car_repository.delete(2)
        car_repository.delete(3)

    def test_populate(self):
        car_repository = GenericRepository('test.pickle')
        transaction_repository = GenericRepository('test.pickle')
        car_validator = CarValidator()
        car_service = CarService(car_repository, car_validator, transaction_repository)
        car_service.add_car(1, 'logan', 2006, 20000, 'no', False)
        car_service.populate(2)
        self.assertEqual(len(car_service.getAll()), 3)
        car_repository.delete(1)
        car_repository.delete(2)
        car_repository.delete(3)

    def test_delete(self):
        car_repository = GenericRepository('test.pickle')
        transaction_repository = GenericRepository('test.pickle')
        car_validator = CarValidator()
        car_service = CarService(car_repository, car_validator, transaction_repository)
        car_service.add_car(1, 'logan', 2006, 20000, 'no', False)
        car_repository.delete(1)
        self.assertEqual(len(car_service.getAll()), 0)

    def test_showCarsBasedOnSumMan(self):
        car_repository = GenericRepository('test.pickle')
        transaction_repository = GenericRepository('test1.pickle')
        car_validator = CarValidator()
        car_service = CarService(car_repository, car_validator, transaction_repository)
        car_service.add_car(1, 'logan', 2006, 20000, 'no', False)
        car_service.add_car(2, 'logan', 2006, 20005, 'no', False)
        storage = car_service.showCarsBasedOnSumMan()
        self.assertEqual(len(storage), 0)
        car_repository.delete(1)
        car_repository.delete(2)

    def test_modifyGuarantee(self):
        car_repository = GenericRepository('test.pickle')
        transaction_repository = GenericRepository('test.pickle')
        car_validator = CarValidator()
        car_service = CarService(car_repository, car_validator, transaction_repository)
        car_service.add_car(1, 'logan', 2018, 20000, 'no', False)
        car_service.modifyGuarantee()
        self.assertEqual(car_service.get_car(1).get_car_guarantee(), True)
        car_repository.delete(1)
