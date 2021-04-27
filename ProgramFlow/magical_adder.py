user_input = input("Please enter 3 numbers with a comma between them: ")

split_numbers = user_input.split(",")
for idx in range(len(split_numbers)):
    split_numbers[idx] = int(split_numbers[idx])

print(int(split_numbers[0] + split_numbers[1] - split_numbers[2]))
