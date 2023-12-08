list = []
n = int(input(" write len of your array: "))
a = 0
for i in range(n):
    list.append(int(input("{} write your numbers: ".format(i+1))))
    
i = 1
while i < len(list):
    if list[i] < list[i - 1]:
        a = 1
    i += 1
     
if a :
    print ("list is not sorted.")
else :
    print ("list is sorted.")
