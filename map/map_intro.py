import timeit

text = "what have the romans ever done for us"


def a1():
    capitals = [char.upper() for char in text]
 #   print(capitals)
    return capitals


def a2():
    # use map
    map_capitals = list(map(str.upper, text))
 #   print(map_capitals)
    return map_capitals

def a3():
    words = [word.upper() for word in text.split(' ')]
 #   print(words)
    return words

def a4():
    # use map
    map_words = list(map(str.upper, text.split(' ')))
 #   print(map_words)
    return map_words


result1 = timeit.timeit(a1, number=100000)
result2 = timeit.timeit(a2, number=100000)
result3 = timeit.timeit(a3, number=100000)
result4 = timeit.timeit(a4, number=100000)
print(f"A1 = {result1}")
print(f"A2 = {result2}")
print(f"A3 = {result3}")
print(f"A4 = {result4}")
