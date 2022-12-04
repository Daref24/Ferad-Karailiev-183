class MissingParameterError(Exception):
    pass
    
class InvalidParameterError(Exception):
    pass

class InvalidAgeError(InvalidParameterError):
    pass

class InvalidSoundError(InvalidParameterError):
    pass

class JungleAnimals:
    def __init__(self,name,age,sound):
        self.n = name
        self.a = age
        self.s = sound

    def make_sound(self):
        print(f"{self.n} makes {self.s}")

    def print(self):
        pass
    
    def daily_tast(self):
        pass