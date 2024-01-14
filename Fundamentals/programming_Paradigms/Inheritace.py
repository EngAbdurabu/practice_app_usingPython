# try to write the code again to undersand the concept of inheritace
"""
class Product:
    def __init__(self, id, name, price, count):
        self.id = id
        self.name = name
        self._price = price
        self.count = count

    def discount(self, ratio):
        self._price = self._price - self._price * ratio

    def info(self):
        return f"id: {self.id}, Name: {self.name}, Price: {self._price}$, Count: {self.count}"

    def set_price(self, price):
        self._price = price

    def get_price(self):
        return str(self._price) + "$"


class Mobile(Product):
    def __init__(self, id, name, price, count, memory, storage, screen_size):
        super().__init__(id, name, price, count)
        self.memory = memory
        self.storage = storage
        self.screen_size = screen_size

    def specs(self):
        return f'Name: {self.name}, Memory: {self.memory} GB, Storage: {self.storage} GB, Screen Size: {self.screen_size}"'


class Laptop(Product):
    def __init__(self, id, name, price, count, disk_space, cpu, ram, screen_size):
        super().__init__(id, name, price, count)
        self.disk_space = disk_space
        self.cpu = cpu
        self.ram = ram
        self.screen_size = screen_size

    def specs(self):
        return f'Name: {self.name}, Disk Space: {self.disk_space} GB, CPU: {self.cpu}, Ram: {self.ram} GB, Screen Size: {self.screen_size}"'


class Monitor:
    pass


galaxyS21 = Mobile(
    id=3,
    name="Samsung Galaxy S21",
    price=620,
    count=12,
    memory=8,
    storage=128,
    screen_size=6.7,
)
macbookpro2020 = Laptop(
    id=43,
    name="Mac Book Pro",
    price=1200,
    count=5,
    disk_space=256,
    cpu="M1",
    ram=8,
    screen_size=13.3,
)
print(galaxyS21.info())
print(galaxyS21.specs())
print(macbookpro2020.specs())
print(macbookpro2020.info())
"""
