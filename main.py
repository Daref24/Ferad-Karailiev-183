from bank import Bank
from errors import InvalidUserData, InvalidMenuChoice

class Menu:
    def print_menu(self):
        print("1. Register a new user")
        print("2. Create an account for an existing user")
        print("3. List all users")
        print("4. List all accounts for an existing user")
        print("5. Deposit money to a user account")
        print("6. Withdraw money from a user account")
        print("7. Exit")

    def run(self):
        bank = Bank()

        # infinite menu loop
        while True:  
            self.print_menu()
            choice = input("Choose an item from the menu: \n> ")

            try:
                if choice == "1":
                    names = input("Enter the user's names (alpha-only): ")
                    fname, lname = names.split(" ")
                    if len(names) < 4 or not fname.isalpha() or not lname.isalpha():
                        raise InvalidUserData("Invalid names")

                    egn = input("Enter the user's EGN number (len 10, digits-only): ")
                    if len(egn) != 10 or not egn.isdigit():
                        raise InvalidUserData("Invalid EGN number")

                    bank.add_user(names, egn)
                elif choice == "2":

                    search_egn = input("Enter the desired user's EGN:  ")
                    crr = input("Enter desired currency:  ")
                    type = input("Enter desired type of the account (Either SAVINGS, PAYMENT or CREDIT):  ")
                    bank.add_account(search_egn,crr,type)

                elif choice == "3":
                    for u in bank.users:
                        print(u.get_print())
                elif choice == "4":
                    search_egn = input("Enter the desired user's EGN:  ")
                    desired_user = bank.find_user(search_egn)
                    i = 0
                    for f in desired_user.accounts:
                        print(f"{i}  |IBAN: {f.iban}| Currency: {f.currency}| Type: {f.type}| Balance: {f.balance}")
                        i += 1
                elif choice == "5":
                    search_egn = input("Enter the desired user's EGN:  ")
                    num_acc = int(input("Select the number of the desired account:  "))
                    value = float(input("Deposited amount: "))
                    bank.deposit(search_egn,num_acc,value)
                elif choice == "6":
                    search_egn = input("Enter the desired user's EGN:  ")
                    num_acc = int(input("Select the number of the desired account:  "))
                    value = float(input("Withdrawed amount: "))
                    bank.withdraw(search_egn,num_acc,value)
                elif choice == "7":
                    print("Goodbye\n")
                    break
                else:
                    raise InvalidMenuChoice("Error: Invalid choice")
            except Exception as ex:
                print(f"Error: There was an error while executing the command:\n{str(ex)}")
            
            print()

if __name__ == '__main__':
    menu = Menu()
    menu.run()