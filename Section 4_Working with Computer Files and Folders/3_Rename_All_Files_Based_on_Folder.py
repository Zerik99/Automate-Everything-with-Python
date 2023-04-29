from pathlib import Path

root_dir = Path("Section 4_Working with Computer Files and Folders/files")
# using glob to return sub folders and files.
file_paths = root_dir.glob("**/*")

for path in file_paths:
    # I don't want to return the paths of the files in the files folder. only in the sub folders.
    parent_folder = path.parent
    # alt way of setting the parent folder
    # parent_folder = path.parts[-2]
    # parent_folder = path.parents[0]
    if (
        path.is_file()
        and parent_folder.name == "November"
        or parent_folder.name == "December"
    ):
        new_filename = parent_folder.name + "_" + path.stem + path.suffix
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)
        print(path)
        print(new_filepath)
