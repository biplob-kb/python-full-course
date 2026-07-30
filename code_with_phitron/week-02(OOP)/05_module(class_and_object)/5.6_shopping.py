class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def checkout(self, amount):
        total_price = 0
        for item in self.cart:
            total_price += (item['price'] * item['quantity'])
        print(f"Total cost: {total_price} TK")
        print(f"You have given: {amount} TK")

        rest_money = amount - total_price

        if rest_money > 0:
            print(f"Take your rest money: {rest_money} TK")
            print("Thank You")
        elif rest_money < 0:
            print(f"You need to pay more {abs(rest_money)} TK")
        else:
            print("Thank You")


ms_dhoni = Shopping('MS Dhoni')
ms_dhoni.add_to_cart('Rice', 100, 10)
ms_dhoni.add_to_cart('Egg', 120, 12)
ms_dhoni.add_to_cart('Tea', 150, 1)

print(ms_dhoni.cart)
ms_dhoni.checkout(2590)