from pathlib import Path

root_dir = Path("Section 4_Working with Computer Files and Folders/files")
file_paths = root_dir.iterdir()

# print(list(file_paths))
for path in file_paths:
    new_filename = "new_" + path.stem + path.suffix
    # generates a path with the new filename.
    new_filepath = path.with_name(new_filename)
    print(new_filepath)
    # renames the path to a target path.
    path.rename(new_filepath)
