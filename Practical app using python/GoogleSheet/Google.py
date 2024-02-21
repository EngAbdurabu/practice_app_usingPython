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

# for open file
sheet = file.open("test").sheet1

# for write to sheet "sheet.update_cell(row, column, 'message')"
sheet.update_cell(2, 5, "Welcome to google sheet")


