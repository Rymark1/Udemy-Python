day = "Friday"
temperature = 30
raining = False

if (day == "Saturday" and temperature > 27) or not raining:
    print("Go swimming")
else:
    print("Learn Python")


if 0:
    print("true")
else:
    print("false")

name = input("Please Enter your name: ")
#if name:
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")

