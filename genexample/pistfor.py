print(__file__)

numbers = [1, 2, 3, 4, 5, 6]
squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)

text = "what have the romans ever done for us"

# capitals = [char.upper() for char in text]
capitals = [word.upper() for word in text.split(" ")]

print(capitals)

lc_words = text.split(" ")
print(lc_words)

