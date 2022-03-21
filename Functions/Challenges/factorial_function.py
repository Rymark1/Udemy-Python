def factorial(nbr: int) -> int:
    """
    Pass an `int` and returns factorial of the number

    :param nbr: number to be factorialed
    :return: factorial of the number
    """
    if nbr == 0:
        return 1

    total_factorial = 1
    for fact_i in range(1, nbr+1):
        total_factorial *= fact_i

    return total_factorial


for i in range(0, 36):
    print(f"{i}\t{factorial(i)}")
