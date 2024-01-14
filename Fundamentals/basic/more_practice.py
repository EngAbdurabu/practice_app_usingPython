# draw shapes 
# star
# for i in range(0, 11):
#     for j in range(0, i + 1):
#         print("* ", end='')
#     print("\r")
#     for i in range(11, 0, -1):
#         for j in range(0, i + 1):
#             print("* ", end = "")
#         print("\r")
#         #print(f"{i}:", i * "*")

for j in range(1, 6):
    print("*" * j)
for i in range(6, 0, -1):
    print("*" * i )
    
print("-" * 100)

for i in range(1, 11):
    print("\t*" * i)

print("-" * 100)

for i in range(1,6):
    print("\t" * 5 , "*" * i)
