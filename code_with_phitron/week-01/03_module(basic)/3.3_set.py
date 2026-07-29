# set is a unique collection of data type in python. It is unordered and unindexed. It is mutable but cannot contain duplicate values.

numbers = {1, 2, 3, 4, 5,3} # no duplicate values will be stored in the set
print(numbers)

numbers.add(6)  # Adding an element to the set
print(numbers)

#numbers[0] = 10  # This will raise an error because sets are unordered and unindexed

numbers.remove(3)  # Removing an element from the set
print(numbers)

if 4 in numbers:
    print("4 is present in the set.")
else:
    print("4 is not present in the set.")

print(len(numbers))  # Getting the length of the set


A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))  # Union of two sets
print(A.intersection(B))  # Intersection of two sets
print(A.difference(B))  # Difference of two sets
print(B.difference(A))  # Difference of two sets


