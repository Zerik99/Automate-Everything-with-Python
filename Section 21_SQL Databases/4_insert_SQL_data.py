"""A simple app to insert data into a SQL database."""
from typing import Any
import sqlite3
from sqlite3.dbapi2 import Connection


# establish connection and create cursor.
con: Connection = sqlite3.connect("Section 21_SQL Databases/files/database.db")
cur = sqlite3.Cursor(con)

new_rows: list[Any] = [
    ("100.100.100.100", "a.b.c", "100"),
    ("200.200.200.200", "d.e.f", "200"),
]

cur.executemany("INSERT INTO ips VALUES(?, ?, ?)", new_rows)
con.commit()

cur.execute("SELECT * FROM ips ORDER BY asn")
print(cur.fetchall())
