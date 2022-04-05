input_filename = '../country_info.txt'

countries = {}

with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split("|")
        country, capital, code, code3, dialing, timezone, currency = data
        # print(data)
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name' : country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        countries[country.casefold()] = country_dict
        countries[code.casefold()] = country_dict

while True:
    user_input = input("Please enter a country or a country code to see the capital: ").casefold()
    if user_input in countries:
        if countries[user_input]['capital'] == "":
            print(F"There is no capital of {user_input.title()}\n")
        else:
            print(F"The capital of {user_input.title()} is {countries[user_input]['capital']}.\n")
    elif user_input == 'quit':
        break
    else:
        print("Please enter a valid country.")
