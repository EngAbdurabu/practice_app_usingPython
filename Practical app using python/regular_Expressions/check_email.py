import re

def is_Email(email):
	is_email = re.search(r'^[A-z0-9]+[\.-]?[A-z0-9]+@\w+\.\w{2,3}$', email)
	if is_email:
		print(f"The {email} is valid email")
	else:
		print(f"The {email} isn't valid email")


print('Is hsoub.academy@gmail.com a email?')
is_Email('hsoub.academy@gmail.com')
print('Is hsoub.academy@gmail a email?')
is_Email('hsoub.academy@gmail')