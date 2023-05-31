"""A simple script to convert a SQL database to a CSV file."""
from typing import Any
import sqlite3
from sqlite3.dbapi2 import Connection
from fpdf import FPDF


# establish connection and create cursor.
con: Connection = sqlite3.connect("Section 21_SQL Databases/files/database.db")
cur = sqlite3.Cursor(con)

cur.execute("PRAGMA TABLE_INFO(ips)")
columns = cur.fetchall()
print(columns)

pdf = FPDF(orientation="P", unit="pt", format="A4")
pdf.add_page()

for column in columns:
    print(column[1])
    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(w=100, h=25, txt=column[1], border=1, align="C", ln=0)
pdf.ln()

cur.execute("SELECT * FROM ips ORDER BY asn")
rows: list[Any] = cur.fetchall()

for row in rows:
    for item in row:
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=str(item), border=1, align="C", ln=0)
    pdf.ln()

pdf.output("Section 21_SQL Databases/files/ips.pdf")
