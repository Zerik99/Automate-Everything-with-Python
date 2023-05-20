"""a simple program to replace a specific word from the content of multiple csv files"""
from pathlib import Path

files_dir = Path(
    "section 15_text_processing/files/lecture_4"
)  # create a Path object for the directory containing the files
filesbackup_dir = Path(
    "section 15_text_processing/files/lecture_4/files_backup"
)  # create a Path object for the directory containing the files

for filepath in files_dir.iterdir():  # iterate over the files in the directory
    with open(filepath, "r", encoding="utf-8") as file:  # open the file for reading
        content: str = file.read()  # read the content
        modified_content: str = content.replace("amount", "units")  # replace the word
        file.close()  # close the file

    with open(
        f"{filesbackup_dir}/{filepath.name}", "w", encoding="utf-8"
    ) as file:  # open the file for writing
        file.write(modified_content)  # write the modified content
        file.close()  # close the file


# Here is the explanation for the code above:
# 1. Import the Path object from the pathlib module
# 2. Create a Path object for the directory containing the files
# 3. Create a Path object for the directory containing the backup files
# 4. Iterate over the files in the directory
# 5. Open the file for reading
# 6. Read the content of the file
# 7. Replace the word in the content and store the modified content in a variable
# 8. Close the file
# 9. Open the file for writing
# 10. Write the modified content to the file
# 11. Close the file
