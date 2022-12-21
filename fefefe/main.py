from entities.__init__ import Character, Weapon, Item
from errors import *

available_roles = ["warrior", "mage", "archer"]
weapon_types = ["sword","bow","staff"]
    
class Menu:
    def __init__(self):
        self.characters = []
    def print_menu(self):
        print("1. Create a new character")
        print("2. Craft a weapon for existing character")
        print("3. Add additional tool for existing character")
        print("4. Display all characters")
        print("5. Delete an existing character")
        print("6. Exit")
    
    def find_char(self,name):
        for f in self.characters:
            if f.name == name:
                return f
        
    def create_character(self, name, gender, role):
        found_char = self.find_char(name)
        if type(found_char) == Character:
            raise CharacterExists("This character name is already taken")

        new_char = Character(name,gender,role)
        self.characters.append(new_char)   

    def run(self):
        # infinite menu loop
        while True:  
            # print the menu
            # ...
            self.print_menu()
            # ask the user to choose a command
            choice = input("Choose an item from the menu: \n> ")
            

            # catch errors
            try:
                # process the user's choice
                if choice == "1": 
                    char_name = input("Enter a name for your character:  ")
                    char_gender = input("Enter the gender of your character (male or female):")
                    if char_gender != "male" and char_gender != "female":
                        raise InvalidGender("Choose either male or female")
                    char_role = input("Choose a class (archer / mage / warrior):  ")
                    if char_role not in available_roles:
                        raise InvalidCharacterClass("Such class doesn't exist")                
                    self.create_character(char_name,char_gender,char_role)
                    
                    
                elif choice == "2":
                    print("Your character can use a staff, a bow or a sword")
                    weapon_type = input("Choose your weapon:  ")
                    try:
                        attack = float(input("How much attack does your weapon have:  "))
                    except ValueError:
                        print("Weapon attack must be a number")
                    new_weapon = Weapon(weapon_type,attack)
                    
                elif choice == "4":
                    print("Your characters:")
                    for i in self.characters:
                        i.show_char()
                elif choice == "6":
                    print("See you later!")
                    break
                else:
                    raise InvalidCommand("Error: Invalid choice")
            except Exception as ex:
                print(f"Error: {str(ex)}")

            print()

if __name__ == '__main__':
    menu = Menu()
    menu.run()