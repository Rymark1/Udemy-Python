data = [104, 101, 4, 105, 308, 103, 5, 107,
        100, 306, 106, 102, 108]

min_valid = 100
max_valid = 200

# for i in range(len(data) - 1, -1, -1):
#     if data[i] < min_valid or data[i] > max_valid:
#         print(i, data)
#         del data[i]

top_index = len(data) - 1
for i, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        del data[top_index - i]
        print(top_index - i, value)

print(data)
