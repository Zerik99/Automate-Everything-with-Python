"""A simple app to open a public google spreadsheet using pandas."""
from pathlib import Path
import gspread


secrets_file = Path("Section 11_Working with Google Sheets/API_KEY/secrets.json")
gc = gspread.service_account(secrets_file)
spreadsheet = gc.open("PythonTestPrivate")
worksheet1 = spreadsheet.worksheet("Sheet1")

# update a cell
worksheet1.update("A2", "Hello World")

# update a cell by row and column
worksheet1.update_cell(row=3, col=1, value="Hello World 2")

# update a column of cells
existing_column = worksheet1.get_values("b2:b9")
print(existing_column)

# an example of defining a new column based on an existing column.
new_column = [[cell[0] + " New value"] for cell in existing_column]
print(new_column)

worksheet1.update("f1:f9", [["New_Column"]] + new_column)
