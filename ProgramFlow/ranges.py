for i in range(101,21,-2):
    print("i is now {}".format(i))

for i in range(0,101):
    if i%7 == 0:
        print(i)
        i += 7

for i in range(1, 13):
    for j in range(1, 13):
        print("{0} times {1} is {2}".format(j, i, i*j))
    print("-" * 18)

