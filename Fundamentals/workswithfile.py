# open file and write 
f = open("file.txt", 'w')
f.write("hello pythion\nthis file for work with file ")
f.close()

# read from file
f = open("file.txt", 'r')
print(f.read())
f.close()

# use with to avoid the forget the close the file 
with open("file.txt", 'w') as w:
    w.write("hello python\nI am intersting for develope myself in python")

# copy the element from file to other 
with open("file.txt", 'r') as r, open("file2.txt", 'w') as w:
    f_line = r.read()
    w.write(f_line)

# exercise " take the user fill the file "
user_file = input("Enter summery about yourself: ")
with open("user_file.txt", 'w') as uw:
    uw.write(user_file)
    print("You are write the following \n===============================")
with open("user_file.txt", 'r') as ur:
    print(ur.read())



