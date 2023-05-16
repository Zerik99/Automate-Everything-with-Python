import pandas
from fpdf import FPDF

df = pandas.read_excel(
    "Section 7_Generating PDFs and Extracting Data from PDFs/files/lecture_2/data.xlsx"
)

print(df)

for index, row in df.iterrows():
    pdf = FPDF(orientation="P", unit="pt", format="A4")
    pdf.add_page()

    pdf.set_font(family="Times", size=24, style="B")
    pdf.cell(w=0, h=50, txt=f"{row['name']}", align="C", ln=1)

    for column in df.columns[1:]:
        pdf.set_font(family="Times", size=12, style="B")
        pdf.cell(w=100, h=25, txt=f"{column.title()}: ")

        pdf.set_font(family="Times", size=12, style="")
        pdf.cell(w=100, h=25, txt=f"{row[column]}", ln=1)

    pdf.output(
        f"Section 7_Generating PDFs and Extracting Data from PDFs/files/lecture_2/{row['name']}.pdf"
    )
