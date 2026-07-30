# base class or common class or parent class
# derived class, child class

class Gadget:
    def __init__(self, brand, price, color, origin):
         self.brand = brand
         self.price = price
         self.color = color
         self.origin = origin

    def run(self):
        pass

        
class Laptop(Gadget):
    def __init__(self, memory, ssd):
        self.memory = memory
        self.ssd = ssd

    def coding(self):
        return f"Learning python and practicing"

class Phone(Gadget):
    def __init__(self, brand, price, color, origin, dual_sim):
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)

    def phone_call(self, number, text):
        return f"Sending SMS to: {number} with: {text}"

    def __repr__(self):
        return f"Brand: {self.brand}, Price: {self.price}, IsDualSim: {self.dual_sim}"

class Camera(Gadget):
    def __init__(self, pixel):
        self.pixel = pixel

    def change_lens(self):
        pass


my_phone = Phone('IPhone', 120000, 'Silver', 'China', True)
print(my_phone)