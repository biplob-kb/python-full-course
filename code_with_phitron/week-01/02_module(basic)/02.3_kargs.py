
def full_name(first, last):
    return f"{first} {last}"

# print(full_name(first="John", last="Doe"))

# name = full_name(last="Doe", first="John")
# print(name)


def famous_name(first, last, **titles):
    full_name = f"{first} {last}"
    if titles:
        full_name += " - " + ", ".join(titles.values())
    return full_name

famous = famous_name("Albert", "Einstein", physicist="Physicist", nobel_laureate="Nobel Laureate")
print(famous)

