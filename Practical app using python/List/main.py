# employees entry project


employees_name = []
while True:
	print("ادخل اسم الموظف هنا : ", end=" ")
	names = input()

	employees_name.append(names)

	if names == "":
		employees_name.pop()

		break


for i in range(len(employees_name)):
	print(f"اسماء الموظف رقم {i}  : {employees_name[i]}")
