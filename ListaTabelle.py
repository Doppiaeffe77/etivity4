import mysql.connector

print("Username: ", end="")
usr = input()
print("Password: ", end="")
pwd = input()
print("Database: ", end="")
db = input()
conn = mysql.connector.connect(user=usr, password=pwd, host='127.0.0.1', database=db)
cursor = conn.cursor()
print("Tabelle presenti:\n")
cursor.execute("show tables")
print(cursor.fetchall())
conn.close()