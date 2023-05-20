"""a simple script that merges the contents of a text file or a CSV file into a single file"""
from pathlib import Path
from typing import Any

files_dir = Path("Section 15_Text_processing/files/lecture_6")
filesbackup_dir = Path("Section 15_Text_processing/files/lecture_6/files_backup")

merged_content: str = ""
content_string: str = ""

for i, filepath in enumerate(files_dir.iterdir()):
    with open(filepath, "r", encoding="utf-8") as file:
        content: list[Any] = file.readlines()
        content_no_header: list[Any] = content[1:]
    if i == 0:
        content_string = "AMOUNT,UNITS,COST\n" + "".join(content[1:])
        merged_content += content_string + "\n"
        file.close()
    else:
        content_string = "".join(content_no_header)
        merged_content += content_string + "\n"
        file.close()

    f_ext: str = "." + filepath.parts[-1].split(sep=".")[-1]

    with open(f"{filesbackup_dir}/merged_data{f_ext}", "w", encoding="utf-8") as file:
        file.write(merged_content)

# -----logic documentation----- #
# 1. Create a files directory and a filesbackup directory.
# 2. Create a variable to store the merged content.
# 3. Create a variable to store the content of the file as a string.
# 4. Iterate over each file in the files directory.
# 5. Open the file in read mode.
# 6. Create a variable to store the content of the file as a list.
# 7. Create a variable to store the content of the file as a list without the header.
# 8. If the file is the first file in the directory:
#       - Create a variable to store the content of the file as a string with a header.
#       - Add the content of the file as a string with a header to the merged content.
#       - Close the file.
# 9. Otherwise:
#       - Create a variable to store the content of the file as a string without a header.
#       - Add the content of the file as a string without a header to the merged content.
#       - Close the file.
# 10. Create a variable to store the extension of the file.
# 11. Open a file in the filesbackup directory in write mode.
# 12. Write the merged content to the file.
# 13. Close the file.
