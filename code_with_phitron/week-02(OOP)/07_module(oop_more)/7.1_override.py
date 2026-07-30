class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("Vat mangso polau korma")

    def exercise(self):
        raise NotImplementedError



class Cricketer(Person):
    def __init__(self, name, age, height, weight, team):
        self.team = team
        super().__init__(name, age, height, weight)

    # override
    def eat(self):
        print("Vegetables")

    def exercise(self):
        print("Gym a poisa diya gham jhorai")

sakib = Cricketer("Sakib Al Hasan", 38, 6, 70, 'Bangladesh')
sakib.eat()
sakib.exercise()

# + sign overriding
print(30 + 15)
print("Sakib" + "Rakib")
print([12, 14] + [13, 10])