import openpyxl
from pathlib import Path

excelfile = openpyxl.load_workbook(Path.home()/Path("OneDrive","سطح المكتب",
                                                    "python_practical", "file.xlsx"))

sheet = excelfile['Sheet1']

# charts
title = openpyxl.chart.Reference(sheet, min_col=1, max_col=1,
                                 min_row=1, max_row=7)
data = openpyxl.chart.Reference(sheet, min_col=2, max_col=2,
                                 min_row=1, max_row=7)
# chart display
# chart = openpyxl.chart.BarChart3D()
chart = openpyxl.chart.DoughnutChart()
chart.title = "My Chart"
# chart.type = "bar"
# chart.style = 11

chart.add_data(data=data)
chart.set_categories(title)

sheet.add_chart(chart, "E8")
# save file
excelfile.save(Path.home()/Path("OneDrive","سطح المكتب",
                                                    "python_practical", "file.xlsx"))
