
# List => List is a collection which is ordered and changeable and allows duplicate members. ["apple", "orange", "banana"]

# Tuple => Tuple is a collection which is (ordered), (unchangeable) and allows duplicate members. ("apple", "orange", "banana")

# Set = > Set is a collection which is (unordered), (unchangeable), (unindexed) and allows no dulicate members. {"apple", "orange", "banana"}

# Dictionary => Dictionary is a collection which is (ordered), (changeable) and allows no duplicate members. {"brand": "Sony", "model":"Xperia 5"}


#---------------------------Declaration-----------------------------------
# myTuple = ("apple", "orang", "banana")
# myTuple2 = ("apple", 2, 10.25, True, "apple")
# print(myTuple)
# print(type(myTuple))
# print(len(myTuple))

# print(myTuple2)



#----------------------Access Tuple------------------------------------
# myTuple = ("apple", "orange", "banana", "lichi", "mango")

# print(myTuple[0])
# print(myTuple[1:4])

# for c in myTuple:
#     print(c)


# for i in range(len(myTuple)):
#     print(myTuple[i])



# if "apple" in myTuple:
#     print("Yes")
# else:
#     print("No")



#------------------------ Update Tuples--------------------------
myTuple = ("apple", "orange", "banana", "lichi", "mango")

# myTuple[0] = "pineapple"
# print(myTuple)

list1 = list(myTuple)
list1[0] = "pineapple"
myTuple = tuple(list1)
print(myTuple)


# to update or add  tuple information firstly we need to convert the tuple into list then after changing again we need to convert it into tuple





