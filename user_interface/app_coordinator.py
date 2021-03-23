from domain.CustomerCardValidator import CustomerCardValidator
from domain.CarValidator import CarValidator
from domain.TransactionValidator import TransactionValidator
from repository.GenericRepository import GenericRepository
from service.CustomerCardService import CustomerCardService
from service.CarService import CarService
from service.TransactionService import TransactionService
from user_interface.Console import Console


def main():
    """
    MAIN FUNCTION
    :return: -
    """
    car_repository = GenericRepository("cars.pkl")
    car_validator = CarValidator()
    customer_card_repository = GenericRepository("cards.pkl")
    customer_card_validator = CustomerCardValidator()
    transaction_repository = GenericRepository("transactions.pkl")
    transaction_validator = TransactionValidator()
    car_service = CarService(car_repository,
                             car_validator,
                             transaction_repository)
    customer_card_service = CustomerCardService(customer_card_repository,
                                                customer_card_validator,
                                                transaction_repository)
    transaction_service = TransactionService(transaction_repository,
                                             transaction_validator,
                                             customer_card_repository,
                                             car_repository)

    ui = Console(car_service,
                 customer_card_service,
                 transaction_service)
    ui.run_console()


main()
