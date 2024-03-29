import sqlite3
import pytz

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

# for row in db.execute("SELECT * FROM history"):
#     # print(row)
#     utc_time = row[0]
#     local_time = pytz.utc.localize(utc_time).astimezone()
#     print(f"{utc_time}\t{local_time}")

for row in db.execute("SELECT strftime('%m-%d-%Y %H:%M:%f', history.time, 'localtime') AS localtime, history.account, "
                      "history.amount FROM history ORDER BY history.time"):
    print(row)

db.close()