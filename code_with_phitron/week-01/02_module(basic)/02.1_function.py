

# def my_func():
#     print("I am a function")
# my_func()


# def double_it(num):
#     result = num * 2
#     print(result)
# double_it(5)

# def add_it(num1, num2):
#     result = num1 + num2
#     print(result)
# add_it(5, 10)


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

leap_year(2020)

