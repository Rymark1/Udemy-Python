split_string = "This string has been\nsplit over\nseveeral\nlines"
print(split_string)

tabbed_string = "1\t2\t3\t4\t5"
print(tabbed_string)

print('The pet show owner said "No, no, \'e\'s uh,...he\'s resting".')
#or
print("the pet shop owner said \"No, no, 'e's uh,...he's resting\".")
#or
print("""The pet shop owner said "No, no, \
'e's uh,...he's resting".""")

# triple quotes allow anything to print within them.  We can have it include line breaks like below.  If there is a \, it cancels the line break.
another_split_string = """This string has been \
split over \
several 
lines"""
print(another_split_string)

#the 'r' arguement in the print function means raw string.  This outputs exactly what is in quotes and ignores the escape characters.
print("C:\\Users\\rmark\\notes.txt")
print(r"C:\Users\rmark\notes.txt")