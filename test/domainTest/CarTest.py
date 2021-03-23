import unittest

from domain.Car import Car


class CarTest(unittest.TestCase):
    def test_not_equal(self):
        car_one = Car(1, 'logan', 2005, 200000, False, False)
        car_two = Car(2, 'audi', 2005, 200000, False, False)
        self.assertNotEqual(unittest.TestCase, car_one, car_two)

    def test_equal(self):
        car_one = Car(1, 'logan', 2005, 200000, False, False)
        car_two = Car(1, 'logan', 2005, 200000, False, False)
        self.assertEqual(car_one, car_two)

    def test_getter(self):
        car_one = Car(1, 'logan', 2005, 200000, False, False)
        self.assertEqual(1, car_one.get_id_entity())
        self.assertEqual('logan', car_one.get_car_model())
        self.assertEqual(2005, car_one.get_car_year())
        self.assertEqual(200000, car_one.get_car_km())
        self.assertEqual(False, car_one.get_car_guarantee())
        self.assertEqual(False, car_one.get_isRemoved())

    def test_setter(self):
        car_one = Car(1, 'logan', 2005, 200000, False, False)
        car_two = Car(1, 'audi', 2006, 200001, True, True)
        car_one.set_car_model('audi')
        car_one.set_car_year(2006)
        car_one.set_car_km(200001)
        car_one.set_car_guarantee(True)
        car_one.set_isRemoved(True)
        self.assertEqual(car_one, car_two)

    def test_get_text_format(self):
        car_one = Car(1, 'logan', 2005, 200000, False, False)
        carString = car_one.get_text_format()
        self.assertEqual(carString, '1,logan,2005,200000,False,False')
