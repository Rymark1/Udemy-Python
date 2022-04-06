import json
import urllib.request

json_data_source = "https://www.ncdc.noaa.gov/cag/global/time-series/globe/land_ocean/1/2/1880-2022/data.json"

with urllib.request.urlopen(json_data_source) as json_stream:
    data = json_stream.read().decode('utf-8')
    anomalies = json.loads(data)

print(anomalies['description'])

for year, value in anomalies['data'].items():
    year, value = int(year), float(value)
    print(f'{year} ...{value:6.2f}')
print('*' * 80)
