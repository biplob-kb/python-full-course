balance = 3000

def buy_item(item, item_price):
    print(f"Buying {item} for {item_price} taka.")
    global balance

    balance -= item_price

buy_item("Laptop", 2500)
print(f"Remaining balance: {balance} taka.")
