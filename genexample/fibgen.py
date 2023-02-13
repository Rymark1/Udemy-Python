def fibinacci():
    current, previous = 0, 1
    while True:
        current, previous = current + previous, current
        yield current


fib = fibinacci()

for i in range(21):
    print(next(fib))
