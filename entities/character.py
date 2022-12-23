class Character:
    def __init__(self, name, gender, role):
        self.name = name
        self.gender = gender
        self.role = role
        self.main_weapon = "Character has no weapon"
        self.additional_item = "Character has no additional item"
    
    def show_char(self):
        print(f"{self.name} | {self.gender} | {self.role} | {self.main_weapon} | {self.additional_item} |")
        