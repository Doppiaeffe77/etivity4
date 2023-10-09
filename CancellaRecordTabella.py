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
        print("Nome da cancellare: ", end="")
        nome = input()
        dlt = "DELETE FROM magazzino WHERE Nome="+nome
        cursor.execute(dlt)
        conn.commit()
    case "cliente":
        print("Nome da cancellare: ", end="")
        nome = input()
        dlt = "DELETE FROM cliente WHERE Nome=" + nome
        cursor.execute(dlt)
        conn.commit()
    case "merci":
        print("Mittente da cancellare: ", end="")
        mittente = input()
        dlt = "DELETE FROM merci WHERE Mittente=" + mittente
        cursor.execute(dlt)
        conn.commit()
    case "personale":
        print("Cognome da cancellare: ", end="")
        cognome = input()
        dlt = "DELETE FROM personale WHERE Cogome=" + cognome
        cursor.execute(dlt)
    case "stato":
        print("codice fiscale da cancellare: ", end="")
        codfisc = input()
        dlt = "DELETE FROM stato WHERE Codice_fiscale=" + codfisc
        cursor.execute(dlt)
    case "bancali":
        print("id da cancellare: ", end="")
        id = input()
        dlt = "DELETE FROM bancali WHERE id=" + id
        cursor.execute(dlt)
    case "ordine":
        print("id da cancellare: ", end="")
        id = input()
        dlt = "DELETE FROM ordine WHERE id=" + id
        cursor.execute(dlt)
    case "giro":
        print("Nome da cancellare: ", end="")
        nome = input()
        dlt = "DELETE FROM giro WHERE Nome=" + nome
        cursor.execute(dlt)
    case "attrezzatura":
        print("id da cancellare: ", end="")
        id = input()
        dlt = "DELETE FROM attrezzatura WHERE id=" + id
        cursor.execute(dlt)
    case "attrezzatura_non_disponibile":
        print("Numero da cancellare: ", end="")
        numero = input()
        dlt = "DELETE FROM attrezzatura_non_disponibile WHERE Numero=" + numero
        cursor.execute(dlt)
    case "veicoli":
        print("id da cancellare: ", end="")
        id = input()
        dlt = "DELETE FROM veicoli WHERE id=" + id
        cursor.execute(dlt)
    case "veicoli_non_disponibili":
        print("Targa da cancellare: ", end="")
        targa = input()
        dlt = "DELETE FROM veicoli_non_disponibili WHERE Targa=" + targa
        cursor.execute(dlt)