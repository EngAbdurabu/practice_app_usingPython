'''
number = int(input("enter a number : "))
# using for loop when the number or reapat know before work 
for x in range(1,13):# in range(strat number , end number - one )
    print(str(number), ' * ', x, ' = ', number * x )


print("==" * 50)
x = 3 
while x > 0:
    print(x)
    x = x - 1 



x = 0
while x < 100:
    x += 1
    if x %2 != 0: print('odd number : ', x, end = ' ') # write by this method only when have on line of code in instruction 
    # end make space in the end of code 
    else:continue # jump to another condition 

print("==" * 50)

x = 1 
while True: # infinit loop 
    print(x, end = ' ')
    x +=2 
    if x > 100:
        break  # when the condition is true stop the loop not any instruction work in after the break if in the same indention
        print('the end')  # not work 
print('the end ')
'''  
x = 1 
while x < 100: 
    print(x, end = ' ')
    x +=2 
else:
    print('the end')
