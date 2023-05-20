"""a simple program to remove a specific character from the end of the content of multiple text files"""
from pathlib import Path

files_dir = Path(
    "section 15_text_processing/files/lecture_3_multiple_files"
)  # create a Path object for the directory containing the files
filesbackup_dir = Path(
    "section 15_text_processing/files/lecture_3_multiple_files/files_backup"
)  # create a Path object for the directory containing the files

for filepath in files_dir.iterdir():
    with open(filepath, "r", encoding="utf-8") as file:
        content: str = file.read()
        modified_content: str = content[:-1]
        file.close()

    with open(f"{filesbackup_dir}/{filepath.name}", "w", encoding="utf-8") as file:
        file.write(modified_content)
        file.close()


# simplified example only for one file.
#
#
# with open(
#     "section 15_text_processing/files/lecture_3/data.csv", "r", encoding="utf-8"
# ) as file:
#     content = file.read()

# modified_content = content[:-1]

# with open(
#     "section 15_text_processing/files/lecture_3/data_modified.csv",
#     "w",
#     encoding="utf-8",
# ) as file:
#     file.write(modified_content)
#     file.close()
