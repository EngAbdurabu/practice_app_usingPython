import gspread, re
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
	"https://www.googleapis.com/auth/drive",
	"https://www.googleapis.com/auth/spreadsheets",
]

# key for credential
credentials = ServiceAccountCredentials.from_json_keyfile_name("keys.json", scopes)

# طلب اذن الوصول
file = gspread.authorize(credentials)

# open file
sheet = file.open("Example").sheet1 # means active sheet

# find
cell = sheet.find("Abdurabu") # to find the first one
print(cell)
print("Found something in Row: %s and in Column:  %s" % (cell.row, cell.col))

cell = sheet.findall("Abdurabu") # to find all in this file
print(cell)

# find using regular expression
name = re.compile("Abdurabu|Majid")
cell = sheet.findall(name)
print(cell)

# clear
# to remove specific cell or data
sheet.batch_clear(["A9:C9"])

# to remove all
sheet.clear()
