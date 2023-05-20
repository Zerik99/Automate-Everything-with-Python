"""a simple script that merges the contents of a text file or a CSV file into a single file"""

from pathlib import Path

files_dir = Path("Section 15_Text_processing/files/lecture_5")
filesbackup_dir = Path("Section 15_Text_processing/files/lecture_5/files_backup")

merged_content: str = ""

for file in files_dir.iterdir():
    with open(file, "r", encoding="utf-8") as f:
        content: str = f.read()
        merged_content += content + "\n"
        f.close()

    f_ext: str = "." + file.parts[-1].split(sep=".")[-1]

    with open(f"{filesbackup_dir}/merged_data{f_ext}", "w", encoding="utf-8") as f:
        f.write(merged_content)

# -----high-level description----- #
# 1. iterate over the files in the files directory
# 2. open the current file for reading
# 3. read the file content
# 4. add the file content to the merged_content string
# 5. close the file
# 6. get the file extension of the current file
# 7. open the merged file for writing
# 8. write the merged file content
# 9. close the merged file
# --------------------------------- #
