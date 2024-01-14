# some idea from my brain
# while True:
#     class Officers:
#         def  __init__(self, id, name, phone_number, address):
#             self.id = id
#             self.name = name
#             self.phone_number = phone_number
#             self.address = address

#     officer = Officers(input("Enter id : "), input("Enter your name : "),
#                     input("Enter phone number : "), input("Enter your address : "))

"""
# this from course 
class Product:
    def __init__(self, id, name, price, count):
        self.id = id
        self.name = name
        self.price = price
        self.count = count

    def discount (self, ratio):
        self.price = self.price - self.price * ratio
    def info(self):
        return f'id: {self.id}, Name: {self.name}, Price: {self.price}$, Count: {self.count}'
iphone_13 = Product (id = 1, name='iPhone 13', price=999, count=10)
samsung_s21 = Product (id=2, name='Samsung Galaxy S20', price=985, count=8)
print (samsung_s21.info())

print (iphone_13.name)
print (samsung_s21.price)    
"""


class Product:
    def __init__(self, id, name, price, count):
        self.id = id
        self.name = name
        self.price = price
        self.count = count

    def discount(self, ratio):
        self.price = self.price - self.price * ratio

    def info(self):
        return f"id: {self.id}, Name: {self.name}, Price: {self.price}$, Count: {self.count}"


iphone_13 = Product(id=1, name="iPhone 13", price=999, count=10)
samusung_s21 = Product(id=1, name="Samsung Galaxy S20", price=985, count=8)
print(
    f"the Product name is : {iphone_13.name} and the price is only : {iphone_13.price}"
)

print(
    f"the Product name is : {samusung_s21.name} and the price is only :{samusung_s21.price}"
)
print(iphone_13.info())
print("-" * 100)


# the exercise of school
class School:
    def __init__(self, classes, student, techers, manger):
        self.classes = int(input("Enter the number of classes:"))
        self.student = int(input("Enter the number of student in this school: "))
        self.techers = int(input("Enter the number of techer in this school: "))
        self.manger = input("who is the manger of this school: ")

    def New_Student(self, address):
        self.name = input("Enter student name: ")
        self.address = input("Enter student address: ")

    def New_techer(self, salary, level):
        self.name = input("Enter techer name: ")
        self.address = input("Enter techer address: ")
        self.salary = input("Enter techer salary:")
        self.level = input("Enter techer degree: ")


# cs_school = School( classes = 20, student = 200, techers = 5 , manger = "shmsan") # type: ignore

print("Welcome to Schools system : ")
x_school = input("Please Enter the school name: ")
print(f"Welcome to {x_school}  school system ")
print(f"Please Enter the inforamtion of {x_school} school ")
x_school = School(classes="", student="", techers="", manger="")

print(
    f"The information you add about {x_school} school :\nThe number of classes is : {x_school.classes}\nThe number of student in this school is : {x_school.student}\nThe number of techers in this school is :{x_school.techers}\nThe manger of this school is : {x_school.manger}"
)

new = input(
    "Did you want add new student or new techer : chose (student) of (techer)"
)
if new.lower() == "student":
    x_school.New_Student(address="")
elif new.lower() == "techer":
    x_school.New_techer(salary="", level="")
else:
    print("you don't chose any option :")
    exit()


# print(f"the number of classes is : {cs_school.classes}")
# # cs_school.New_Student(address = "")
# cs_school.New_techer(salary = "", level = "" )
"""
    class School:
    def __init__(self):
        self.classes = self.get_input("Enter the number of classes: ", int)
        self.students = self.get_input("Enter the number of students: ", int)
        self.teachers = self.get_input("Enter the number of teachers: ", int)
        self.manager = input("Enter the name of the manager: ")

    def get_input(self, prompt, data_type):
        while True:
            try:
                user_input = data_type(input(prompt))
                return user_input
            except ValueError:
                print("Please enter a valid input.")

    def new_student(self):
        name = input("Enter student name: ")
        address = input("Enter student address: ")
        self.students.append({
            "name": name,
            "address": address
        })

    def new_teacher(self):
        name = input("Enter teacher name: ")
        address = input("Enter teacher address: ")
        salary = self.get_input("Enter teacher salary: ", float)
        level = input("Enter teacher degree: ")
        self.teachers.append({
            "name": name,
            "address": address,
            "salary": salary,
            "level": level
        })

    def print_school_info(self):
        print(f"School Information:")
        print(f"Number of classes: {self.classes}")
        print(f"Number of students: {len(self.students)}")
        print(f"Number of teachers: {len(self.teachers)}")
        print(f"School manager: {self.manager}")


school = School()

school.new_student()
school.new_teacher()

school.print_school_info()    
"""
