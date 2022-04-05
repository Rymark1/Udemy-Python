# jabber = open('Jabberywocky.txt', 'r')
#
# for line in jabber:
#     print(line.rstrip())
#     # print(line, end="")
#     # print(len(line))
#
# jabber.close()

# with open('Jabberywocky.txt', 'r') as jabber:
#     # for line in jabber:
#     #     print(line.rstrip())
#     lines = jabber.readlines()
#
# print(lines)
# print(lines[-1:])
# for line in reversed(lines):
#     print(line, end="")

# with open ('Jabberywocky.txt') as jabber:
#     text = jabber.read()
#
# print(text)
# for character in reversed(text):
#     print(character, end="")

with open ('Jabberywocky.txt') as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break

print('*' * 80)

with open('Jabberywocky.txt') as jabber:
    for line in jabber:
        print(line.rstrip())
        if 'jubjub' in line.casefold():
            break
