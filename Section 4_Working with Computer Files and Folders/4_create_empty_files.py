import FileUtilities


def main():
    root_dir = (
        "Section 4_Working with Computer Files and Folders/files/create empty files"
    )
    f = FileUtilities.FileUtil(root_dir=root_dir)
    f.create_empty_files(num_filestart=0, num_filestop=10, file_extension=".txt")


if __name__ == "__main__":
    main()
