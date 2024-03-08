list = []

n = int(input(" enter len of your array: "))

for i in range(n):
    list.append(int(input("{} enter your numbers: ".format(i+1))))

print("your list: ",list)
list.reverse()
print("your reversed list: ",list)