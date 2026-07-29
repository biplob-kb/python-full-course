name = 'Alice'
name2 = "Bob"
name3 = '''Charlie
Charlie's friend
'''

# print(name)
# print(name2)
# print(name3)

# string is a sequence of characters. It can be defined using single quotes, double quotes, or triple quotes. Triple quotes allow for multi-line strings.

# for char in name:
#     print(char)  # Printing each character in the string

print(name[0])  # Accessing the first character of the string
print(name[1])  # Accessing the second character of the string

#name[0] = 'Z'  # This will raise an error because strings are immutable in Python

if 'A' in name:
    print("The letter 'A' is present in the name.")
if 'B' in name2:
    print("The letter 'B' is present in the name2.")
if 'C' in name3:
    print("The letter 'C' is present in the name3.")

print(name.upper())  # Converting the string to uppercase
print(name.lower())  # Converting the string to lowercase   
print(name.replace('A', 'Z'))  # Replacing a character in the string
print(name.split('i'))  # Splitting the string into a list based on a delimiter
print(name.strip())  # Removing leading and trailing whitespace from the string
print(name.startswith('A'))  # Checking if the string starts with a specific character
print(name.endswith('e'))  # Checking if the string ends with a specific character