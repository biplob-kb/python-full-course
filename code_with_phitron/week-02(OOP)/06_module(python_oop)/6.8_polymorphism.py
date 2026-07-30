# poly --> many
# morph --> shape

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("animal making some sound")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print("meow meow")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("gheu gheu")

don = Cat("Real Don")
don.make_sound()

shepard = Dog("Local Shepard")
shepard.make_sound()