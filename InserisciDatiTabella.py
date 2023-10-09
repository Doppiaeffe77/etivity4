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
        trnct = "TRUNCATE TABLE magazzino"
        cursor.execute(trnct)
        conn.commit()
        ins1 = "INSERT INTO magazzino (Partita_iva, Nome, Indirizzo, Cap, Citta) VALUES ('01234567890', 'Trasporti SCARL', 'Via dei Matti 0', '16641', 'Paperopoli')"
        cursor.execute(ins1)
        conn.commit()
    case "cliente":
        trnct = "TRUNCATE TABLE cliente"
        cursor.execute(trnct)
        conn.commit()
        ins1 = "INSERT INTO cliente (Nome, Numero_contratto) VALUES ('Finesso', '1')"
        cursor.execute(ins1)
        conn.commit()
        ins2 = "INSERT INTO cliente (Nome, Numero_contratto) VALUES ('Mogway', '2')"
        cursor.execute(ins2)
        conn.commit()
        ins3 = "INSERT INTO cliente (Nome, Numero_contratto) VALUES ('Aiazzone', '3')"
        cursor.execute(ins3)
        conn.commit()
        ins4 = "INSERT INTO cliente (Nome, Numero_contratto) VALUES ('Chimera', '4')"
        cursor.execute(ins4)
        conn.commit().connect()
    case "merci":
        trnct = "TRUNCATE TABLE merci"
        cursor.execute(trnct)
        conn.commit()
        ins1 = "INSERT INTO merci (Mittente, Numero_DDT) VALUES ('Finesso', '1')"
        cursor.execute(ins1)
        conn.commit()
        ins2 = "INSERT INTO merci (Mittente, Numero_DDT) VALUES ('Mogway', '2')"
        cursor.execute(ins2)
        conn.commit()
        ins3 = "INSERT INTO merci (Mittente, Numero_DDT) VALUES ('Aiazzone', '3')"
        cursor.execute(ins3)
        conn.commit()
        ins4 = "INSERT INTO merci (Mittente, Numero_DDT) VALUES ('Chimera', '4')"
        cursor.execute(ins4)
        conn.commit()
    case "personale":
        trnct = "TRUNCATE TABLE personale"
        cursor.execute(trnct)
        conn.commit()
        ins1 = "INSERT INTO personale (id, Codice_fiscale, Cognome, Nome, Indirizzo, Cap, Citta) VALUES ('1', 'plnppr34p09d969u', 'Paolino', 'Paperino', 'Via della Sfortuna 13', '03130', 'Paperopoli')"
        cursor.execute(ins1)
        conn.commit()
        ins2 = "INSERT INTO personale (id, Codice_fiscale, Cognome, Nome, Indirizzo, Cap, Citta) VALUES ('2', 'pllpnc55f04a969u', 'Pallino', 'Pinco', 'Piazza la Bomba e Scappa, 4', '03130', 'Paperopoli')"
        cursor.execute(ins2)
        conn.commit()
        ins3 = "INSERT INTO personale (id, Codice_fiscale, Cognome, Nome, Indirizzo, Cap, Citta) VALUES ('3', 'pltplt40q31a969u', 'Plutozzi', 'Pluto', 'Corso un Rischio 1', '03130', 'Paperopoli')"
        cursor.execute(ins3)
        ins4 = "INSERT INTO personale (id, Codice_fiscale, Cognome, Nome, Indirizzo, Cap, Citta) VALUES ('4', 'cltrsa70t12c969u', 'Culetto', 'Rosa', 'Via da Lì 7', '03130', 'Paperopoli')"
        cursor.execute(ins4)
        ins5 = "INSERT INTO personale (id, Codice_fiscale, Cognome, Nome, Indirizzo, Cap, Citta) VALUES ('5', 'clmpsq45v25a969u', 'Colomba', 'Pasquale', 'Scalinata in Discesa 41', '03130', 'Paperopoli')"
        cursor.execute(ins5)
        conn.commit()
        ins6 = "INSERT INTO personale (id, Codice_fiscale, Cognome, Nome, Indirizzo, Cap, Citta) VALUES ('6', 'lmpdri50g07f969u', 'Lampa', 'Dario', 'Viale Illuminato 4', '03130', 'Paperopoli')"
        cursor.execute(ins6)
        conn.commit()
        ins7 = "INSERT INTO personale (id, Codice_fiscale, Cognome, Nome, Indirizzo, Cap, Citta) VALUES ('7', 'rmeglt65z17h969u','Romeo', 'Giulietta', 'Via della Balconata 1', '03130', 'Paperopoli')"
        cursor.execute(ins7)
        ins8 = "INSERT INTO personale (id, Codice_fiscale, Cognome, Nome, Indirizzo, Cap, Citta) VALUES ('8', 'sntntl58s25j969u','Santo', 'Natale', 'Via della Mangiatoia 8', '03130', 'Paperopoli')"
        cursor.execute(ins8)
        conn.commit()
    case "stato":
        trnct = "TRUNCATE TABLE stato"
        cursor.execute(trnct)
        conn.commit()
        ins1 = "INSERT INTO stato (Codice_fiscale, Mansione, Stipendio, Operativita) VALUES ('plnppr34p09d969u', 'magazziniere', '13.80', 'in servizio')"
        cursor.execute(ins1)
        conn.commit()
        ins2 = "INSERT INTO stato (Codice_fiscale, Mansione, Stipendio, Operativita) VALUES ('pllpnc55f04a969u', 'autista', '15.00', 'in servizio')"
        cursor.execute(ins2)
        conn.commit()
        ins3 = "INSERT INTO stato (Codice_fiscale, Mansione, Stipendio, Operativita) VALUES ('pltplt40q31a969u', 'magazziniere', '13.80', 'ferie')"
        cursor.execute(ins3)
        ins4 = "INSERT INTO stato (Codice_fiscale, Mansione, Stipendio, Operativita) VALUES ('cltrsa70t12c969u', 'impiegato', '17.50', 'in servizio')"
        cursor.execute(ins4)
        ins5 = "INSERT INTO stato (Codice_fiscale, Mansione, Stipendio, Operativita) VALUES ('clmpsq45v25a969u', 'magazziniere', '13.80', 'in servizio')"
        cursor.execute(ins5)
        conn.commit()
        ins6 = "INSERT INTO stato (Codice_fiscale, Mansione, Stipendio, Operativita) VALUES ('lmpdri50g07f969u', 'magazziniere', '13.80', 'in servizio')"
        cursor.execute(ins6)
        conn.commit()
        ins7 = "INSERT INTO stato (Codice_fiscale, Mansione, Stipendio, Operativita) VALUES ('rmeglt65z17h969u', 'impiegato', '17.50', 'in servizio')"
        cursor.execute(ins7)
        ins8 = "INSERT INTO stato (Codice_fiscale, Mansione, Stipendio, Operativita) VALUES ('sntntl58s25j969u', 'autista', '15.00', 'in servizio')"
        cursor.execute(ins8)
        conn.commit()
    case "bancali":
        trnct = "TRUNCATE TABLE bancali"
        cursor.execute(trnct)
        conn.commit()
        ins1 = "INSERT INTO bancali (id, Epal, Eur, Niente) VALUES ('1', '20', '10', '10')"
        cursor.execute(ins1)
        conn.commit()
    case "ordine":
        trnct = "TRUNCATE TABLE ordine"
        cursor.execute(trnct)
        conn.commit()
        ins1 = "INSERT INTO ordine (id, Numero_spedizione) VALUES ('1', '104')"
        cursor.execute(ins1)
        conn.commit()
        ins2 = "INSERT INTO ordine (id, Numero_spedizione) VALUES ('2', '222')"
        cursor.execute(ins2)
        conn.commit()
        ins3 = "INSERT INTO ordine (id, Numero_spedizione) VALUES ('3', '14')"
        cursor.execute(ins3)
        conn.commit()
        ins4 = "INSERT INTO ordine (id, Numero_spedizione) VALUES ('4', '16')"
        cursor.execute(ins4)
        conn.commit()
    case "giro":
        trnct = "TRUNCATE TABLE giro"
        cursor.execute(trnct)
        conn.commit()
        ins1 = "INSERT INTO giro (Nome, Targa, Numero_spedizione) VALUES ('Pinco Pallino', 'lo992ou', '14')"
        cursor.execute(ins1)
        conn.commit()
        ins2 = "INSERT INTO giro (Nome, Targa, Numero_spedizione) VALUES ('Santo Natale', 'tr199re', '16')"
        cursor.execute(ins2)
        conn.commit()
    case "attrezzatura":
        trnct = "TRUNCATE TABLE attrezzatura"
        cursor.execute(trnct)
        conn.commit()
        ins1 = "INSERT INTO attrezzatura (id, Numero, Tipo) VALUES ('1', '4', 'Transpallet a mano')"
        cursor.execute(ins1)
        conn.commit()
        ins2 = "INSERT INTO attrezzatura (id, Numero, Tipo) VALUES ('2', '2', 'Transpallet elettrico')"
        cursor.execute(ins2)
        conn.commit()
    case "attrezzatura_non_disponibile":
        trnct = "TRUNCATE TABLE attrezzatura_non_disponibile"
        cursor.execute(trnct)
        conn.commit()
        ins1 = "INSERT INTO attrezzatura_non_disponibile (id, Numero, Note) VALUES ('1', '4', '----')"
        cursor.execute(ins1)
        conn.commit()
        ins2 = "INSERT INTO attrezzatura_non_disponibile (id, Numero, Note) VALUES ('2', '2', '----')"
        cursor.execute(ins2)
        conn.commit()
    case "veicoli":
        trnct = "TRUNCATE TABLE veicoli"
        cursor.execute(trnct)
        conn.commit()
        ins1 = "INSERT INTO veicoli (id, Targa, Tipo) VALUES ('1', 'lo992ou', 'Furgone')"
        cursor.execute(ins1)
        conn.commit()
        ins2 = "INSERT INTO veicoli (id, Targa, Tipo) VALUES ('2', 'tr199re', 'Furgone')"
        cursor.execute(ins2)
        conn.commit()
        ins3 = "INSERT INTO veicoli (id, Targa, Tipo) VALUES ('3', 'ai512io', 'Muletto')"
        cursor.execute(ins3)
        conn.commit()
    case "veicoli_non_disponibili":
        trnct = "TRUNCATE TABLE veicoli_non_disponibili"
        cursor.execute(trnct)
        conn.commit()
        ins1 = "INSERT INTO veicoli_non_disponibili (id, Targa, Note) VALUES ('1', 'lo992ou', '----')"
        cursor.execute(ins1)
        conn.commit()
        ins2 = "INSERT INTO veicoli_non_disponibili (id, Targa, Note) VALUES ('2', 'tr199re', '----')"
        cursor.execute(ins2)
        conn.commit()
        ins3 = "INSERT INTO veicoli_non_disponibili (id, Targa, Note) VALUES ('3', 'ai512io', '----')"
        cursor.execute(ins3)
        conn.commit()