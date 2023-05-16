import fitz

# there seems to be an issue with the fitz package. It is not working properly. I will try to fix it later.
with fitz.open(
    "Section 7_Generating PDFs and Extracting Data from PDFs/files/lecture_3/students.pdf"
) as pdf:
    text = ""
    for page in pdf:
        text += page.get_Text()
    print(text)
