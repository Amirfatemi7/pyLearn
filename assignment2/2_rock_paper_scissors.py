import random

userScore = 0
pcScore = 0
times = 0
# for i in range(times):
while abs(userScore - pcScore) < 2 or times <3:
    times +=1
    x = random.randint(1,3)

    if x ==1:
        pcChoice = "rock"
    elif x== 2:
        pcChoice = "paper"
    elif x== 3:
        pcChoice = "scissors"

    userChoice = input("which one?!  rock or paper or scissors ")

    print("computer :",pcChoice)
    print("user :",userChoice)
   
    if pcChoice == "rock" and userChoice == "paper":
        userScore +=1
    elif pcChoice == "rock" and userChoice == "scissors":
        pcScore +=1
    elif pcChoice == "paper" and userChoice == "scissors":
        userScore +=1
    elif pcChoice == "paper" and userChoice == "rock":
        pcScore +=1
    elif pcChoice == "scissors" and userChoice == "rock":
        userScore +=1
    elif pcChoice == "scissors" and userChoice == "paper":
        pcScore +=1
    print("computer score :",pcScore)
    print("your score :",userScore)
    if times >=3:
        if userScore == pcScore:
            print("you are the same score ",pcScore)
            
if userScore>pcScore:
    print("you are win")
    print("computer score :",pcScore)
    print("your score :",userScore)
else:
    print("computer win")
    print("computer score :",pcScore)
    print("your score :",userScore)


