import csv

input_filename = '../country_info.txt'

dialect = csv.excel
dialect.delimiter = "|"

countries = {}

with open(input_filename, encoding='utf-8', newline='') as country_file:
    # get the columns from the first line of the file.
    headings = country_file.readline().strip('/n').split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()

    reader = csv.DictReader(country_file, dialect=dialect, fieldnames=headings)
    for row in reader:
        countries[row['country'].casefold()] = row
        countries[row['cc'].casefold()] = row

while True:
    user_input = input("Please enter a country or a country code to see the capital: ").casefold()
    if user_input in countries:
        if countries[user_input]['capital'] == "":
            print(F"There is no capital of {user_input.title()}\n")
        else:
            print(F"The capital of {user_input.title()} is {countries[user_input]['capital']}.\n")
    elif user_input.casefold() == 'quit':
        break
    else:
        print("Please enter a valid country.")
