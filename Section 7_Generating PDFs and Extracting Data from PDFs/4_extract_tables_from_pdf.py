import tabula

# table = tabula.io.read_pdf(
#     "Section 7_Generating PDFs and Extracting Data from PDFs/files/lecture_4/weather.pdf",
#     pages=1,
# )

# print(type(table))

tabula.io.convert_into(
    input_path="Section 7_Generating PDFs and Extracting Data from PDFs/files/lecture_4/weather.pdf",
    output_path="Section 7_Generating PDFs and Extracting Data from PDFs/files/lecture_4/data.csv",
    output_format="csv",
)
