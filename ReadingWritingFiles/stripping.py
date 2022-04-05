def removeprefix(string: str, prefix: str) -> str:
    if string.startswith(prefix):
        return string[len(prefix)]
    else:
        return string[:] # Return a copy of 'string'.


def removesuffix(string: str, suffix: str) -> str:
    if suffix and string.endswith(suffix): # suffix='' should not call string[:-0]
        return string[:-len(suffix)]
    else:
        return string[:]

filename = 'Jabberywocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()

print(first)

chars = "' Twasebv"
no_apostrophe = first.strip(chars)
print(no_apostrophe)

print("*" * 80)

twas_removed = first.removeprefix("'Twas")
print(twas_removed)
toves_removed = first.removesuffix("toves")
print(toves_removed)

