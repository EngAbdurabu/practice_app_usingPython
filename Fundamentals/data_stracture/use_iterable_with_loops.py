# I know how can deals with all type with loop but dic no 
# dic 
units = {"mg" : 0.001, "cg" : 0.01, "dg" : 0.1, "g": 1, "kg" : 1000}
for unit in units.keys():
    print(unit, end = ", ")

for unit in units.values():
    print(unit, end=', ')

for unit in units.items():
    print(unit, end= " ")
    
print('\n')
for key, value in units.items():
    print('unit : ', key, ' multiplier : ', value)
    
for i, j in [(1, 2), (3, 4), (5, 6), (7, 8)]:
    print(i, j)
    
print("--" * 80)
employees = ["Ahmed", "Mjahed", "Saleh", "Salem", "Mohammed", "Abduallh"]
print("employees")
print("=" * 9)
for index in range(len(employees)):
    print(index + 1, employees[index])
print("**" * 50)
    
# using enumerate this use for punctuation the iterable element 
for count, value in enumerate(employees, start = 1):
    print(count, value)
    
# using while loop 
print("&"*39)
index = 0
while index < len(employees):
    print(index + 1, employees[index])
    index += 1
    