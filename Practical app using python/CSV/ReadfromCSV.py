import csv
from pathlib import Path

file = open(Path.home() / Path("OneDrive", "سطح المكتب",
                               "python_practical", "employees_1.csv"))

Reader = csv.reader(file)
# data = list(Reader)
# print(data)

# print(data[1][0])
# print(data[1][1])
# print(data[1][2])

# for row in Reader:
# 	print("Row #" + str(Reader.line_num) + ": " + str(row))

for name in Reader:
	print("{0}:{1}".format(str(Reader.line_num -1 ), str(name[0])))
