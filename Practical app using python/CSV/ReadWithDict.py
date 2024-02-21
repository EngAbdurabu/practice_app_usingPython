import csv
from pathlib import Path

file = open(Path.home() / Path("OneDrive", "سطح المكتب",
                               "python_practical", "employees_1.csv"))
ReadDict = csv.DictReader(file)

for row in ReadDict:
	print(row['Name'], row['Salary'], row['Date'])

