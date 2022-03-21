numbers = (0, 1, 2, 3, 4, 5)

# the star is unpacking the list or tuple to print.  Can also inverse and pack a bunch of arguments together
print(numbers, sep=";")
print(*numbers, sep=";")
print(0, 1, 2, 3, 4, 5, sep=";")


# The star means we will pack all arguments into a single tuple
def test_star(*args):
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)
print()

test_star()
