import mysql.connector

print("Username: ", end="")
usr = input()
print("Password: ", end="")
pwd = input()
conn = mysql.connector.connect(user=usr, password=pwd, host='127.0.0.1')
cursor = conn.cursor()
print("Nome nuovo database: ", end="")
nome = input()
sql = "create database " + nome
cursor.execute(sql)
conn.close()
