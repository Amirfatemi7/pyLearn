print("------------------------------------------")
fName = input('write your first name:')
lName = input('write your last name:')
a = float(input('Enter first score: '))
b = float(input('Enter second score: '))
c = float(input('Enter third score: '))

avg = (a+b+c)/3

print(" avrage of "+fName+" "+lName+ "'s scores")
if avg >= 17:
    print("Great")
elif avg <17 and avg>=12:
    print("Normal")
else:
    print("Fail !!!!!!!!!!!!!!")