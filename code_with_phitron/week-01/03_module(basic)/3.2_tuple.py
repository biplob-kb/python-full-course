things = "pen", "book", "laptop", "mouse"
print(things)

print(things[0])  # Accessing the first item in the tuple
print(things[1])  # Accessing the second item in the tuple

print(things[0:2])  # Slicing the tuple to get the first two items
print(things[1:3])  # Slicing the tuple to get the second and third items

print(things.index("laptop"))  # Getting the index of an item in the tuple
print(things.count("pen"))  # Counting the occurrences of an item in the tuple

print(len(things))  # Getting the length of the tuple

print(things + ("keyboard", "monitor"))  # Concatenating tuples

print(things * 2)  # Repeating the tuple

print(things[-1])  # Accessing the last item in the tuple
print(things[-2])  # Accessing the second-to-last item in the tuple

for item in things:
    print(item)  # Iterating through the tuple and printing each item

for i in range(len(things)):
    print(things[i])  # Iterating through the tuple using index and printing each item  

#things[0] = "pencil"  # This will raise an error because tuples are immutable in Python



