name = "Husob Academy"
print(name[3])
# for n in range(len(name)):
#     print(f"{n} the location of {name[n]}")
print(name[-1])
print(len(name))
print("--" * 50)
# funcation using with string 
print(name.capitalize())
print(name.endswith('emy'))
print(name.endswith('ob'))

names = ['Mohammed', 'Ahmed', 'Tawfeek']
sep = ' # '
sep_names = sep.join(names)
print(sep_names)

string = " I am wake up yesterday earlyer then today "
print(' * '.join(string))

coords = 'Coordinates : {latitude}, {longitude}'.format(latitude = '37.24N', longitude = '-115.81W')
print(coords)
print(coords.center(100))
