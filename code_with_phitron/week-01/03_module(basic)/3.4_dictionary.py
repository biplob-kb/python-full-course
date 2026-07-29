person = {"name": "Alice", "age": 30, "city": "New York"}
print(person)

print(person["name"])  # Accessing a specific value by its key
print(person["age"])   # Accessing a specific value by its key
print(person["city"])  # Accessing a specific value by its key

person["age"] = 31  # Updating the value of a specific key
print(person)

person["country"] = "USA"  # Adding a new key-value pair to the dictionary
print(person)

print(len(person))  # Getting the length of the dictionary

print(person.keys())  # Getting all the keys in the dictionary
print(person.values())  # Getting all the values in the dictionary
print(person.items())  # Getting all the key-value pairs in the dictionary

for key, value in person.items():
    print(f"{key}: {value}")  # Iterating through the dictionary and printing each key-value pair

