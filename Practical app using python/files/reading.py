from pathlib import Path
import os

Myfile = open(Path.home()/Path(os.getcwd(), "file_one.txt"), "r")
# print(os.getcwd()) # to get current directory
# print(Path(os.getcwd())) # use path for work this one all systems
print(Path().home()) # this return the home file one any system
print(Path.home()/Path(os.getcwd(), "file_one.txt"))

print(Myfile)
print(Myfile.name)
print(Myfile.mode)

# print(Myfile.read()) # to read all file content
# print(Myfile.readline()) # to read one line in the file
# print(Myfile.readlines()) # to read all line in file and put them in array

# how can read only five line ?  => it's easy using loop
lines = Myfile.readlines()
i = 0
for line in lines:
	print(line)
	i+= 1
	if i == 5:
		break


# the important to close the file after work on it
Myfile.close()


