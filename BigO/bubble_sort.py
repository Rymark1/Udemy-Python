def bubble_sort(data: list) -> None:
    """Sorts a list in place."""
    n = len(data)
    comparison_count = 0

    for i in range(n - 1):
        swapped = False
        for j in range (n - 1 - i):
            comparison_count += 1
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        print(f"End of pass {i}.  'data' is now {data}")
        if not swapped:
            # All the data is sorted and nothing left to be checked.
            break
    print(f"comparison_count is {comparison_count}")


# numbers = [3, 2, 4, 1, 5, 7, 6]
# numbers = [7, 6, 5, 4, 3, 2, 1]
# numbers = list(range(70, 0 , -1))
numbers = [1, 2, 3, 4, 6, 5, 7]
print(f"Sorting{numbers}")
bubble_sort(numbers)
print(f"The sorted data is {numbers}")

string = "\""


# NO TOUCHING ============================================
from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])

if food == "apple" or "grape":
    print("fruit")
elif food == "bacon" or "steak":
    print("meat")
else:
    print("yuck")


