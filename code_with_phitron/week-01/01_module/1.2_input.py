# print("Now It is time to taking input")
# age = input("Enter age : ")
# print(age)

# small project on the basis of input output and type casting
my_money = float(input("I have TK : "))
singara_per_price = float(input("How many price of every singara ? "))
quantity = int(input("Give me : "))

total_singara_price = singara_per_price * quantity

print(f"Total price : {total_singara_price} tk")

if total_singara_price > my_money:
    print(f"I have no this money. I have {my_money} tk")
else:
    print("Thank you for the singara")


