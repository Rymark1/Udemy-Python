import random

highest = 10
answer = random.randint(1, highest)
guess = 0

print("Please guess number between 1 and {}. Enter 0 to quit: ".format(highest))
while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    elif guess == answer:
        print("Well done, you guessed it")
        break
    elif guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
