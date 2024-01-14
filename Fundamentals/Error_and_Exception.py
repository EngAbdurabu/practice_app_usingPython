# for make exception 
# raise Exception(" This is an Exception ")

# # try and except 
# class NotName(Exception):
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return "You are not Abdurabu you can't Enter " 
# try:
#     name = input("Enter your name : ")
#     if name == "Abdurabu":
#         print("Welcome back to me")
#     elif name != "Abdurabu":
#         raise NotName("You are not Abdurabu you can't Enter ")
# except NotName as error:
#     print(error)

# # idea to applie 
# class MissMuch(Exception):
#     def __init__(self, args):
#         self.args = args
#     def __str__(self):
#         return "The first lettel must be captial littel"

# try:
#     city = input("Enter your city name:")
#     if city == city.capitalize():
#         print(f"your city name is : {city}")
#     elif city != city.capitalize():
#         raise MissMuch("The first lettel must be captial littel")
# except MissMuch as error:
#     print(error)

        
        

# Exercise 
"""_summary_

    class TooOldError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message
class TooYoungError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message
    

def check_age(age):
    
    try:
        if age > 15 and age < 40:
            print("your age is good ")
    
        elif age < 15:
            raise TooYoungError("you are too younger")

        elif age > 40:
            raise TooOldError("you are too old ")

    except TooYoungError as er:
        print(er)

    except TooOldError as er:
        print(er)

    finally:
        print("the excution is finished ")

check_age(age = int(input("Enter your age : "))) 

    Raises:
        TooYoungError: _description_
        TooOldError: _description_

    Returns:
        _type_: _description_
    """
