small_ints = set(range(21))
print(small_ints)

# small_ints.clear()
# print(small_ints)

small_ints.discard(10)
small_ints.remove(11)
print(small_ints)

small_ints.discard(99)
print(small_ints)

# remove() spits an error if it doesn't exist in the set.
small_ints.remove(99)
print(small_ints)
