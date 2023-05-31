import sqlite3
from sqlite3.dbapi2 import Connection

# establish connection and create cursor.
con: Connection = sqlite3.connect("Section 21_SQL Databases/files/database.db")
cur = sqlite3.Cursor(con)

# execute query All rows and columns ordered.
cur.execute("SELECT * FROM 'ips' ORDER BY asn")
print(cur.fetchall())

# execute query All rows and certain columns ordered.
cur.execute("SELECT address, asn FROM 'ips' ORDER BY asn")
print(cur.fetchall())

# execute query All rows where asn is less that 300.
cur.execute("SELECT * FROM 'ips' WHERE asn < 300")
print(cur.fetchall())

# execute query All rows where asn is less that 300.
cur.execute("SELECT * FROM 'ips' WHERE asn = 144")
print(cur.fetchall())

# execute query All rows where asn is less that 300.
cur.execute("SELECT * FROM 'ips' WHERE asn < 144 AND domain like '%.sa'")
print(cur.fetchall())
