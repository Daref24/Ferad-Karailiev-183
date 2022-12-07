from random import *

class MissingParameterError(Exception):
    pass
    
class InvalidParameterError(Exception):
    def __init__(self,invalid_parameter,*args):
        message = f"invalid class parameter: {invalid_parameter}"
        super().__init__(message,*args)


class InvalidAgeError(InvalidParameterError):
    def __init__(self):
        super().__init__('age')

class InvalidSoundError(InvalidParameterError):
    def __init__(self):
        super().__init__('sound')

class JungleAnimals:
    def __init__(self,name,age,sound):
        self.name = name
        self.age = age
        self.sound = sound

        if name == None or age == None or sound == None:
            raise MissingParameterError()   
        if type(name) != str:
            raise InvalidParameterError('name')
        if type(age) != int:
            raise InvalidAgeError()
        if type(sound) != str:
            raise InvalidSoundError()

    def make_sound(self):
        print(f"{self.name} makes {self.sound}!")
    def print(self):
        pass
    def daily_task(self):
        pass

class Jaguar(JungleAnimals):
    def __init__(self,name,age,sound):
        super().__init__(name,age,sound)
        if self.age > 15:
            raise InvalidSoundError()
        if self.sound.count('r') < 2:
            raise InvalidSoundError
    
    def print(self):
        print(f"Jaguar {self.name}, {self.age}, {self.sound}")
    
    def daily_task(self,animals):
        for i in range(len(animals)):
            if type(animals[i]) == Lemur or type(animals[i]) == Human:
                print(f"{self.name} the Jaguar hunted down {animals[i].name} the {type(animals[i]).__name__}")
                del animals[i]

class Lemur(JungleAnimals):
    def __init__(self,name,age,sound):
        super().__init__(name,age,sound)
        if self.age > 10:
            raise InvalidAgeError()
        if 'e' not in self.sound:
            raise InvalidSoundError()
        
    def print(self):
            print(f"Lemur({self.name}, {self.age}, {self.sound})")

    def daily_task(self,fruits):
        if fruits >= 10:
            print(f"{self.name} the Lemur ate a full meal of 10 fruits")
            return fruits - 10
        elif fruits < 10:
            print(f"{self.name} the Lemur could only find {fruits} fruits")
            return 0
        elif fruits <= 0:
            self.make_sound()
            self.make_sound()
            return 0
    
class Human(JungleAnimals):
    def __init__(self,name,age,sound):
        super().__init__(name,age,sound)
        if self.age > 10:
            raise InvalidAgeError()
        if 'e' not in self.sound:
            InvalidSoundError()
    
    def print(self):
        print(f"Human {self.name}, {self.age}, {self.sound}")

    def daily_task(self,animals,buildings):
        for i in range(len(animals)):
            if i == 0:
                if type(animals[i]) == Human and type(animals[i+1]) == Human:
                    f = Building('_|^|_')
                    buildings.append(f)
            elif i == -1:
                if type(animals[i]) == Human and type(animals[i-11]) == Human:
                    f = Building('_|^|_')
                    buildings.append(f)
            else:
                if type(animals[i]) == Human and type(animals[i-1]) == Human and type(animals[i+1]) == Human:
                    f = Building('_|^|_')
                    buildings.append(f)
class Building:
    def __init__(self,build):
        self.build = build
    
fruits = 100
animals = []
buildings = []

names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]

for i in range(102):
    f = randint(0,9)
    if f >= 0 and f <= 3:
        animal = Lemur(names[randint(len(names))],randint(0,20),sounds[randint(len(sounds))])
    if f >= 4 and f <= 7:
        animal = Jaguar(names[randint(len(names))],randint(0,20),sounds[randint(len(sounds))])
    if f >= 8 and f <= 9:
        animal = Human(names[randint(len(names))],randint(0,20),sounds[randint(len(sounds))])
    animals.append(animal)

print(f"The jungle now has {len(animals)} animals")

for anim in animals:
    if type(anim) == Lemur:
        fruits = anim.daily_task(fruits)
    if type(anim) == Jaguar:
        anim.daily_task(animals)
    if type(anim) == Lemur:
        anim.daily_task(animals,buildings)

print(f"The jungle now has {len(animals)} animals")
print(fruits)
print(animals)
print(buildings)
