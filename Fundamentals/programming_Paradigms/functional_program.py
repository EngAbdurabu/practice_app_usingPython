# map function
numbers = [1, 2, 3, 4, 5]
# def squar(x):
#     return x ** 2

# use lambda
squar = map(lambda x : x ** 2, numbers)
# squars = map(squar, numbers)
print(list(squar))

# another example 
temps = [("Damascus", 29), ("Cairo", 36), ("Baghdad", 44), ("Riyadh", 40), ("Beirut", 34), ("Tunis", 30)]
# F = 1.8*C + 32
def C_to_F(item):
    return item [0], (1.8)*item [1] + 32

f_temps = list (map (C_to_F, temps))
print (f_temps)

# smallest the  code 
print(list(map(lambda item: (item[0], (1.8) * item[1] + 32), temps)))

# for compersion use loop 
f_temps = []
for temp in temps:
    f = (1.8) * temp [1] + 32
    f_temps.append((temp [0], f))
print (f_temps)

print("-" * 100)

# filter function 
Languages = [('C', 1972), ('C++', 1985), ('Java', 1995), ('JavaScript', 1995), 
            ('PHP', 1994), ('Python', 1991)]
def old(item):
    return item[1] < 1990
    

print(list(filter(old, Languages)))

def find (iterable, text):
    def finder (lang):
        for i in lang:
            if str(i).startswith(text):
                return True
            return False
    return list(filter(finder, iterable))
results = find (Languages, 'J')
print (results)
results = find (Languages, 'P')
print (results)

print("-" * 100)

# reduce function 
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6]
def add(x, y):
    return x + y
print (reduce (add, numbers))

