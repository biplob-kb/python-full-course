numbers = [10, 20, 30, 12, 14, 25, 35, 45, 55, 65]

highest = max(numbers)
print("The highest number is:", highest)

print(numbers[0])  # Accessing the first element of the list
print(numbers[3])  # Accessing the fourth element of the list
print(numbers[9])  # Accessing the tenth element of the list

print(numbers[-1])  # Accessing the last element of the list
print(numbers[-2])  # Accessing the second-to-last element of the list

print(numbers[2:5])  # Accessing elements from index 2 to 4
print(numbers[:4])   # Accessing elements from the start to index 3
print(numbers[5:10])  # Accessing elements from index 5 to the end

print(numbers[::2])  # Accessing every second element of the list
print(numbers[1:10:2])  # Accessing every second element starting from index 1

numbers[0] = 100  # Modifying the first element of the list
print(numbers)  # Printing the modified list

numbers.append(75)  # Adding a new element to the end of the list
print(numbers)  # Printing the list after appending a new element

numbers.remove(30)  # Removing the element with value 30 from the list
print(numbers)  # Printing the list after removing an element

