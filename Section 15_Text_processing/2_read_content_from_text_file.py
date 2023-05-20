"""a simple program to read the content of a text file"""
with open(
    "section_15_text_processing/files/lecture_1/file1.txt", "r", encoding="utf-8"
) as file:
    content = file.read()
    print(content)
    file.close()
