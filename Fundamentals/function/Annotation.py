class MyType:
    def __len__(self):
        """ this for make funcation use len as str,list,set..."""
        return 1000
    
mytype = MyType()
print(len(mytype))

    
# the -> float means what type the funcation must be return  
def duplicate(value:float) -> float:
    return value * 2

print(duplicate(7))