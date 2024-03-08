n = int(input('Enter number of row: '))

for i in range(1, n+1):
    for j in range(1,n-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()

for i in range(n-1,0, -1):
    for j in range(1,n-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()