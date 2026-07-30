# encapsulation --> hide details
# access modifier --> public, protected, private

class Bank:
    def __init__(self, holder_name, initial_deposit):
        self.holder_name = holder_name          # public attribute
        self._branch = "Banani Branch"          # protected attribute
        self.__balance = initial_deposit        # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        self.__balance -= amount



alex = Bank("Alex", 10000)
print(alex.holder_name)
print(alex._branch)
alex.deposit(5000)
alex.withdraw(2000)
print(alex.get_balance())


#print(dir(alex))
print(alex._Bank__balance)

