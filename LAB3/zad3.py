from doctest import master


class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property area:{self.area}, rooms:{self.rooms}, price:{self.price}, address:{self.address}\n"


class House(Property):
    def __init__(self, plot):
        self.plot = plot

    def __str__(self):
        return f"House plot:{self.plot}"


class Flat(Property):
    def __init__(self, floor):
        self.floor = floor

    def __str__(self):
        return f"Flat floor:{self.floor}"


house = House(1000)
flat = Flat(3)
print(house)
print(flat)
