import pickle

from exception.InvalidIdException import InvalidIdException


class GenericRepository:
    """
    The class for generic repository
    """
    def __init__(self, filename):
        """
        Initialization the generic repository
        :param filename: name of file (pickle file)
        """
        self.__storage = {}
        self.__filename = filename

    # FILE OPERATION

    def __load_from_file(self):
        """
        Function read from a given file
        :return: -
        """
        try:
            with open(self.__filename, "rb") as f_read:
                self.__storage = pickle.load(f_read)
        except FileNotFoundError:
            self.__storage = {}
        except Exception as ve:
            self.__storage.clear()
            print(ve)

    def __save_to_file(self):
        """
        Function write in a file
        """
        with open(self.__filename, "wb") as f_write:
            pickle.dump(self.__storage, f_write)

            # CRUD OPERATION
    # CREATE
    def create(self, entity):
        """
        Function create an object
        :param entity: an object of type Car, CustomerCard or Transaction
        """
        self.__load_from_file()
        id_entity = entity.get_id_entity()
        if id_entity in self.__storage:
            raise InvalidIdException('The entity id already exists!')
        self.__storage[id_entity] = entity
        self.__save_to_file()

    # READ
    def read_all(self):
        """
        Function read all the objects from storage
        :return:a list of all objects
        """
        self.__load_from_file()
        return self.__storage.values()

    # UPDATE
    def update(self, entity):
        """
        Function update an object
        :param entity: an object of type Car, CustomerCard or Transaction
        """
        self.__load_from_file()
        id_entity = entity.get_id_entity()
        if id_entity not in self.__storage:
            raise InvalidIdException('There is no entity with that id!')
        self.__storage[id_entity] = entity
        self.__save_to_file()

    # DELETE
    def delete(self, id_entity):
        """
        Function delete the object from storage with the given id
        :param id_entity: int
        """
        self.__load_from_file()
        if id_entity not in self.__storage:
            raise InvalidIdException('There is no entity with that id!')
        del self.__storage[id_entity]
        self.__save_to_file()

        # MORE OPERATIONS
    def clear(self):
        self.__load_from_file()
        self.__storage.clear()
        self.__save_to_file()

    def ensure_unique_cnp(self,
                          customer_card):
        for card_key in self.__storage:
            if self.__storage[card_key].get_customer_cnp() == customer_card.get_customer_cnp():
                raise InvalidIdException("CNP already exist!")

    def read_by_id(self, id_entity):
        """
        Function returns the object with the given id
        :param id_entity: int
        :return: object which has the given id
        """
        self.__load_from_file()
        if id_entity in self.__storage:
            return self.__storage[id_entity]
        return None

