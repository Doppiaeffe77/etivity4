import mysql.connector

print("Username: ", end="")
usr = input()
print("Password: ", end="")
pwd = input()
print("Database: ", end="")
db = input()
print("Tabella: ", end="")
tb = input()
conn = mysql.connector.connect(user=usr, password=pwd, host='127.0.0.1', database=db)
cursor = conn.cursor()
cursor.execute("DROP TABLE "+tb)
conn.close()