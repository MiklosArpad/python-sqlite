
import sqlite3
from pprint import pprint

# kapcsolat létrehozása

conn = sqlite3.connect("adatbazis.db")
curs = conn.cursor()

# a táblák létrehozása
curs.execute("CREATE TABLE IF NOT EXISTS felhasznalok (nev TEXT, kor INTEGER, nem TEXT, pontszam REAL)")
curs.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER, gender TEXT, score REAL)")


#curs.execute("INSERT INTO felhasznalok VALUES ('Erika', 28, 'no', 8.1)")
#curs.execute("INSERT INTO felhasznalok VALUES ('Evi', 41, 'no', 8.2)")
#curs.execute("INSERT INTO felhasznalok VALUES ('Zoli', 38, 'ferfi', 7.9)")
#curs.execute("INSERT INTO felhasznalok VALUES ('Pista', 48, 'ferfi', 8.7)")


#curs.execute("INSERT INTO felhasznalok VALUES ('Vivien', 32, 'nő', 8.4)")
#curs.execute("INSERT INTO felhasznalok VALUES ('Tamás', 47, 'ferfi', 6.3)")
#conn.commit()


#curs.execute("INSERT INTO users VALUES ('Jack', 48, 'man', 7.7)")
#curs.execute("INSERT INTO users VALUES ('Angelina', 21, 'woman', 7.9)")
#curs.execute("INSERT INTO users VALUES ('Hilary', 47, 'woman', 6.4)")


#curs.execute("UPDATE felhasznalok SET nem=? WHERE nem=?", ("nő", "no"))
#curs.execute("UPDATE felhasznalok SET nem=? WHERE nem=?", ("férfi", "ferfi"))


#curs.execute("UPDATE users SET gender=? WHERE gender=?", ("male", "man"))
#curs.execute("UPDATE users SET gender=? WHERE gender=?", ("female", "woman"))
#conn.commit()


#curs.execute("DELETE FROM felhasznalok WHERE REWID=6")
curs.execute("DELETE FROM felhasznalok WHERE pontszam<6.5")
conn.commit()


# ezzel a konzolra lehet kiiratni
curs.execute("SELECT * FROM felhasznalok")
adatok = curs.fetchall()
pprint(adatok)


# ezzel kell elmenteni a táblák tartalmát
conn.commit()

# le kell zárni a kapcsolatot mert különben túlcsordúl
conn.close()


"""   Ha az sqlite ban szeretnénk insertelni 
    1- az EXECUTE SQL gombon kell beilleszteni
    2- a paly icont kell elindítani
    3- ahhoz, hogy a python is lefutassa, ahhoz az SQLite -on kell a File + Write Changes kell klickelni,
       így a python is elmenti       egyébként az 5-ös részben van  
"""