# def Recursion():
#     print("Recursion Funcation")
#     return Recursion()

# Recursion()

# this for brack the unfant loop or return 
# this funcation return the factorial of the n number
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))
print("-" * 50)

data = [["Effective python", "Byte of Python", "python Essnetial Reference"],
        44, 12,'python cookbook ', ("Books", "Websites")]
def print_data(data):
    if not data:return
    if (type(data[0]) == list or type(data[0]) == tuple):
        print_data(data[0])
    else:
        print(data[0])
    print_data(data[1:])
    
print_data(data)