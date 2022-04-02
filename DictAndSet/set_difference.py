from primes_and_squares import squares_generator, primes_generator

evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))
print(evens)
print(odds)

# This is giving a set of all items that appear in both sets
primes = set(primes_generator(100))
print(primes)
squares = set(squares_generator(100))
print(squares)

# This is giving a set of all items that appear in both sets
print(odds.intersection(squares))
print(evens & squares)
even_squares = evens.intersection((squares_generator(100)))
print(even_squares)

# this is giving the odd numbers that are not prime
print(odds.difference(primes))
print(odds - primes)

# this is giving the prime numbers that are not odd
print(primes.difference(odds))
print(primes - odds)
