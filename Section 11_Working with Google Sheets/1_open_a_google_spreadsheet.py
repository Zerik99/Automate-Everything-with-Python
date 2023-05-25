"""A simple app to open a public google spreadsheet using pandas."""
import pandas as pd
import gspread
import re

import regex

# public google spreadsheet url
# url = "https://docs.google.com/spreadsheets/d/ndp2r7ijBuMfGHDLbhqb6k38g/gviz/tq?tqx=out:csv&sheet=sheet1" # intentionally wrong url
# df = pd.read_csv(url)
# print(df)

# private google spreadsheet url

gc = gspread.service_account(
    "Section 11_Working with Google Sheets/API_KEY/secrets.json"
)

spreadsheet = gc.open("PythonTestPrivate")

# get worksheet by index
# worksheet1 = spreadsheet.get_worksheet(0)

# get worksheet by title
worksheet1 = spreadsheet.worksheet("Sheet1")

# get all values from worksheet
# data = worksheet1.get_all_records()

# get specific range of values from worksheet
data = worksheet1.get_values("A1:E1")
print(data)

data = worksheet1.get_values("A1:E2")
print(data)

# get row values
data = worksheet1.row_values(1)
print(data)

# get column values
data = worksheet1.col_values(1)
print(data)

# get cell value
cell = worksheet1.get_values("A1")[0][0]
print(cell)

# get cell with acell function
cell = worksheet1.acell("A1").value
print(cell)

# get cell by searching for a value
cell = worksheet1.find("col1")
print(cell.row, cell.col, cell.value)

# search for many cells
print("search for many cells with matching values. findal: ")
cells = worksheet1.findall("test2")
for cell in cells:
    print(cell.row, cell.col, cell.value)


# search cells for partial match. Use regex + findall
print("search cells for partial match. Use regex + findall: ")
regex = re.compile(r"col")
cells = worksheet1.findall(regex)
for cell in cells:
    print(cell.row, cell.col, cell.value)

# url = "https://docs.google.com/spreadsheets/d/1fxnyEz5PRAj6qhDYqKe5FJZmYQppDPXaEBK1Ry8qMYc/gviz/tq?tqx=out:csv&sheet=sheet1"
# df = pd.read_csv(url)
# print(df)
