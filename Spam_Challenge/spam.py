menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for breakfast in menu:
    for item in breakfast:
        if item != 'spam':
            print(item, end=", ")
    print()

for breakfast in menu:
    for item in reversed(breakfast):
        if item == 'spam':
            breakfast.remove(item)
    print(breakfast)

print()