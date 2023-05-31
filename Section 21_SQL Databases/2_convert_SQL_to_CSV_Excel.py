"""A simple script to convert a SQL database to a CSV file."""
import sqlite3
from sqlite3.dbapi2 import Connection
import pandas as pd
from pandas.core.frame import DataFrame


# establish connection and create cursor.
con: Connection = sqlite3.connect("Section 21_SQL Databases/files/database.db")
cur = sqlite3.Cursor(con)

df: DataFrame = pd.read_sql_query("SELECT * FROM 'ips' ORDER BY asn", con)
print(df)

df.to_csv("Section 21_SQL Databases/files/ips.csv", index=False)
df.to_excel("Section 21_SQL Databases/files/ips.xlsx", index=False)
