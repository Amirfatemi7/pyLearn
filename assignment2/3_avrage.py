
number = 0
sum = 0
while True:
    x = input("write your score or exit to calculate avrage ")

    if x == "exit":
        break
    number += 1
    sum  += float(x)

print("your avrage score : ",sum/number)