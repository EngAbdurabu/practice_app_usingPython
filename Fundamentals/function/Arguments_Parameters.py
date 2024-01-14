def print_name(name):
    print("Hello", name)


print_name("Abdurau")
print("*" * 100)


# positional arguments
def print_info(name, age, weight): # type: ignore
    print(f"Name : {name}, age : {age}, weight : {weight}")


print_info("Abdurabu", 25, 95)

# keyword arguments
print_info(name="Abdurabu", age=25, weight=95)

# default parameter  assginet the value to parameter


def print_info(name, weight, age=25):
    # default argument always in the last in defination
    print(f"Name : {name}, age : {age}, weight : {weight}")


print_info("Abdurabu", weight=95)
print("*" * 100)


# use funcation with unknow number of argurments
def print_fruits(*fruits):  # always use *args intead of fruits
    for fruit in fruits:
        print(f"I like the {fruit}")


print_fruits("Apple", "orange", "bnanna", "peach", "watermalen", "lemen")
print("*" * 100)


# use function with unknow number of argurments with keyword arguments
def weather(**kwarags):
    print(kwarags)


# thsi give me the output as dictionary
weather(
    location="Yemen",
    temparture=25,
    wind_dircation="south",
    wind_speed=5,
    condition="sunny",
    )

print("=" * 100)
# exercise 
"""
create function the suer enter two number and the second number must be the power of the first number     
"""
def power_number(num1, num2):
    print(num1 ** num2 )

power_number(4,4)
    
