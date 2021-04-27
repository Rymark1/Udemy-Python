print("Today is a good day to learn Python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world")

greeting = "Hello"
# name = input("Please enter your name ")
name = "Ryan"

print(greeting + name)
# if we want a space, we can add that too
print(greeting + ' ' + name)

age = 24
print(age)

# python likes to use the term bound or rebound to indicate a value being loaded into a variable.
# This force changes and rebounds the type of the variable.  Below we swap an Int to a String

print(type(greeting))
print(type(age))

age_in_words = "2 Years"
print(type(age))
# this is illegal because there are 2 different data types in this print
# print(name + " is " + age + " years old")

print(name + f" is {age} years old")
print(f"Pi is approximately {22/7:12.50f}")

pi = 22/7
print(f"Pi is approximately {pi:12.50f}")
