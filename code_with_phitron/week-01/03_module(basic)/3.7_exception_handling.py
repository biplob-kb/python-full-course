try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("This block will always execute, regardless of whether an exception occurred or not.")

