import mysql.connector

print("Username: ", end="")
usr = input()
print("Password: ", end="")
pwd = input()
print("Database: ", end="")
db = input()
conn = mysql.connector.connect(user=usr, password=pwd, host='127.0.0.1', database=db)
cursor = conn.cursor()
print("Tabella: ", end="")
tb = input()
print("Contenuto tabella:\n")
cursor.execute("select * from "+tb)
print(cursor.fetchall())
conn.close()