parrot = "Norwegian Blue"
#         01234567890123
# neg     43210987654321
print(parrot)
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()

print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

print(parrot[0:6])  # Norweg  This is substring which uses 0 as the start index and end - 1 as the last number
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])
print(parrot[10:14])
print(parrot[10:])

print(parrot[:6] + parrot[6:])
print(parrot[:])


print(parrot[-4:-2])
print(parrot[-4:12])

print(parrot[-14:-8])  # Norweg  This is substring which uses 0 as the start index and end - 1 as the last number
print(parrot[-11:-9])
print(parrot[-14:-5])
print(parrot[:-5])
print(parrot[-4:])

print(parrot[0:6:2]) # Nre
print(parrot[0:6:3]) # Nw

number = "9,223;372:036 854,775;807"

print(number[1::4])
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])