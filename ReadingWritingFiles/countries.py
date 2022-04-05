input_filename = 'country_info.txt'

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
        print(country_dict)

print(countries)