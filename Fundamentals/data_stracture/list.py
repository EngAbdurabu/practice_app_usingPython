list = [1, 3, 5, 6]
my_list = [3, 5, 7, list]
print(my_list)

# insted list 
building_homes = [[100, [1, [10], [11]], [2, [20], [21]]], [200, [1, [10], [11]], [2, [20], [21]]], [300, [1, [10], [11]], [2, [20], [21]]], [400, [1, [10], [11]], [2, [20], [21]]]]
print(building_homes[0][1][2][0])
# ==============================================================
#form my idea 
'''
name = input("Enter your name : ")
names = ['ahmed', 'saleh', 'mohammed', 'ali', 'majid', 'abdurabu','trky','salem']
if (name.upper() in names) or (name.lower() in names) or (name.title() in names):
    print(f" you name is {name} good lock")
'''
# ==============================================================
print("==" * 50)
names = ['ahmed', 'saleh', 'mohammed', 'ali', 'majid', 'abdurabu','trky','salem']
print(names,end = "\n -----------------------------------------------------------\n")

# to change an item from this list do the following 
names[-2] = 'chaild of Abduallh'
print(names,end = "\n -----------------------------------------------------------\n")

# to delete item
del names[-2]
print(names,end = "\n -----------------------------------------------------------\n")

# to add item without function 
names += ["hussin","khalal"]
print(names,end = "\n -----------------------------------------------------------\n")

# the function use in list 
## 1) append("new_item ") to add any element to list 
names.append([30,54,3,849,92949,84849])
print(names, end = "\n -----------------------------------------------------------\n")
del names[-1]

## 2) extend() to add list to anthor list and make them one list 
numbers = [1 , 3, 4, 5, 2, 5, 6 ,5]
names.extend(numbers)
print(names, end = "\n -----------------------------------------------------------\n")

## 3) insert() to add any item and determined when you want adding by location 
del names[-8:-1]
del names[-1]
print(names)
names.insert(1 ,"Trky")
print(names, end = "\n ----------------------------------------------------------- \n")

## 4) remove() to remove an item from list with mantion it's name only one item
names.remove("ali")
print(names ,end = "\n ----------------------------------------------------------- \n")

## 5) pop() to remove any item from last of list or useing determine the index of item
names.pop() # last item will remove 'khalal'
names.pop(1) # the second will remove 'Trky'
print(names, end = "\n ----------------------------------------------------------- \n")

## 6) sort() to sort the item in list 
names.sort()
print(names, end = "\n ----------------------------------------------------------- \n" )

## 7) len() to determine the length of any item of list
print("the list has ",len(names), "of items")
print("this name has ", len(names[0]), "of Letters")



