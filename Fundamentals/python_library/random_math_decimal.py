# the first I uer the math module 
import math

# grateres commen devider
print(math.gcd(2, 5, 8, 9))  
# less commen multipier
print(math.lcm(2, 5, 8, 9))
# to a round to less value 
print(math.floor(8.8))
# to a round to large value
print(math.ceil(8.1))
# to a round to real number
print("this round value : ", round(8.4), ":",round(8.6))

# to use expatial (e)
print(math.exp(4))
# to use loge 
print(math.log(1000, 10))
print(math.log10(1000))
# to use power 
print(8**2)
print(pow(8,2))  
# to take squr file of value of root
print(math.sqrt(4))
# constant value 
print(f"constant value : \npi : {math.pi}\ne: {math.e} ")

print("=" * 40)

# ====================================================
import decimal 

# requmend to use 
print(decimal.getcontext())
# you cant deals with as math 
decimal1 = decimal.Decimal(8.3)
decimal2 = decimal.Decimal("6.2")
decimal3 = decimal.Decimal(5/2)
list_decimal = [decimal1, decimal2, decimal3]
print(decimal1)
print(decimal2)
print(decimal3)
print(f"the max value : {max(list_decimal)}")
print(f"the min value : {min(list_decimal)}")
print(f"the squre value : {decimal3.sqrt()}")
com1 = decimal.Decimal(0.1 + 0.1 + 0.1)
com2 = decimal.Decimal(0.3)
print(0.1 + 0.1 + 0.1 == 0.3)
print(com1 == com2 )
print("=" * 40)

# ====================================================
import random

# to take random number in range 0 -> 1
print(random.random())
print(random.random())

# to take random number in range you give him
print(random.randint(1, 100))
print(random.randint(1, 100))

# to take random in range of number and give you random choice
print(random.randrange(1000))
print(random.randrange(1000))
print(random.randrange(1000))

# to take random value from squance varibles
names = ['Ahamed', 'Mohammed', 'Majid', 'jana', 'Abdurabu', 'Saleh']
print(random.choice(names))
# to take many value 
print(random.choices(names, k = 3))

# to random reorder the squance varible 
print(names)
random.shuffle(names)
print(names)