"""A simple program to create a new text file and add content to it."""
content_text = """This is a multiline text
        
that will be written in the file

and will be displayed in the file
            
as it is written here."""

with open(
    "Section 15_Text_processing/files/lecture_1/file1.txt", "w", encoding="utf-8"
) as file:
    file.write("Hello World")
    file.write("\n")
    file.write(content_text)
    file.close()
