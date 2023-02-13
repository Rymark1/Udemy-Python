def fact(n):
    """Calculate n! iteratively"""
    result = 1
    if n > 1:
        for f in range(2, n+1):
            result *= f
    return result


def fact_recur(n):
    # n! can also be defined as n * (n-1)
    """Calculate n! recursively"""
    if n <= 1:
        return 1
    else:
        return n * fact_recur(n-1)


def fib_recur(n):
    """F(n) = F(n-1) + F(n-2)"""
    if n <= 1:
        return n
    else:
        return fib_recur(n-1) + fib_recur(n-2)


for i in range (130):
    print(i, fact_recur(i))

for i in range (36):
    print(i, fib_recur(i))
