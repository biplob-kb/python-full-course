
# def my_func():
#     print("Hello Python")
# my_func()


def name_func(fName, lName):
    fullName = fName + " "+ lName
    print(f'Your Full Name : {fullName}')

fName = input("Enter your first name : ")
lName = input("Enter your last name : ")

name_func(fName, lName)
