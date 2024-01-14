import re

# use search for search about one thing in string as the first thing
# نستخدم find للبحث عن اول نص اجده مطابق لشروط بحثي في ذالك الانص
text = "AHMED is man work outside "
# use r"" before double quotation to avoid the backslash work in code
search = re.search(r"[a-z]\s", text)
print(search)
print(search.group())
print(search.span())

search = re.search(r"[a-z]\s\s", text)
# if doesn't find anything return none
print(search)


# --------------------------------------------------------
# findall() : use to find all thing in the text and put in the list
# نستخدم findall للبحث عن كل النصوص الموجود في النص التي تطابق شروط بحثي

phone_number = input("Please Enter your number : ")
find = re.findall(r"\d{3}\s\d{3}\s\d{3}", phone_number)
# if not have any match return empty list
print(find)
# --------------------------------------------------------------
# practice example
if find != []:
	print("That is valid number")
else:
	print("That isn't valid number")

