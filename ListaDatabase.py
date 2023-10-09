import mysql.connector

print("Username: ", end="")
usr = input()
print("Password: ", end="")
pwd = input()
conn = mysql.connector.connect(user=usr, password=pwd, host='127.0.0.1')
cursor = conn.cursor()
print("Database presenti:\n")
cursor.execute("show databases")
print(cursor.fetchall())
conn.close()