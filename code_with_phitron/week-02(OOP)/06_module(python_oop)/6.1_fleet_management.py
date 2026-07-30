class Company:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.buses = []
        self.drivers = []
        self.counters = []
        self.routes = []
        self.managers = []
        self.supervisors = []
        self.fares = []

class Driver:
    def __init__(self, name, license, age):
        self.name = name
        self.license = license
        self.age = age

class Counter:
    def __init__(self):
        pass

class Passenger:
    def __init__(self):
        pass

class Supervisor:
    def __init__(self):
        pass
