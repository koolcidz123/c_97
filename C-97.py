import random
Number = random.randint(1,9)

chances = 0

while chances<5:
    Guess = int(input("enter your guess :- "))
    
    if Guess==Number:
        print("You Won :) !")
        break

    elif Guess<Number:
        print("Guess higher than" + str(Guess))

    elif Guess>Number:
        print("Guess lower than" + str1(Guess))
     
    else:
        print("try again")

    chances = chances+1


if not chances<5:
      print("You Lost :( !")