from FileUtilities import FileUtil


class files(FileUtil):
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
                continue
            file_created_date = self.get_file_Created_Date(path)
            new_filename = f"{file_created_date}_{path.name}"
            new_filepath = path.with_name(new_filename)
            path.rename(new_filepath)


def main():
    root_dir = "Section 4_Working with Computer Files and Folders/files"
    f = files(root_dir=root_dir)
    f.rename_files()


if __name__ == "__main__":
    main()
