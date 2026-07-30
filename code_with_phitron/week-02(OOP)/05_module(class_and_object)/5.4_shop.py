class Shop:
    cart = []
    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)


john_doe = Shop('John Doe')
john_doe.add_to_cart('shoes')
john_doe.add_to_cart('phone')

print(john_doe.cart)

alex = Shop('Alex')
alex.add_to_cart('cap')
alex.add_to_cart('watch')

print(alex.cart)