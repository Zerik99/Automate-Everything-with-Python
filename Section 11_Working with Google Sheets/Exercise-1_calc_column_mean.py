"""A simple app to calculate the mean of a column in a google spreadsheet."""
from pathlib import Path
from statistics import mean
import gspread


secrets_file = Path("Section 11_Working with Google Sheets/API_KEY/secrets.json")
gc = gspread.service_account(secrets_file)
spreadsheet = gc.open("PythonTestPrivate")
worksheet1 = spreadsheet.worksheet("Sheet1")

column = worksheet1.get_values("g2:g9")
mean_value = round(mean([float(cell[0]) for cell in column]), 2)
worksheet1.update_cell(10, 7, mean_value)
