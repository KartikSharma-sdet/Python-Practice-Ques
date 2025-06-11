import Input_Keywords.input as input
import random

# From Jenny's Playlist

def guessTheNumber():

    target = random.randint(1, 50)
    count = 0

    # easy = 10
    # medium = 5
    # hard = 2

    print("Choose the difficulty : 1:'easy'(10 tries), 2:'medium'(5 tries) or '3:hard'(2 tries) ? ")
    inp = input.inputInteger()
    dif = 0

    if inp == 1:
        dif = 10
    elif inp == 2:
        dif = 5
    else :
        dif = 2

    for i in range(dif):
        print("Guess the number between 1 and 50")
        tries = input.inputInteger()
        if tries == target:
            count = 1
            break
        elif tries > target:
            print(f"Try again with a smaller number")
        elif tries < target:
            print(f"Try again with a larger number")

    if count == 0:
        print(f"You failed in guessing the exact number, It was {target}")
    else :
        print(f"You guessed it right, the number was : {target}")

guessTheNumber()