import openpyxl
from pathlib import Path

excelfile = openpyxl.load_workbook(Path.home() / Path("OneDrive", "سطح المكتب",
                                                       "python_practical",
                                                       "file.xlsx"))

sheet = excelfile["Sheet1"]

# using formulas
sheet['B8'] = '=SUM(B1:B7)'
sheet['B9'] = '=average(B1:B7)'
sheet['B10'] = '=countif(B1:B7,">=700")'

# saving file in important
excelfile.save(filename=Path.home() / Path("OneDrive", "سطح المكتب",
                                                       "python_practical",
                                                       "file.xlsx"))