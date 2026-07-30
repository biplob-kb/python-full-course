class Shop:
    shopping_mall = 'Jamuna'

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []    # cart is an instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)


alex = Shop('Alex')

alex.add_to_cart('Shoes')
alex.add_to_cart('Phone')

print(alex.cart)

bob = Shop('Bob')
bob.add_to_cart('Watch')
bob.add_to_cart('Cap')
print(bob.cart)