x = 100


def add(y):
    z = x + y
    return z


print(add(50))


def print_number():
    global x
    print(x)


print_number()


# to adite on the suround use unlocal
def outer():
    x = 300

    def inner():
        nonlocal x
        x = 100

    inner()
    print(x)


outer()
