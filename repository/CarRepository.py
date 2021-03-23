import json

from domain.Car import Car
from exception.InvalidCarException import InvalidCarException


class CarRepository:
    def __init__(self, filename):
        self.__car_storage = {}
        self.__filename = filename

    def __load_from_file(self):
        try:
            with open(self.__filename, "r") as f_read:
                saved_cars = json.load(f_read)
                self.__car_storage.clear()
                for saved_car in saved_cars:
                    car = Car(*saved_car)
                    self.__car_storage[car.get_id_entity()] = car
        except FileNotFoundError:
            self.__car_storage = {}

    def __save_to_file(self):
        to_save = []
        for car in self.__car_storage.values():
            found_car = [car.get_id_entity(),
                              car.get_car_model(),
                              car.get_car_year(),
                              car.get_car_km(),
                              car.get_car_guarantee()]
            to_save.append(found_car)
        with open(self.__filename, "w") as f_write:
            json.dump(to_save, f_write)

    def create(self, car):
        self.__load_from_file()
        if not isinstance(car, Car):
            raise InvalidCarException("This is not a car type")
        key = car.get_id_entity()
        if key in self.__car_storage:
            raise InvalidCarException("Id {} already exists".format(car.get_id_entity()))
        self.__car_storage[key] = car
        self.__save_to_file()

    def read_by_id(self, car_id):
        self.__load_from_file()
        if car_id in self.__car_storage:
            return self.__car_storage[car_id]
        return None

    def read_all(self):
        self.__load_from_file()
        return self.__car_storage.values()

    def update(self, car):
        self.__load_from_file()
        if not isinstance(car, Car):
            raise InvalidCarException("This is not a car type")
        car_id = car.get_id_entity()
        if car_id not in self.__car_storage:
            raise InvalidCarException("Id {} already exists".format(car.get_id_entity()))
        self.__car_storage[car_id] = car
        self.__save_to_file()

    def delete(self, car_id):
        self.__load_from_file()
        if car_id not in self.__car_storage:
            raise InvalidCarException("There's no ID = {}".format(car_id))
        del self.__car_storage[car_id]
        self.__save_to_file()
