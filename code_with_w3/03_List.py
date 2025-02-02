#----------------------Declaration--------------------------
# myList = ["apple", "banana", "orange"]
# myList2 = [10, "age", True, False, 20.25]
# myList3 = list(("Apple", "Banana", "Orange"))

# print(myList)
# print(type(myList))
# print(len(myList))
# print(myList2)
# print(myList3)



#------------------------Access List Item-----------------------
myList = ["apple", "orange", "banana", "pineapple", "lichi"]

# print(myList[0])

# myList[0] = "pineapple"
# print(myList)

# print(myList[1])
# print(myList[-1])
# print(myList[0:4])
# print(myList[:4])
# print(myList[1:])
# print(myList[-4:-2])




#---------------------------Change List Item ------------------------
# myList = ["apple", "orange", "banana", "pineapple", "lichi"]

# myList[0] = 4
# print(myList)

# myList[1:4] = "Lemon"
# print(myList)





#--------------------------Add item---------------------------------
# myList = ["apple", "orange", "lemon"]
# print(myList)
# myList.append("pineapple")
# print(myList)

# myList.insert(2, "mango")
# print(myList)

# myList = ["apple", "orange", "lemon"]
# list1 = ["pineapple", "mango"]
# myList.extend(list1)
# print(myList)



#------------------------------Remove List----------------------------
# myList = ["apple", "orange", "lemon", "apple", "pineapple"]

# myList.remove("apple")
# print(myList)
# print(myList)

# print(myList.pop())
# print(myList.pop(1))






#------------------------------Loop Major--------------------------
myList = ["apple", "orange", "lemon", "apple", "pineapple"]

# for st in myList:
#     print(st)


# for i in range(len(myList)):
#     print(myList[i])

# if "apple" in myList:
#     print("Yes")

# [print(x) for x in myList]



#-------------------------------Sort------------------------------
# myList.sort()
# print(myList)


# myList.sort(key=str.lower)
# print(myList)

# myList.reverse()
# print(myList)




#-------------------------------Join----------------------------------
list1 = ["apple", "orange"]
list2 = [2, 4]
list3 = list1 + list2

print(list3)



