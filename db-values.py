import sqlite3

conn = sqlite3.connect('logins.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM logins")
logins = cursor.fetchall()
print("logins:")
for logins in logins:
    print(logins)
