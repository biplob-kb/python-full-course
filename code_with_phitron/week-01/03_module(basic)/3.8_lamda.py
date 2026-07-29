
# def doubled(x):
#     return x * 2

doubled = lambda x: x * 2  # Using a lambda function to double the input value
squared = lambda x: x ** 2  # Using a lambda function to square the input value

result = doubled(4)
print(result) 

result = squared(4)
print(result) 


addition = lambda x, y: x + y  # Using a lambda function to add two numbers
result = addition(3, 5)
print(result)  # Output: 8

res = list(map(lambda x: x * 2, [1, 2, 3, 4, 5]))  # Using a lambda function with map to double each element in the list
print(res)  # Output: [2, 4, 6, 8, 10]


