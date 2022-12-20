from errors import InvalidAccountType, InvalidAccountData

class Account:
    ACC_TYPES = ("SAVINGS", "CREDIT", "PAYMENT")
    CURR_TYPES = ("BGN", "EUR", "USD")
    def __init__(self, iban, currency, type, balance):
        if type not in Account.ACC_TYPES:
            raise InvalidAccountType("Account type should be either SAVINGS, CREDIT or  PAYMENT")
        if currency not in Account.CURR_TYPES:
            raise InvalidAccountData("Available currencies are only BGN, EUR or USD")

        self.iban = iban
        self.currency = currency
        self.type = type
        self.balance = balance