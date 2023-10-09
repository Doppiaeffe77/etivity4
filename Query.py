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
print("1) Clienti")
print("2) Lista DDT, mittente, numero contratto")
print("3) Lista mittente, DDT, contratto")
print("4) Tipo e numero bancali")
print("5) Numero dipendenti")
print("6) Lista dipendenti")
print("7) Numeri spedizione")
print("8) Attrezzature")
print("9) Veicoli")
print("Scelta: ",end="")
scelta = input()
match scelta:
    case "1":
        rcrc = "SELECT * FROM Cliente ORDER BY Nome ASC"
        cursor.execute(rcrc)
        risultato = cursor.fetchall()
        for row in risultato:
            print("Nome: ", row[0], "   ", "Numero contratto: ", row[1])
        conn.close()
    case "2":
        rcrc = "SELECT Merci.Numero_DDT, Merci.Mittente, Cliente.Numero_contratto AS Nome FROM Merci JOIN Cliente ON Merci.Mittente=Cliente.Nome ORDER BY Merci.Numero_DDT ASC"
        cursor.execute(rcrc)
        risultato = cursor.fetchall()
        for row in risultato:
            print("Numero DDT: ", row[0], "    ", "Nome: ", row[1], "    ", "Numero contratto: ", row[2])
        conn.close()
    case "3":
        rcrc = "SELECT Merci.Mittente, Merci.Numero_DDT, Cliente.Numero_contratto AS Nome FROM Merci JOIN Cliente ON Merci.Mittente=Cliente.Nome ORDER BY Merci.Mittente ASC"
        cursor.execute(rcrc)
        risultato = cursor.fetchall()
        for row in risultato:
            print("Nome: ", row[0], "    ", "Numero DDT: ", row[1], "    ", "Numero contratto: ", row[2])
        conn.close()
    case "4":
        rcrc = "SELECT * FROM Bancali ORDER BY id ASC"
        cursor.execute(rcrc)
        risultato = cursor.fetchall()
        for row in risultato:
            print("Epal: ", row[1], "   ", "Eur: ", row[2], "   ", "Niente marchio: ", row[3])
        conn.close()
    case "5":
        rcrc = "SELECT id, Cognome, Nome FROM Personale ORDER BY id ASC"
        cursor.execute(rcrc)
        risultato = cursor.fetchall()
        for row in risultato:
            print("Numero dipendente: ", row[0], "   ", "Cognome: ", row[1], "   ", "Nome: ", row[2])
        conn.close()
    case "6":
        rcrc = "SELECT Personale.Cognome, Personale.Nome, Personale.Codice_fiscale, Personale.Indirizzo, Personale.Cap, Personale.Citta, Stato.Mansione, Stato.Stipendio, Stato.Operativita FROM Personale JOIN Stato ON Personale.Codice_fiscale=Stato.Codice_fiscale ORDER BY Personale.Cognome ASC"
        cursor.execute(rcrc)
        risultato = cursor.fetchall()
        for row in risultato:
            print("Cognome: ", row[0], "    ", "Nome: ", row[1], "    ", "Codice fiscale: ", row[2], "    ", "Indirizzo: ", row[3], "    ", "Cap: ", row[4], "    ", "Città: ", row[5], "    ", "Mansione: ", row[6], "    ", "Stipendio: ", row[7], "    ", "Operatività: ", row[8])
        conn.close()
    case "7":
        rcrc = "SELECT Ordine.Numero_spedizione, Giro.Nome, Giro.Targa FROM Ordine JOIN Giro ON Ordine.Numero_spedizione=Giro.Numero_spedizione ORDER BY Ordine.Numero_spedizione ASC"
        cursor.execute(rcrc)
        risultato = cursor.fetchall()
        for row in risultato:
            print("Numero spedizione: ", row[0], "    ", "Nome autista: ", row[1], "    ", "Targa veicolo: ", row[2])
        conn.close()
    case "8":
        rcrc = "SELECT Attrezzatura.id, Attrezzatura.Numero, Attrezzatura.Tipo, Attrezzatura_non_disponibile.Numero, Attrezzatura_non_disponibile.Note FROM Attrezzatura JOIN Attrezzatura_non_disponibile ON Attrezzatura.id=Attrezzatura_non_disponibile.id ORDER BY Attrezzatura.id ASC"
        cursor.execute(rcrc)
        risultato = cursor.fetchall()
        for row in risultato:
            print("id: ", row[0], "    ", "Disponibili: ", row[1], "    ", "Tipo: ", row[2], "    ", "Guasti: ", row[3], "    ", "Note: ", row[4])
        conn.close()
    case "9":
        rcrc = "SELECT Veicoli.id, Veicoli.targa, Veicoli.Tipo, Veicoli_non_disponibili.Note FROM Veicoli JOIN Veicoli_non_disponibili ON Veicoli.id=Veicoli_non_disponibili.id ORDER BY Veicoli.id ASC"
        cursor.execute(rcrc)
        risultato = cursor.fetchall()
        for row in risultato:
            print("id: ", row[0], "    ", "Targa: ", row[1], "    ", "Tipo: ", row[2], "    ", "Note: ", row[3])
        conn.close()