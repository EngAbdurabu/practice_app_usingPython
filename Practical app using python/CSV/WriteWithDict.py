import csv
from pathlib import Path

# file = open(Path.home() / Path("OneDrive", "سطح المكتب",
#                     "python_practical", "employees_1.csv"), 'a', newline='')
#
# WriteDict = csv.DictWriter(file, ["Name", "Salary", "Date"])
# WriteDict.writerow({"Name":"Ali", "Salary":"1500", "Date":"02/01/2021"})
# file.close()

# if you determine the file not exist
# this will create new one in the same path and the name
file = open(Path.home() / Path("OneDrive", "سطح المكتب",
                    "python_practical", "employees_test.csv"), 'w', newline='')

Writer = csv.DictWriter(file, ["Name", "Salary", "Date"])
Writer.writeheader()
Writer.writerow({"Name": "Saleh", "Salary": 1200, "Date":"10/02/2024"})
file.close()