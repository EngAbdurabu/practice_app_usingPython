# defined the functions 
# def greeting():
#     name = input("Enter your name : ")
#     print(f"wellcome dear { name } this is your home ")

# greeting()

# def sum():
#     print(1)
#     print(4)
#     return
#     print(3+1)
# sum()

# def get_age():
#     age = int(input("Enter your age : "))
#     if age < 0:
#         return
#     elif age > 120:
#         return
#     print(age)

# get_age()

print("++" * 40)

def dagry():
    return 40
temperature = dagry()
print(temperature)

def temp_scal():
    return ['celues', 'fahrenhit', 'kilven']
scale = temp_scal()
for index, value in enumerate(scale, start=1):
    print(index, value )
    