numbers = [10, 20, 30, 12, 14, 19]

for num in numbers:
    print(num)  # Printing each element of the list
    if num % 2 == 1:
        print(f"{num} is an odd number.")
    else:
        print(f"{num} is an even number.")


for i in range(len(numbers)):
    print(f"Element at index {i} is: {numbers[i]}")  # Accessing elements using index   

odd_numbers = [num for num in numbers if num % 2 == 1]
print("The odd numbers in the list are:", odd_numbers)  # Printing the list of odd numbers

even_numbers = [num for num in numbers if num % 2 == 0]
print("The even numbers in the list are:", even_numbers)  # Printing the list of even numbers

