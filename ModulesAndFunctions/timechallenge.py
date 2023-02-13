import datetime
import pytz
import random

countries = {}

for i in range(90):
    if i == 0:
        countries[i] = "Exit"
    else:
        countries[i] = random.choice(pytz.all_timezones)

x = 10
while x != 0:
    for x in countries:
        print(f"{x}: {countries[x]}")
    x = input("Please choose a time zone: ")
    x = int(x)
    if x == 0:
        pass
    elif x in countries:
        test = pytz.timezone(countries[x])
        local_time = datetime.datetime.now(tz=test)
        utc_time = datetime.datetime.now(datetime.timezone.utc)
        print(f"\nLocal time is + {local_time}")
        print(f"UTC time is + {utc_time}\n")
