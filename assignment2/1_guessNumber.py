import random

pcNumber = random.randint(10,100)

for i in range(10):
    if i > 6:
        print('you have {} times !!!!'.format(10-i))
    userNumber = int(input("type your guess:"))

    if pcNumber == userNumber:
        print("* aaaahsaant *")
        print("number of your guess is : {}".format(i+1))
        break
    elif pcNumber > userNumber:
        print("go up")
    elif pcNumber < userNumber:
        print("go down")
