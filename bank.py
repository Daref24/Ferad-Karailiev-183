from random import randint
from errors import UserNotFound, UserAlreadyExists
from account import Account
from user import User

class Bank:
    def __init__(self) -> None:
        self.users = []

    def find_user(self, user_egn: str) -> User:
        for u in self.users:
            if u.egn == user_egn:
                return u

    def add_user(self, names, egn):
        found_user = self.find_user(egn)

        if type(found_user) == User:
            raise UserAlreadyExists()

        user = User(names, egn)
        self.users.append(user)

    def add_account(self, user_egn, currency, type):
        # user exists?
        found_user = self.find_user(user_egn)

        if found_user == None:
            raise UserNotFound("No user with such EGN")

        # generate iban
        iban = "BG9812"
        for i in range(0, 10):
            iban += str(randint(0, 9))

        balance = 0
        # create account object
        account = Account(iban, currency, type, balance)

        # call the user's add_account() method
        found_user.add_account(account)
    
    def deposit(self, user_egn, num_acc, value):
        found_user = self.find_user(user_egn)
        found_user.accounts[num_acc].balance += value

    def withdraw(self, user_egn, num_acc, value):
        found_user = self.find_user(user_egn)
        found_user.accounts[num_acc].balance -= value