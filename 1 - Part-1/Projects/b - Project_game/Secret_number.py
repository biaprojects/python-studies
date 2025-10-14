import random

import webbrowser
import time

number = random.randint(1, 100)  # de O a 100 está incluso no sorteio

print("What's your name?")
name = input()
print("Hey", name, "Let's start our game to guess the secret number!")

print("What's your first guess? Choose a number from 1 to 100")
guess = int(input())
sum = 1
if guess == number:
    print("Uhuuu! Congrats", name + "!!!")
    print("You guessed the secret number at your first try! (" + str(number) + ")")
else:
    while guess != number:
        print("Ops, you didn't get the secret number...")
        if guess > number:
            print("The secret number is LOWER")
        else:
            print("The secret number is HIGHER")
        print("What's your next guess?")
        guess = int(input())
        sum += 1
    print("Uhuuu! Congrats", name + "!!!")
    print("You guessed the secret number! (" + str(number) + "). You took", sum, "tries.")

# Time of pause in the program (in seconds)
time.sleep(10)

# To open some link in the screen
webbrowser.open('https://media.istockphoto.com/id/1451590744/vector/congratulations-beautiful-greeting-card-poster-banner.jpg?s=612x612&w=0&k=20&c=CD60HIUbZNFGDcVWOfBB90Zjp0weQaFBi5CjetIgRSw=')