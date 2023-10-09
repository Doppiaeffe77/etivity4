from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, Float, VARCHAR, CHAR

print("Username: ", end="")
usr = input()
print("Password: ", end="")
pwd = input()
print("Database: ", end="")
db = input()
engine = create_engine("mysql+mysqlconnector://" + usr + ":" + pwd + "@localhost/" + db, echo=False)
meta = MetaData()
magazzino = Table('Magazzino', meta, Column('Partita_iva', CHAR(11), primary_key=True), Column('Nome', VARCHAR(30)),
                  Column('Indirizzo', VARCHAR(40)), Column('Cap', CHAR(5)), Column('Citta', VARCHAR(20)))
cliente = Table('Cliente', meta, Column('Nome', VARCHAR(20), primary_key=True), Column('Numero_contratto', VARCHAR(15)))
merci = Table('Merci', meta, Column('Mittente', VARCHAR(20), primary_key=True), Column('Numero_DDT', VARCHAR(15)))
personale = Table('Personale', meta, Column('id', Integer, primary_key=True), Column('Codice_fiscale', CHAR(16)),
                  Column('Cognome', VARCHAR(20)), Column('Nome', VARCHAR(20)), Column('Indirizzo', VARCHAR(50)),
                  Column('Cap', CHAR(5)), Column('Citta', VARCHAR(20)))
stato = Table('Stato', meta, Column('Codice_fiscale', CHAR(16), primary_key=True), Column('Mansione', VARCHAR(20)),
              Column('Stipendio', Float(4,2)), Column('Operativita', VARCHAR(15)))
bancali = Table('Bancali', meta, Column('id', Integer, primary_key=True), Column('Epal', Integer),
                Column('Eur', Integer), Column('Niente', Integer))
ordine = Table('Ordine', meta, Column('id', Integer, primary_key=True), Column('Numero_spedizione', VARCHAR(15)))
giro = Table('Giro', meta, Column('Nome', VARCHAR(30), primary_key=True), Column('Targa', CHAR(7)), Column('Numero_spedizione', VARCHAR(30), primary_key=True))
attrezzatura = Table('Attrezzatura', meta, Column('id', Integer, primary_key=True), Column('Numero', VARCHAR(2)), Column('Tipo', VARCHAR(30)))
a_n_d = Table('Attrezzatura_non_disponibile', meta, Column('id', Integer, primary_key=True), Column('Numero', VARCHAR(3)), Column('Note', VARCHAR(50)))
veicoli = Table('Veicoli', meta, Column('id', Integer, primary_key=True), Column('Targa', VARCHAR(7)), Column('Tipo', VARCHAR (15)))
v_n_d = Table('Veicoli_non_disponibili', meta, Column('id', Integer,  primary_key=True), Column('Targa', VARCHAR(7)), Column('Note', VARCHAR(50)))
meta.create_all(bind=engine)