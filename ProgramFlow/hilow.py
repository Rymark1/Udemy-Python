low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1

while low != high:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}.  "
                     "Should I guess higher or lower (H/L/C)"
                     .format(guess)).casefold()
    if high_low == "h":
        # Guess higher.
        low = guess + 1
    elif high_low == "l":
        # guess lower
        high = guess - 1
    elif high_low == "c":
        if guesses == 1:
            print("I got it in {} guess!".format(guesses))
        else:
            print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l, c")
    guesses += 1
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses!".format(guesses))
