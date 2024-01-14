import sys

# to know what the system is 
print(sys.platform)

if sys.platform.startswith("Linux"):
    print("your system is Linux")
elif sys.platform.startswith("win32"):
    print("your system is windows")
elif sys.platform.startswith("darwin"):
    print("your system is MacOs")

# to know the version of python 
print(sys.version)

if sys.version.startswith('3.10'):
    print("your version is old")
elif sys.version.startswith('3.11'):
    print("your version is good")

print(sys.getwindowsversion())
print("=" * 40)
# ============================================================================
import os

# to get the current directory
print(os.getcwd())
print("-" * 10)
# to chage my dicrectory
os.chdir("fundamentals")
print(os.getcwd())
print("-" * 10)
os.chdir("python_library")
print(os.getcwd())
print("-" * 10)
os.chdir("..")
print(os.getcwd())
print("-" * 10)
# to show the subfoldor in this foldor 
print(os.listdir())
print("-" * 10)
content = os.scandir()
for item in content:
    print(item.name)

print("-" * 10)
# to show the foldor only 
for item in content:
    if item.is_file():
        print(item.name)

# to make folder or dirctory
# if the folder exit we back error 
# try:
#     os.mkdir("Abdurabu")
# except FileExistsError as error:
#     print(error)

# #  to create the dirctor in the dirctor
# os.makedirs("Abdurabu/Majid")

# # to rename the folder 
# os.rename("Abdurabu", "Abumajid")

# # to remove empty folder
# os.rmdir("Abumajid\\Majid")
# os.rmdir("Abumajid")
# ============================================================================
import shutil

# # to remove dirctory not empty
# shutil.rmtree("Abdurabu")

# to copy file without information of it
shutil.copy("file.txt", "python_library")
# to copy file with information of it 
shutil.copy2("file2.txt", "python_library")

# # to move folder or file from place to another 
# shutil.move("python_library/random_math_decimal.py", "random_math_decimal.py")
# shutil.move("random_math_decimal.py", "python_library")