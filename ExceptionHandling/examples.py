# x = 8 - 5
# y = x / 0

def factorial(n):
    # n! can also be defined as n * (n-1)!
    """calculates n! recursively"""
    if n <= 1:
        return 1
    else:
        print(n/0)
        return n * factorial(n-1)


try:
    print(factorial(1000))
except RecursionError:
    print("This program can't calculate factorials that large")
except ZeroDivisionError:
    print("What is you doing bby.")

print("Program is terminating")
