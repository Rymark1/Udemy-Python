import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts(name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES ('Ryan', 6095551234, '123nospam4m3@gmail.com')")
db.execute("INSERT INTO contacts VALUES('Tim', 123, 'tim@tim.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

#print(cursor.fetchall())
print(cursor.fetchone())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("_" * 20)

cursor.close()
db.commit()
db.close()
