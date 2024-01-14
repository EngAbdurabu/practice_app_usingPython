# the iterators 
x = iter(['a', 'b', 'c'])
print(x)
print(next(x)) # to print the next value 
print(next(x))
print(next(x))
print("=" * 30)

# Generators 
def my_generator():
    i = 0
    print("First value ")
    yield i
    i += 1
    print("Second value ")
    yield i
    i += 1
    print("Last value ")
    yield i 
    
my_gen = my_generator()
print(next(my_gen))
# print(next(my_generator()))
print(next(my_gen))
print(next(my_gen))
print("-" * 40)

# pipelining with generators
def odd_numbers(numbers):
    for num in range(1,numbers,2):
        yield num
        
def Square(nums):
    for num in nums:
        yield num ** 2
    
print(odd_numbers(10))
print(Square(odd_numbers(10)))
print(sum(Square(odd_numbers(10))))
print("=" * 40)

# لاختصار الطريق السابقة نعمل الاتي 
odd_Numbers = (num for num in range(1,10,2))
square = (num ** 2 for num in odd_Numbers)
print(sum(square))
print("=" * 40)

# more summery for berviuse 
resulte = sum(x ** 2 for x in (x for x in range(1,10,2)))
print(resulte)