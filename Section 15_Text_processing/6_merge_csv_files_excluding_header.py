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
        content_string = "".join(content)
        merged_content += content_string + "\n"
        file.close()
    else:
        content_string = "".join(content_no_header)
        merged_content += content_string + "\n"
        file.close()

    f_ext: str = "." + filepath.parts[-1].split(sep=".")[-1]

    with open(f"{filesbackup_dir}/merged_data{f_ext}", "w", encoding="utf-8") as file:
        file.write(merged_content)

# -----high-level logic----- #
# 1. create a path object for the directory containing the files to be merged
# 2. create a path object for the directory where the merged files will be stored
# 3. create an empty string to store the contents of the merged files
# 4. create an empty string to store the contents of the file being read
# 5. iterate over the files in the directory
# 6. open the file in read mode
# 7. create a list of the file's contents
# 8. create a list of the file's contents without the header
# 9. if the file is the first file in the directory
# 10. convert the list of contents into a string
# 11. add the contents of the file to the merged content string
# 12. close the file
# 13. otherwise
# 14. convert the list of contents without the header into a string
# 15. add the contents of the file to the merged content string
# 16. close the file
# 17. get the file extension of the file being read
# 18. open the merged file in write mode
# 19. write the merged content to the merged file
# 20. close the file
