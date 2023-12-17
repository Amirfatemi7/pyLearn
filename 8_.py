

def starSharpPrint(n:int , m:int):
    for i in range(n):
        if i%2 == 0:
            for j in range(m):
                if j%2 == 0:
                    print("#",end="")
                else:
                    print("*",end="")
        else:
            for j in range(m):
                if j%2 == 0:
                    print("*",end="")
                else:
                    print("#",end="")
        print("")

starSharpPrint(5,10)