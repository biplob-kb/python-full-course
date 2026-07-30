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
    def __init__(self, dual_sim):
        self.dual_sim = dual_sim

    def phone_call(self, number, text):
        return f"Sending SMS to: {number} with: {text}"

class Camera(Gadget):
    def __init__(self, pixel):
        self.pixel = pixel

    def change_lens(self):
        pass
        