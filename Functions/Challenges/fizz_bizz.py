def fizz_buzz(nbr: int) -> str:
    """
    Pass a number, and the function will determine if:
    1. Function divisible by 3, return fizz
    2. Function divisible by 5, return buzz
    3. Function returns the number as a string if not divisible by 3 or 5
    If divisible by both, return both strings

    :param nbr: `int` passed to test.
    :return: returns a string with either the number or the word
    """

    test_string = ""
    if nbr % 3 == 0:
        test_string = "fizz"
    if nbr % 5 == 0:
        if test_string != "":
            test_string += " "
        test_string += "buzz"
    if test_string == "":
        test_string = str(nbr)
    return test_string


# for i in range(1,101):
#     print(fizz_buzz(i))

input("Play Fizz Buzz.  Press Enter to start")
curr_nbr = 0
max_count = 100

while curr_nbr < max_count:
    curr_nbr += 1
    print(f"Computer's turn: It guessed {fizz_buzz(curr_nbr)}.")
    curr_nbr += 1
    # user_answer = input("Please enter the next item: ")
    user_answer = fizz_buzz(curr_nbr)
    if user_answer.lower().strip() != fizz_buzz(curr_nbr):
        print(f"Sorry.  You lose.  Correct answer was {fizz_buzz(curr_nbr)}")
        break
else:
    print(f"Well done, you reached {curr_nbr}")
