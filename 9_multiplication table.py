multi = []
def multiplicationTable(n:int , m:int):
    for i in range(1,n+1):
        list = []
        for j in range(1,m+1):
            list.append(i*j)
        multi.append(list)

multiplicationTable(10,10)
for x in multi:
    print(x)
        