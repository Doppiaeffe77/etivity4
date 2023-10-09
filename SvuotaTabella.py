import mysql.connector

print("Username: ", end="")
usr = input()
print("Password: ", end="")
pwd = input()
conn = mysql.connector.connect(user=usr, password=pwd, host='127.0.0.1')
cursor = conn.cursor()
print("Nome database: ",end="")
nome = input()
sql = "use "+nome
cursor.execute(sql)
print("Nome tabella: ",end="")
tabella = input()
match tabella:
    case "magazzino":
        trnct = "TRUNC TABLE magazzino"
        cursor.execute(trnct)
        conn.commit()
    case "cliente":
        trnct = "TRUNCATE TABLE cliente"
        cursor.execute(trnct)
        conn.commit()
    case "merci":
        trnct = "TRUNCATE TABLE merci"
        cursor.execute(trnct)
        conn.commit()
        conn.commit()
    case "personale":
        trnct = "TRUNCATE TABLE personale"
        cursor.execute(trnct)
        conn.commit()
    case "stato":
        trnct = "TRUNCATE TABLE stato"
        cursor.execute(trnct)
        conn.commit()
    case "bancali":
        trnct = "TRUNCATE TABLE bancali"
        cursor.execute(trnct)
        conn.commit()
    case "ordine":
        trnct = "TRUNCATE TABLE ordine"
        cursor.execute(trnct)
        conn.commit()
    case "giro":
        trnct = "TRUNCATE TABLE giro"
        cursor.execute(trnct)
        conn.commit()
    case "attrezzatura":
        trnct = "TRUNCATE TABLE attrezzatura"
        cursor.execute(trnct)
        conn.commit()
    case "attrezzatura_non_disponibile":
        trnct = "TRUNCATE TABLE attrezzatura_non_disponibile"
        cursor.execute(trnct)
        conn.commit()
    case "veicoli":
        trnct = "TRUNCATE TABLE veicoli"
        cursor.execute(trnct)
        conn.commit()
    case "veicoli_non_disponibili":
        trnct = "TRUNCATE TABLE veicoli_non_disponibili"
        cursor.execute(trnct)
        conn.commit()