# defined the function and call in the same line 
print((lambda a: a + 2 )(2))

# assinged the lambda function to variable 
add_two = lambda a : a + 2
print(add_two(3))

# defined more then one number 
add = lambda a, b: a + b
print(add(3,5))
print("=" * 40)

student_name = lambda first_name, second_name:f"the name of student is : {first_name.title()}  {second_name.title()}"
print(student_name(first_name = "Majid", second_name = "Abdruabu"))

ids = ['id1', 'id100', 'id2', 'ia22', 'id4', 'id40']
ids.sort(key = lambda x :int(x[2:]))
print(ids)