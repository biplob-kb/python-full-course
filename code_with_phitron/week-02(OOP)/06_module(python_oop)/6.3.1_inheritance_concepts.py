# base class or parent class
# class BaseClass:
#     pass

# # derived class

# class DerivedClass(BaseClass):
#     pass


class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def move(self):
        pass

class Bus(Vehicle):
    def __init__(self, name, price, seat):
        self.seat = seat
        super().__init__(name, price)

class Truck(Vehicle):
    def __init__(self, name, price, weight):
        self.weight = weight
        super().__init__(name, price)

class PickUpTruck(Truck):
    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)

class ACBus(Bus):
    def __init__(self, name, price, seat, temperature):
        self.temperature = temperature
        super().__init__(name, price, seat)

    def __repr__(self):
        return f"Name: {self.name}, Price: {self.price}, Seats: {self.seat}, Temperature: {self.temperature}"

green_line = ACBus('Green Line', 5000000, 40, 16)
print(green_line)



