class Shopping:
    cart = []           # class attribute # static attribute
    origin = 'China'

    def __init__(self, name, location):
        self.name = 'Jamuna',          # instance attribute
        self.location = 'Jam er majh khane'

    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f"buying {item} for price: {price} and remaining: {remaining}")

Shopping.purchase(2, 3, 3)

