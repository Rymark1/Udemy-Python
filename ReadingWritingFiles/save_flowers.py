data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

# plants_filename = "flowers_print.txt"
#
# with open(plants_filename, "w") as plants:
#     for plant in data:
#         # the file command is telling it to print in a different place.  The default is the terminal, but we can
#         # specify a file
#         print(plant, file=plants)
#
# new_list = []
# with open(plants_filename) as plants:
#     for plant in plants:
#         new_list.append(plant.rstrip())
#
# print(new_list)

# # The write method doesn't do any formatting so we just append everything to the same line.
# plants_filename = "flower_write.txt"
# with open(plants_filename, "w") as plants:
#     for plant in data:
#         plants.write(plant)
#
# print(data)
# string_representation = data.__str__()
# print(type(string_representation))
#
# new_list = []
# with open(plants_filename) as plants:
#     for plant in plants:
#         print(plant)

# the print function grabbed the string representation of each number and put it into the file.  This is why the
# print function can write numbers.
filename = "test_numbers.txt"
with open(filename, "w") as test:
    for i in range(10):
        print(i, file=test)

# The write method is explicit in what it does.  Whatever you send, will be interpreted as it is, and no
# conversions will happen.  It cannot handle anything other than strings
with open(filename, "a") as test:
    for i in range(10):
        test.write(str(i) + "\n")
