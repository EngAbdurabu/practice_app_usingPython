import csv
from pathlib import Path

header = ["Name", "Salary", "Date"]
data = [
	["Ahmed", 1000, "12/01/2024"],
	["Saleh", 2000, "14/02/2024"],
	["Mohammed", 2500, "24/02/2024"],
	["Majid", 3000, "10/02/2023"],
	["Abdurabu", 4000, "05/07/1999"]
]
file = open(Path.home() / Path("OneDrive", "سطح المكتب",
                    "python_practical", "employees_1.csv"), 'w', newline='')
# نستخدم newline لكي يعمل لي كل سطر تحت الاخر مباشرة اذا لم اعملة دائماً سوف يعمل لي سطر فارغ

Writer = csv.writer(file)
# Writer.writerow(["Ali", 1000, '22/11/2024']) # to add one line or row
Writer.writerow(header)
Writer.writerows(data) # to add multi line
file.close()

# delimiter and  line-terminator

# file = open(Path.home() / Path("OneDrive", "سطح المكتب",
#                     "python_practical", "employees_1.csv"), 'w', newline='')
# # delimiter is the separate between cell
# # lineterminator is the line between cell
# Writer = csv.writer(file, delimiter='\t', lineterminator='\n---------------\n')
# Writer.writerows(data)
# file.close()
