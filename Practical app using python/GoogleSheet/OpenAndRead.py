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

# sheet = file.open("Example")

# open using another methods " url"
sheet = file.open_by_url("https://docs.google.com/spreadsheets/d/13kWIORtfYUoTS6OWyI0GmVc2cMA-f1CVIQ3JfYqrOSA/edit?usp=drive_link")

# determine the worksheet
# worksheet = sheet.get_worksheet(0) # 1) by index
worksheet = sheet.worksheet("sheet3") # 2) by name

# for known the name of worksheet
worksheetlist = sheet.worksheets()
print(worksheetlist)


# read form sheet
val = worksheet.acell("B2").value
print(val)

val = worksheet.acell("A5").value
print(val)

# worksheet.cell(row, column)
val = worksheet.cell(5, 3).value
print(val)

# for read whole row or column
value_list = worksheet.row_values(3)
print(value_list)

name_list = worksheet.col_values(1)
print(name_list)

# to get all values in file
list_of_list = worksheet.get_all_values()
print(list_of_list)

list_of_list = worksheet.get_all_records()
print(list_of_list)