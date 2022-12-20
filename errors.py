# User
class InvalidUserData(Exception):
    def __init__(self, message = "User already exists", *args: object):
        super().__init__(message, *args)

class UserNotFound(Exception):
    def __init__(self, message = "No user with such EGN", *args: object):
        super().__init__(message, *args)

class UserAlreadyExists(Exception):
    def __init__(self, message = "User already exists", *args: object):
        super().__init__(message, *args)

class UserAlreadyOwnsAccount(Exception):
    pass

# Account 
class AccountNotFound(Exception):
    def __init__(self, message = "Such account cannot be found", *args: object):
        super().__init__(message, *args)

class UnsufficientBalance(Exception):
    pass

class InvalidAccountData(Exception):
    pass

class InvalidAccountType(Exception):
    pass

# Bank


# Menu
class InvalidMenuChoice(Exception):
    pass