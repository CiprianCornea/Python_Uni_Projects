from domain.CustomerCardValidator import CustomerCardValidator
from domain.CarValidator import CarValidator
from domain.TransactionValidator import TransactionValidator
from repository.GenericRepository import GenericRepository
from service.CustomerCardServiceLab11 import CustomerCardServiceLab11
from service.CarServiceLab11 import CarServiceLab11
from service.TransactionServiceLab11 import TransactionServiceLab11
from user_interface.ConsoleLab11 import ConsoleLab11


def main():
    """
    MAIN FUNCTION
    :return: -
    """
    car_repository = GenericRepository("carsLab11.pkl")
    car_validator = CarValidator()
    customer_card_repository = GenericRepository("cardsLab11.pkl")
    customer_card_validator = CustomerCardValidator()
    transaction_repository = GenericRepository("transactionsLab11.pkl")
    transaction_validator = TransactionValidator()
    car_service = CarServiceLab11(car_repository,
                                  car_validator,
                                  transaction_repository)
    customer_card_service = CustomerCardServiceLab11(customer_card_repository,
                                                     customer_card_validator,
                                                     transaction_repository)
    transaction_service = TransactionServiceLab11(transaction_repository,
                                                  transaction_validator,
                                                  customer_card_repository,
                                                  car_repository)

    ui = ConsoleLab11(car_service,
                      customer_card_service,
                      transaction_service)
    ui.run_console()


main()
