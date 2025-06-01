length = int(input("Enter the size of the pattern: "))
row  = 0
while row < length:
    for i in range(length):
        print("*", end="")
    print("\n")
    row +=1


