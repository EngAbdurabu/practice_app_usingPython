# Question one factorail 
numbers = [ 2, 5, 3, 1, 4]
fac = 1
for number in numbers:
    fac *= number
print(fac)

# Question two sumation 
Sum = 0
new_numbers = []
for number in numbers:
    Sum += number
    new_numbers.append(Sum)
print(new_numbers)

# Question three 
Numbers = [1, 2, 2, 2, 4, 4, 5, 6, 7, 8, 8]
dous = []
seem = {}
for number in Numbers:
    if number not in seem:
        seem[number] = 1
    else:
        if seem[number] == 1:
            dous.append(number)
        seem[number] += 1

print(seem, '\n', dous)

# Question 4 we have a list of word make dicationary 
words = [ 'data', 'science', 'machin', 'learing']
dic_word = {}
for word in words:
    dic_word[word] = len(word)
print(dic_word)
# another solution 
dic_word = {word:len(word) for word in words}
print(dic_word)

# Question 5 divid the list to multilist equal in element depend on orginal list
Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, Second, third = [], [], []
for number in Numbers:
    if number in range(4):
        first.append(number)
    if number in range(4,7):
        Second.append(number)
    if number in range(7,10):
        third.append(number)
        
print(f"{first}\n{Second}\n{third}")

# another solution 
grouped_number = []
size = 3
for i in range(0,len(Numbers), size):
    grouped_number.append(Numbers[i:i + size] )
print(grouped_number)