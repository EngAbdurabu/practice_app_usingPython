import os, csv
from pathlib import Path

os.makedirs(Path.home() / Path("OneDrive", "سطح المكتب",
                    "python_practical", "CSV files"), exist_ok=True)

for csvfilename in os.listdir(Path.home() / Path("OneDrive", "سطح المكتب",
                    "python_practical", "CSV files")):
	if not csvfilename.endswith("csv"):
		continue

	print("Removing header form " + csvfilename + "...")
	csvRows = []
	# Read file
	csvfileObj = open(Path.home() / Path("OneDrive", "سطح المكتب",
                    "python_practical", "CSV files", csvfilename))
	csvfileReader = csv.reader(csvfileObj)

	for row in csvfileReader:
		if csvfileReader.line_num == 1:
			continue

		csvRows.append(row)
	csvfileObj.close()
	# Write file
	csvfileObj = open(Path.home() / Path("OneDrive", "سطح المكتب",
                "python_practical", "CSV files", csvfilename), "w", newline="")
	csvWriter = csv.writer(csvfileObj)
	for row in csvRows:
		csvWriter.writerow(row)
	csvfileObj.close()

