import csv

csv_filename = 'OlympicMedals_2020.csv'

olympic_dict = {}

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    headers = csv_file.readline().strip('\n').split(',')
    print(f"Column headers: {headers}")
    reader = csv.reader(csv_file)
    rank, country, gold, silver, bronze,total = headers
    for row in reader:
        temp_dict = {}
        for i, value in enumerate(row):
            temp_dict[headers[i]] = value
        olympic_dict[row[1]] = temp_dict

print(olympic_dict)
