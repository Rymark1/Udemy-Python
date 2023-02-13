def build_tuple(*args):
    return args


def avg_word_length(*args):
    # length = 0
    # word_tuple, = args
    #
    # for word in word_tuple:
    #     if isinstance(word, str):
    #         length += len(word)
    # return length / len(word_tuple)
    temp, = args
    length = len(''.join(temp))
    return length // len(temp)


def small_large(*args):
    small = large = 0
    number_tuple, = args
    small = min(number_tuple)
    large = max(number_tuple)
    return small, large


def reverse_tuple(*args):
    word_tuple, = args
    return word_tuple[::-1]





message_tuple = build_tuple("hello", "planet", "earth", "me", "to", "your", "leader")
print(message_tuple)
print(type(message_tuple))

test_tuple = ("hello", "planet", "earth", "me", "to", "your", "leader")
print(avg_word_length(test_tuple))

test_nbr_tuple = (1, 2, 100, 30, -5)
print(small_large(test_nbr_tuple))

print(reverse_tuple(test_nbr_tuple))

test_list = [1, 2, 3, 4, 5]
print(*test_list)
print(test_list)