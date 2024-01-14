numbers = [2, 30, 40, 50, 3, 5, 2, 33, 54, 80, 70, 7]

my_numbers = []
for number in numbers:
    if number > 30:
        my_numbers.append(number)
print(my_numbers)

# to replace the above method py comprehension 
my_numbers_1 = [number for number in numbers if number > 30]
print(my_numbers_1)

squar_numbers = [num **2 for num in range(1,10)]
print(squar_numbers)

# use comprehension in dictionary 
Numbers = {i:i**2 for i in range(10)} # important to defined the key 
print(Numbers)

# use comprehension with sets 
Numbers1 = [2, 4, 4, 5, 3, 5, 7, 4, 7, 34, 65, 23, 5, 4]
New_Numbers = {num for num in Numbers1}
print(New_Numbers)

# make matrix 
Matrix = [[i for i in range(5)] for j in range(6)]
print(Matrix)
# make Zeroes matrix 
Matrix_1 = [[ i * 0 for i in range(4)] for j in range(4)]
print(Matrix_1 )