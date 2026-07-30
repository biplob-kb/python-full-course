class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid amount for deposit")

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f"You can't withdraw bellow {self.min_withdraw}")
        elif amount > self.max_withdraw:
            print(f"You can't withdraw more than {self.max_withdraw}")
        else:
            self.balance -= amount
            print("Withdraw Done")

brac = Bank(10000)
brac.withdraw(20000)
print(brac.balance)
