generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']
new_int_list = []

for item in generated_list:
    if item.isnumeric():
        new_int_list.append(int(item))

print (new_int_list)

for count, item in reversed(list(enumerate(generated_list))):
    if item.isnumeric():
        generated_list.pop(count)
        generated_list.insert(count, int(item))
    else:
        generated_list.pop(count)

print (generated_list)
