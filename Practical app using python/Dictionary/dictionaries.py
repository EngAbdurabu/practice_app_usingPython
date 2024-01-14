# know birthday
birthday = {
	'Ahmed': "May 5",
	'Saleh': "Seb 4",
	'Abdurabu': "Api 5"
            }
while True:
	name = input("Enter your name (or press Enter to stop): ").title()
	if name == "":
		break

	if name in birthday:
		print(f"{birthday[name]} is the birthday of {name}")
	else:
		print(" I don't know your birthday.")
		bday = input("if you want add your birthday Enter here: ")
		birthday[name] = bday
		print("Birthday Dataset Update.")