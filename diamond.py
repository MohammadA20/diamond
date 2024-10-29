row = int(input("Enter the number of rows: "))

#Nested for loop for half-upper diamond which will increase 2 by each row from 1 to 7
for mhmd in range(row):
    print(" " * (row - mhmd), end = "")
    for adada in range(2 * mhmd + 1):
        print("*", end = "")
    print()
        
#Nested for loop for other half diamond which will decrease 2 by each row from 5 to 1
for mhmd in range(row - 1, 0, -1):
    print(" " * ((row + 1) - mhmd), end = "")
    for adada in range(2 * mhmd - 1):
        print("*", end = "")
    print()