import re

number = "123-456-7890"
# for use groups put bracket in the regular Expression
search = re.search(r"(\d{3})-(\d{3})-(\d{3})", number)
print(search.group())
print(search.group(1))
print(search.group(2))
print(search.group(3))

print("===========================================================")

date = "14-01-2024"
search = re.search(r"(\d{2})-(\d{2})-(\d{4})", date)
day, month, year = search.groups()
print(f"The day is {day}, month is {month} and year is {year} ")

print("===========================================================")

# my idea
phone_number = input("Please enter the phone number: ")
number = re.search(r"(\d{3})(\d{3})(\d{3})", phone_number)
print(number.group(1),number.group(2), number.group(3))



