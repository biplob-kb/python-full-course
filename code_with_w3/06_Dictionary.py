

# List => List is a collection which is ordered and changeable and allows duplicate members. ["apple", "orange", "banana"]

# Tuple => Tuple is a collection which is (ordered), (unchangeable) and allows duplicate members. ("apple", "orange", "banana")

# Set = > Set is a collection which is (unordered), (unchangeable), (unindexed) and allows no dulicate members. {"apple", "orange", "banana"}

# Dictionary => Dictionary is a collection which is (ordered), (changeable) and allows no duplicate members. {"brand": "Sony", "model":"Xperia 5"}




#----------------------------------Declaration--------------------------
# myDict = {
#     "brand" : "Sony",
#     "model" : "Xperia 5",
#     "price" : 1212
# }

# print(myDict)
# print(myDict["brand"])

# myDict["price"] = 2000

# print(myDict)





#-----------------------------Access Item-------------------------------------
# myPhone = {
#     "brand" : "Apple",
#     "model" : "Iphone 11",
#     "price" : 35000
# }

# print(myPhone)
# print(myPhone["brand"])
# print(myPhone.keys())
# print(myPhone.values())

# myPhone["price"] = 45000
# print(myPhone)




#---------------------------------Change and Add Item------------------------------
# myPhone = {
#     "brand": "Apple",
#     "model": "Iphone 11",
#     "price": 35000
# }

# print(myPhone)

# myPhone["color"] = "white"
# print(myPhone)

# myPhone.update({"size": "6 inches"})

# print(myPhone)

# myPhone["color"] = "Black"
# print(myPhone)



#------------------------------------Loop in dictionary--------------------------
myPhone = {
    "brand": "Apple",
    "model": "Iphone 11",
    "price": 1210
}

# for x in myPhone:
#     print(x)

# for x in myPhone:
#     print(myPhone[x])

# for k in myPhone.keys():
#     print(k)

# for v in myPhone.values():
#     print(v)


for k, v in myPhone.items():
    print(k, v)