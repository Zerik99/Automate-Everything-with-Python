import FileUtilities


def main():
    root_dir = "Section 4_Working with Computer Files and Folders/files/change file extensions to csv"
    f = FileUtilities.FileUtil(root_dir=root_dir)
    f.change_file_extension(".csv")


if __name__ == "__main__":
    main()
