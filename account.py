from errors import InvalidAccountType

class Account:
    ACC_TYPES = ("SAVINGS", "CREDIT", "PAYMENT")

    def __init__(self, iban, currency, type, balance):
        if type not in Account.ACC_TYPES:
            raise InvalidAccountType()

        self.iban = iban
        self.currency = currency
        self.type = type
        self.balance = balance