import openpyxl, sys
from pathlib import Path
from openpyxl.styles import Font

if len(sys.argv) == 2:

	try:
		number = int(sys.argv[1])

	except Exception as e:
		print(e)

	excelfile = openpyxl.Workbook()
	sheet = excelfile.active

	for y in range(number + 1):
		for x in range(number + 1):

			# check if in header row or columns
			isHeader = False

			if x == 0 and y == 0:
				isHeader = True
				n = ""
			elif x == 0:
				isHeader = True
				n = y
			elif y == 0:
				isHeader = True
				n = x
			else:
				n = y * x
			cell = sheet.cell(row=y+1, column=x+1)
			if isHeader:
				cell.font = Font(bold=True)
			cell.value = n

	savedfile = str(Path.home()/Path("OneDrive", "سطح المكتب",
               "python_practical")/"multiplaction_Table_") + str(number) + ".xlsx"
	excelfile.save(savedfile)
	print("Saved as " + savedfile)



else:
	print("Please Entre only two arguments ")