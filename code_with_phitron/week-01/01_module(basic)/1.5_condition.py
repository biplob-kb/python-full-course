# a = 7
# if a > 5:
#     print("a is greater than 5")




# a = int(input("Enter a number: "))
# if a > 0:
#     print("The number is positive.")
# else:
#     print("The number is not positive.")



year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")