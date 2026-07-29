numbers = [10, 20, 30, 12, 14, 25, 35, 45, 55, 65]

length = len(numbers)
print("The length of the list is:", length)

appended_list = numbers + [75, 85, 95]
print("The list after appending new elements is:", appended_list)

for i in range(length):
    print(f"Element at index {i} is: {numbers[i]}")

numbers.sort()
print("The sorted list is:", numbers)

numbers.reverse()
print("The reversed list is:", numbers)

numbers.remove(25)
print("The list after removing 25 is:", numbers)

numbers.insert(2, 22)
print("The list after inserting 22 at index 2 is:", numbers)

numbers.pop()
print("The list after popping the last element is:", numbers)

numbers.clear()
print("The list after clearing all elements is:", numbers)