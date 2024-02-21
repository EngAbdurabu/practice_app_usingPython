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

# # create file
# new_file = file.create("New Google Sheet")
# # perm_type:means the type of Email, role: means the user validity
# new_file.share('abdu62047@gmail.com', perm_type="user", role='writer')

# open file
new_file = file.open("New Google Sheet")
# create new sheet
# worksheet = new_file.add_worksheet(title="Sheet2", rows=100, cols=20)

# write to sheet
worksheet = new_file.worksheet("Sheet1")
# # this is first method
# worksheet.update("A1", "Hello World!")
# this is second  method
worksheet.update_cell(1, 5, "google sheet ")

# for add more then one information
worksheet.update('A1:C2', [["Ali", "1000$", "20/3/2024"],["Abdurabu", "2000$", "20/2/2024"]])
