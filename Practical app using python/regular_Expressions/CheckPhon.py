# ========================== normal method =====================================
def isPhoneNumber(text):
	if len(text) != 11:
		return False
	for i in range(0, 3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4, 7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8, 11):
		if not text[i].isdecimal():
			return False
	return True

print("is the 773-580-511 phone number ")
print(isPhoneNumber("773-580-511"))

# ============================ regular Expressions methods ==========================
# \d{3}-\d{3}-\d{3}
