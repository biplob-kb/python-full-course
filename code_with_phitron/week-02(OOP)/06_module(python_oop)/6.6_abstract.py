# abstract base class
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod   # enforce all derived class to have a eat method
    def eat(self):
        print("Busy to eat")

    @abstractmethod
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self, name):
        self.category = "Monkey"
        self.name = name
        super().__init__()

    def eat(self):
        print("Busy to eat banana")

    def move(self):
        pass

lucky = Monkey("Lucky")
lucky.eat()