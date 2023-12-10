list = []

n = int(input(" enter len of your array: "))

for i in range(n):
    list.append(int(input("{} enter your numbers: ".format(i+1))))

print("your list: ",list)

list2 = []
for x in list:
    if x not in list2:
        list2.append(x) 

print("deleted duplicate list",list2)