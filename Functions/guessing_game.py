import random


def get_integer(prompt, low, high):
    """
    Get an integer from Standard Input (stdin) between low and high.

    The function loops until a valid `int` is entered.

    :param prompt: The String that the user will see when they're prompted to enter the value.
    :param low: An integer that represents the lowest an input `int` can be, inclusive.
    :param high: An integer that represents the highest an input `int` can be, inclusive.
    :return: the integer that the user enters between low and high, inclusive.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            if low <= int(temp) <= high:
                return int(temp)
            print("Please enter a valid number between {} and {}".format(low+1, high))


# print(input.__doc__)
# print ("*" * 80)
# print(get_integer.__doc__)
# print ("*" * 80)
help(get_integer)

highest = 1000
answer = random.randint(1, highest)
guess = 0

print("Please guess number between 1 and {}. Enter 0 to quit: ".format(highest))
while guess != answer:
    guess = get_integer(": ", 0, highest)
    if guess == 0:
        break
    elif guess == answer:
        print("Well done, you guessed it")
        break
    elif guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
