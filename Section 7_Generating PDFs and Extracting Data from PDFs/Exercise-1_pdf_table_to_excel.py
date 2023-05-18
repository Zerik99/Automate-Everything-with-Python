import tabula
import pandas as pd

pdftable = tabula.io.read_pdf(
    input_path="Section 7_Generating PDFs and Extracting Data from PDFs/files/exercise_1/Table+and+Text.pdf",
    pages="1",
)

# getting an error here when it should be fine. extremely annoying.
print(type(pdftable[0]))  # type: ignore

df = pdftable[0]  # type: ignore

# create a pandas excel writer object using xlsxwriter as the engine
writer = pd.ExcelWriter(
    path="Section 7_Generating PDFs and Extracting Data from PDFs/files/exercise_1/Table+and+Text.xlsx",
    engine="xlsxwriter",
)

# write the dataframe to the excel file
df.to_excel(writer, sheet_name="Sheet1", startrow=0, header=False, index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.close()
