size = int(input("Enter the size of the pattern: "))

row = 0

while row < size:
    # For loop to print stars in a row
    for _ in range(size):
        print("*", end="")
    print()  
    row += 1
