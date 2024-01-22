from pathlib import Path
import os
myfile = open(Path.home()/Path(os.getcwd(), "file_one.txt"), 'w')
myfile.write("1.Hi Abdurabu\n2.Hi Ahmed\n3.Hi Majid\n4.Hi Mohammed")
# this instruction use to remove anything in file and write the new in it

myfile.writelines("\n5.Hi Saleh\n6.Hi Hussain")
myfile.close()

# if we want to add to file without remove the previous
myfile = open(Path.home()/Path(os.getcwd(), "file_one.txt"), 'a')
myfile.write("\n\nWelcome to my file appending in this we can add string\n to file "
             "without remove the previous")

myfile.close()


