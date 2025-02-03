
# List => List is a collection which is ordered and changeable and allows duplicate members. ["apple", "orange", "banana"]

# Tuple => Tuple is a collection which is (ordered), (unchangeable) and allows duplicate members. ("apple", "orange", "banana")

# Set = > Set is a collection which is (unordered), (unchangeable), (unindexed) and allows no dulicate members. {"apple", "orange", "banana"}

# Dictionary => Dictionary is a collection which is (ordered), (changeable) and allows no duplicate members. {"brand": "Sony", "model":"Xperia 5"}



#----------------------------Declaration---------------------------------------
# mySet = {"apple", "orange", "banana", "apple"}
# print(mySet)

# mySet2 = {"apple", 2, 10.25, True}
# print(mySet2)




#--------------------------Access set item-------------------------------------
# mySet = {"apple", "orange", "banana"}

# for fruit in mySet:
#     print(fruit)

# print(len(mySet))


# if "apple2" in mySet:
#     print("Yes")
# else:
#     print("No")


# print("banana" not in mySet)
# print("apple" in mySet)



#---------------------------Add set item------------------------
mySet = {"apple", "orange", "banana"}

# mySet.add("mango")
# print(mySet)

anotherSet = {"pineapple", "lichi", "watermelon"}
mySet.update(anotherSet)
print(mySet)