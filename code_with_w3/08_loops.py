
# for i in range(5):
#     print(i)

row = input("Enter the row : ");


for i in range(int(row)):
    for j in range(int(row)):
        if j <=i:
            print("*", end=" ")
    print()

for i in range(int(row)):
    for j in range(int(row)):
        if j<i:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()

for i in range(int(row), -1, -1):
    for j in range(int(row)):
        if j<i:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
print()

for i in range(int(row), -1, -1):
    for j in range(int(row)):
        if i> j:
            print("*", end=" ")
    print()


print()

for i in range(int(row)):
    for j in range(int(row) - i-1):
        print(" ", end=" ")
    
    for k in range(2*i + 1):
        print("*", end=" ")
    print()
        
