# # program to add employees using dictionaries

# user greeting
print("Welcome to my programming ")
user = input("Enter your name please: ")
print("Welcome sare : %s" % user)
try:
	employee_num = int(input("Enter the number of employees : "))

	# make loop to enter the employees information
	for emp in range(employee_num):
		employees = {
			'name': input("Enter employee name: ") if emp < employee_num else print(""),
			'age': input("Enter employee age: ") if emp < employee_num else print(""),
			'salary': input("Enter employee salary: ") if emp < employee_num else print(""),
			'skills': input("Enter employee skills as list: ") if emp < employee_num else print("")
		                 }
	# print the information of all employees
		for key, value in employees.items():
			print(f"the employee {key} is: {value}\n".title())
		if employee_num != 0:
			print("\n---------------------Information of the another employee: \n")
except:
	print("check form your Entery, maybe you have Erorr")