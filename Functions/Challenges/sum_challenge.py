def sum_eo(n, t):
    value = 0
    if t.lower() == "e":
        for i in range(2, n-1, 2):
            value += i
    elif t.lower() == "o":
        for i in range(1, n, 2):
            value += i
    else:
        return -1
    return value


print(sum_eo(10, "e"))
print(sum_eo(100, "e"))
print(sum_eo(78, "o"))