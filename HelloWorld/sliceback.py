letters = "abcdefghijklmnopqrstuvwxyz"
#          01234567890123456789012345
backwards = letters[25::-1]
print(backwards)

print(letters[16:13:-1])
print(letters[4::-1])
print(letters[:17:-1])
print(letters[:-9:-1])

print(letters[-4:]) # useful to prevent out of bound errors
print(letters[-1:]) # useful to prevent out of bound errors
print(letters[:1])  # useful to prevent out of bound errors

