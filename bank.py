from random import randint
from errors import UserNotFound, UserAlreadyExists, AccountNotFound, UnsufficientBalance
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
            raise UserNotFound()

        # generate iban
        iban = "BG9812"
        for i in range(0, 10):
            iban += str(randint(0, 9))

        balance = 0
        # create account object
        account = Account(iban, currency, type, balance)

        # call the user's add_account() method
        found_user.add_account(account)
    
    def deposit(self):
        search_egn = input("Enter the desired user's EGN:  ")
        found_user = self.find_user(search_egn)
        try:
            num_acc = int(input("Select the number of the desired account:  "))
        except:
            print("Must enter an integer!")
            return
        try:
            value = float(input("Deposit amount: "))
        except ValueError:
            print("Must enter a positive number!")
            return
        if found_user == None:
            raise UserNotFound()
        if value < 0:
            raise UnsufficientBalance("Must deposit a positive ammount!")
        try: 
            found_user.accounts[num_acc].balance += value
            print("New Balance:", found_user.accounts[num_acc].balance, found_user.accounts[num_acc].currency)
        except IndexError:
            print("Account not found")

    def withdraw(self):
        search_egn = input("Enter the desired user's EGN:  ")
        found_user = self.find_user(search_egn)
        try:
            num_acc = int(input("Select the number of the desired account:  "))
        except:
            print("Must enter an integer!")
            return
        try:
            value = float(input("Withdraw amount: "))
        except ValueError:
            print("Must enter a positive number!")
            return
        if found_user == None:
            raise UserNotFound()
        if value < 0:
            raise UnsufficientBalance("Must withdraw a positive ammount!")
        if value > found_user.accounts[num_acc].balance:
            raise UnsufficientBalance("You cant withdraw more than your balance!")
        try: 
            found_user.accounts[num_acc].balance -= value
            print("New Balance:", found_user.accounts[num_acc].balance, found_user.accounts[num_acc].currency)
        except IndexError:
            print("Account not found")
        
