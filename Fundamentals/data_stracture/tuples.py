reviers = ('Euphrates', 'Tigris', 'Jordan River', 'Nile')
print(reviers[1])

# instead tuples
reviers = (('Euphrates', 'Tigris'), ('Jordan River', 'Nile'))
print(reviers[0][0])
print("==" * 50)

# swaping in python using tuples
a = 20 
b = 70
print('a = ', a,'b = ', b)
a, b = b, a
print('a = ', a,'b = ', b)