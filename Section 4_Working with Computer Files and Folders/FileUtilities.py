from pathlib import Path
import zipfile
from time import sleep
from datetime import datetime


class FileUtil:
    def __init__(self, root_dir):
        self.root_dir = Path(f"{root_dir}")
        self.file_paths = self.root_dir.rglob("*")

    def get_file_Created_Date(self, path):
        """Returns the created date of a file in the format: YYYY_MM_DD"""
        filecd = path.stat().st_ctime
        return datetime.fromtimestamp(filecd).strftime("%Y_%m_%d")

    def get_file_Modified_Date(self, path):
        """Returns the modified date of a file in the format: YYYY_MM_DD"""
        filemd = path.stat().st_mtime
        return datetime.fromtimestamp(filemd).strftime("%Y_%m_%d")

    def change_file_extension(self, new_extension):
        """Changes the file extension of all files in the root_dir to new_extension"""
        for path in self.file_paths:
            if not path.is_file():
                continue

            new_filename = f"{path.stem}{new_extension}"
            new_filepath = path.with_name(new_filename)
            path.rename(new_filepath)

    def search_for_file(self, filename):
        """Searches for a file in the root_dir"""
        for path in self.file_paths:
            if not path.is_file():
                continue

            if filename in path.name:
                return path.absolute()

    def rename_files(self, new_filename):
        """Renames all files in the root_dir to new_filename + _filename.extension"""
        for path in self.file_paths:
            if not path.is_file():
                continue

            new_filename = f"{new_filename}_{path.name}"
            new_filepath = path.with_name(new_filename)
            path.rename(new_filepath)

    def create_empty_files(
        self, num_filestart=0, num_filestop=10, file_extension=".txt"
    ):
        """Creates empty files in the root_dir"""
        for i in range(num_filestart, num_filestop):
            new_filename = f"empty_file_{i + 1}{file_extension}"
            new_filepath = self.root_dir.joinpath(new_filename)
            new_filepath.touch()

    def create_archive(self):
        """Creates a zip archive of all files in the root_dir"""
        archive_path = self.root_dir.joinpath("archive.zip")

        with zipfile.ZipFile(archive_path, "w") as zf:
            for path in self.file_paths:
                if not path.is_file():
                    continue
                zf.write(path)

    def unzip_zipfile(self):
        """Unzips a zipfile"""
        destination_path = self.root_dir
        file_paths = self.root_dir.glob("*.zip")
        for path in file_paths:
            with zipfile.ZipFile(path, "r") as zf:
                zf.extractall(path=destination_path)
