"""score = int(input("Enter your score : "))

if score > 100 or score < 0 :
    print("this is wrong value ")
    print("Enter the value in range of 100 ")
    exit()

if  90 <= score <= 100:
    print("your grad is : A ")
elif  80 <= score < 90:
    print("your grad is : B ")
elif  70 <= score < 80:
    print("your grad is : C ")
elif 60 <= score < 70:
    print("your grad is : D ")
elif 50 <=  score < 60:
    print("your grad is : E ")
else:
    print("your grad is : F ")

# the second exercise 
while True:
    name = input("Enter your name : ")
    if name == 'stop':
        break
    barthyear = int(input("Enter your barthyear : "))
    age = 2022 - barthyear 
    print("HI Dear : ",name.title())
    print("your age is : ", age )
    """
for i in range(1,6):
    print('* ' * i)
print('-' * 100)

for n in range(1,6):
    if n == 3:
        print('*Python3*')
        continue 
    else:
        print('* '*5)
print('-'*100)

num = 0
for i in range(0,4):# this go form 0 to 3 onl 
    for j in range(0,i+1):# when i = 0 the j = 1 that mean go form 0 to 0 only
        # when i = 1 the j = 2 that mean go from 0 to 1 only becuse the last number in range don't consider in the program ...  
        print(num, end = ' ')
        num +=1
    print()
        
    


