d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

new_dict = dict.fromkeys(pantry_items)
print(new_dict)

keys = d.keys()
print(keys)

d2 = {
    7: "lucky seven",
    10: "ten",
    3: "this is the new three"
}

d.update(d2)
for key, value in d.items():
    print(key,value)

d.update(enumerate(pantry_items))
for key, value in d.items():
    print(key, value)