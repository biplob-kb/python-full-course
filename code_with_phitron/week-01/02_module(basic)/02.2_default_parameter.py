
# def sum(num1, num2, num3=0):
#     return num1 + num2 + num3

# total = sum(5, 10, 15)
# print(total)



# args 
def all_sum(*numbers):
    print(numbers)
    total = 0
    for num in numbers:
        total += num
    return total

total = all_sum(5, 10, 15, 20, 25)
print(total)