import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
	"https://www.googleapis.com/auth/drive",
	"https://www.googleapis.com/auth/spreadsheets",
]

# key for credential
credentials = ServiceAccountCredentials.from_json_keyfile_name("keys.json", scopes)

# طلب اذن الوصول
file = gspread.authorize(credentials)

new_file = file.open("Example")
worksheet = new_file.worksheet("sheet3")

worksheet.update_cell(9, 2, "=average(B2:B8)" + "%")
worksheet.update_cell(10, 2, "=max(B2:B8)")
worksheet.update_cell(11, 2, "=min(B2:B8)")
worksheet.update_cell(12, 2, "=sum(B2:B8)")

# to know what formula in the cell
cell = worksheet.acell("B9", value_render_option="formula").value
print(cell)

cell = worksheet.acell("B10", value_render_option="formula").value
print(cell)

cell = worksheet.acell("B11", value_render_option="formula").value
print(cell)

cell = worksheet.acell("B12", value_render_option="formula").value
print(cell)

worksheet.format("B9", {
    "backgroundColor": {
      "red": 0.2,
      "green": 0.7,
      "blue": 0.7
    },
    "horizontalAlignment": "CENTER",
    "textFormat": {
      "foregroundColor": {
        "red": 1.0,
        "green": 1.0,
        "blue": 1.0
      },
      "fontSize": 12,
      "bold": True
    }
})