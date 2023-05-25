"""A simple app to listen for changes to a cell on a google spreadsheet."""
from time import sleep
from pathlib import Path
import gspread


secrets_file = Path("Section 11_Working with Google Sheets/API_KEY/secrets.json")
gc = gspread.service_account(secrets_file)
workbook = gc.open("PythonTestPrivate")
worksheet = workbook.worksheet("Excel Listener")

data = worksheet.get_all_values()
print(data)


while True:
    current_value = worksheet.acell("A2").value
    sleep(5)
    check_value = worksheet.acell("A2").value
    if current_value == check_value:
        print("no change")
        continue
    print("value changed")
    worksheet.update_acell("C2", "value changed")
