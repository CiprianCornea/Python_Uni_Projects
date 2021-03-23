import unittest

from test.domainTest.CarTest import CarTest
from test.domainTest.CustomerCardTest import CustomerCardTest
from test.domainTest.TransactionTest import TransactionTest
from test.repositoryTest.GenericRepositoryTest import GenericRepositoryTest
from test.serviceTest.CarServiceTest import CarServiceTest
from test.serviceTest.CustomerCardServiceTest import CustomerCardServiceTest
from test.serviceTest.TransactionServiceTest import TransactionServiceTest


def run_tests():
    loader = unittest.defaultTestLoader
    all_suites = \
        [
            loader.loadTestsFromTestCase(CarTest),
            loader.loadTestsFromTestCase(CustomerCardTest),
            loader.loadTestsFromTestCase(TransactionTest),
            loader.loadTestsFromTestCase(GenericRepositoryTest),
            loader.loadTestsFromTestCase(CarServiceTest),
            loader.loadTestsFromTestCase(CustomerCardServiceTest),
            loader.loadTestsFromTestCase(TransactionServiceTest)
        ]
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(unittest.TestSuite(all_suites))


if __name__ == '__main__':
    run_tests()
