def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_text(*args, sep=" ", end="\n", file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end, file=file, flush=flush)


with open ("centered", mode="w") as centered_file:
    # call the function
    # print(python_food())
    center_text("spam and eggs", file=centered_file)
    center_text(12, file=centered_file)
    center_text("spam, spam, and eggs", file=centered_file)
    center_text("spam, spam, spam and eggs", file=centered_file)
    center_text("first", "second", 3, 4, "spam", sep=":", file=centered_file)
print()

print("Hello World")