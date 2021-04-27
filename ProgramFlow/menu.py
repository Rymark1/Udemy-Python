selection = -1

while selection != 0:
    if selection < 0 or selection > 6:
        print("1. Eat cake")
        print("2. Play Switch")
        print("3. Run a lap")
        print("4. Do Pushups")
        print("5. Take a dump")
        print("6. Live the dream")
        print("0. Exit")
    selection = int(input("Enter selection: "))
    if 0 < selection < 6:
        print("You chose {}.".format(selection))
else:
    print("Goodbye.")