import FileUtilities
import zipfile
from pathlib import Path

"""having trouble with this one. 
It duplicates the root directory in the destination path 
and fails to unzip the files."""


class files(FileUtilities.FileUtil):
    def unzip_zipfile(self):
        """Unzips a zipfile"""
        destination_path = self.root_dir
        file_paths = self.root_dir.rglob("*.zip")
        print(file_paths)
        for fp in file_paths:
            if not fp.is_file():
                continue
            with zipfile.ZipFile(fp, "r") as zf:
                zf.extractall(path=destination_path)


def main():
    f = files(
        root_dir="Section 4_Working with Computer Files and Folders/files/create empty files"
    )
    f.unzip_zipfile()


if __name__ == "__main__":
    main()
