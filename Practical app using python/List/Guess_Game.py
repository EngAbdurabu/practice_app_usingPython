import random

# ====================== teacher code =======================================
# user greeting
name = input("What's your name ? ")
print(f"Good luck {name}")
# make list and take computer choices
names = ["ahemd", "saleh", "salem", "mohammed"]
word = random.choice(names)

print("The name is : ")

guesses = ''

trun = 12

while trun > 0:
	failed = 0
	for char in word:

		if char in guesses:
			print(char, end=" ")
		else:
			print("-", end=" ")
			failed += 1
	if failed == 0:
		print()
		print("🏆you win🏆")
		print("The name is " + word)
		break
	print()
	guess = input("Enter the litter of guess: ")
	guesses += guess

	if guess not in word:
		trun -= 1
		print("wrong guesses ")
		print(f"You have only {trun} attempt ")

	if trun == 0:
		print("Yor are loose ")




# ======================== my code  =======================================




