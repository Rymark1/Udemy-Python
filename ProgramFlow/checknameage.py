name = input("Enter your name: ")
age = int(input("Enter your age: "))

if 18 <= age < 31:
    print("Welcome to the holiday party, {}".format(name))
else:
    print("Sorry, {}. You are not the right age to be here.".format(name))
