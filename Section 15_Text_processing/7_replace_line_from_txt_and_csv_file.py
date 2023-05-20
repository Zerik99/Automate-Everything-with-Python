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
