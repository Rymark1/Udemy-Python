import shelve

print(dir())
# print(dir(__builtins__))
# for m in dir(__builtins__):
#     print(m)

print()
print(dir(shelve))

for obj in dir(shelve.Shelf):
    if obj[0] != "_":
        print(obj)

help(shelve)
