import random

wordsBank = ["tree","book","blue","train","fish","woman","life","iran","car","computer"]

goodChars = []
badChars = []

x = random.randint(0,len(wordsBank)-1)

word = wordsBank[x]
userMistakes = 0
while userMistakes < 6:
    
    a = 0
    for i in range(len(word)):
        if word[i].lower() in goodChars or word[i].upper() in goodChars:
            print(word[i],end="")
            a += 1
        else:
            print("-",end="")
    print("  ",a)
    if a == len(word):
        print("you win ✌️")
        break

    userChar =  input("   please write your guess: ")
    if len(userChar) == 1:
        if userChar.lower() in word or userChar.upper() in word:
            goodChars.append(userChar)
            print("👍")
        else:
            badChars.append(userChar)
            userMistakes += 1
            print("👎")
    else:
        print("write correctly . . .")

if userMistakes == 6:
    print("Game Over ☠️")