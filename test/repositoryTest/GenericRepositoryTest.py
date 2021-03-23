import unittest

from domain.Car import Car
from repository.GenericRepository import GenericRepository


class GenericRepositoryTest(unittest.TestCase):
    def test_create(self):
        filename = 'test.pickle'
        generic_repository = GenericRepository(filename)
        car_one = Car(1, 'logan', 2005, 200000, False, False)
        generic_repository.create(car_one)
        storage = generic_repository.read_all()
        self.assertEqual(len(storage), 1)
        generic_repository.delete(1)

    def test_update(self):
        filename = 'test.pickle'
        generic_repository = GenericRepository(filename)
        car_one = Car(1, 'logan', 2005, 200000, False, False)
        generic_repository.create(car_one)
        car_upd = Car(1, 'audi', 2005, 200000, False, False)
        generic_repository.update(car_upd)
        new_car = generic_repository.read_by_id(1)
        self.assertEqual(new_car.get_car_model(), 'audi')
        generic_repository.delete(1)

    def test_delete(self):
        filename = 'test.pickle'
        generic_repository = GenericRepository(filename)
        car_one = Car(1, 'logan', 2005, 200000, False, False)
        generic_repository.create(car_one)
        generic_repository.delete(1)
        storage = generic_repository.read_all()
        self.assertEqual(len(storage), 0)

