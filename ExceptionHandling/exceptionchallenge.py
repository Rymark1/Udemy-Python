import sys


def getint():
    while True:
        try:
            number = int(input("Please enter a number"))
            return number
        except EOFError:
            sys.exit(1)
        # except ValueError:
        except:
            print("Invalid number entered.  please try again")
            print("Shut up you stupid ass user.")
        finally:
            print("The finally clause always executes")


a = getint()
b = getint()

try:
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
    sys.exit(2)
else:
    print("Division performed successfully")
