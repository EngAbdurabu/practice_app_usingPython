task = {'id': 1, 
        'title': "Go to store", 
        'done': True }
print(task, '\n', type(task))

task = dict([('id', 1), ('title', 'Go to store'), ('done', True)])
print(task)
# if the key is sample string we can write as the follwing
task = dict(id = 1, title = "Go to store", done = True)
print(task)
print("++ " * 50)

card = {}
card['id'] = input("Enter the id number: ")
card['name']  = input("Enter your name : ")
card['family'] = ['Mohammed', 'Saleh', 'Abdulla']

card['son'] = {'firs' : 'majid', 'second': "Mohammed"}
card['daliy_plan'] = ('wakup', 'work', 'sleep')
print(card)