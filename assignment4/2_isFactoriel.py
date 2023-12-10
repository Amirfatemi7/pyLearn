number = int(input("write number:"))

i = factorial = 1
while factorial < number:
    i += 1
    factorial *= i

if factorial == number:
    print("your number is factorial")
else:
    print("your number is not factorial")