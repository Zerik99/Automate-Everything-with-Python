from pathlib import Path

"""This exercise assumes a folder structure like this:
root/files/year/month/file

    This exercise will rename all files in the sub-sub-folders to: 
year_month_filename.extension

    For simplicity I've hard coded the year and month folders. 
regex could be used to find the year and month folders.

I've been using the same folder for other exercises in this section. so it required 
some conditional checks to ensure only the files in the sub-sub-folders are renamed."""


class FileUtil:
    def __init__(self):
        self.root_dir = Path("Section 4_Working with Computer Files and Folders/files")
        self.file_paths = self.root_dir.glob("**/*")

    def rename_files(self):
        for path in self.file_paths:
            parent_folder = path.parts[-2]
            grandparent_folder = path.parts[-3]

            if (
                not path.is_file()
                or (grandparent_folder != "2022" and grandparent_folder != "2021")
                or (parent_folder != "November" and parent_folder != "December")
            ):
                # print("skipping...")
                continue  # omit iteration if the above conditions are met.

            new_filename = (
                grandparent_folder + "_" + parent_folder + "_" + path.stem + path.suffix
            )
            new_filepath = path.with_name(new_filename)
            path.rename(new_filepath)
            print(path)
            print(new_filepath)


def main():
    files = FileUtil()
    files.rename_files()


if __name__ == "__main__":
    main()
