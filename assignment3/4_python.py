n = int(input("number: "))

for i in range(n):
    if i % 2:
        print("#",end="")
    else:
        print("*",end="")
