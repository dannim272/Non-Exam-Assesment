import sqlite3

conn = sqlite3.connect('logins.db')
cursor = conn.cursor()

def printAll(conn,cursor):
    cursor.execute("SELECT * FROM logins")
    logins = cursor.fetchall()
    print("logins:")
    for logins in logins:
        print(logins)

def deleteAll(conn,cursor):
    cursor.execute("DELETE FROM logins")
    conn.commit()

# deleteAll(conn,cursor)
# printAll(conn,cursor)
