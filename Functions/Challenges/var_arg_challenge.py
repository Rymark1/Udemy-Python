def sum_numbers(*args) -> float:
    """
    Accept variable number of `float` variables and sum all numbers passed.

    :param args: Zero or more `float` type arguments
    :return: `float` sum of all arguments passed.
    """

    # This uses the built in function
    # return sum(args)

    # This allows us to iterate over the args tuple
    sum_of_numbers = 0
    for i in args:
        sum_of_numbers += i

    return sum_of_numbers


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
