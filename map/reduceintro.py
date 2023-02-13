import timeit
import functools


def calc_values(x, y: int):
    return x + y


numbers = [2, 3, 5, 8, 13]


def testing_funct():
    reduced_value = functools.reduce(calc_values, numbers)
    return reduced_value


def testing_sum():
    return sum(numbers)


print(timeit.timeit(testing_funct, number=100000))
print(timeit.timeit(testing_sum, number=100000))
