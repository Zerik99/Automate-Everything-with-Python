import FileUtilities


def main():
    root_dir = "Section 4_Working with Computer Files and Folders/files"
    files = FileUtilities.FileUtil(root_dir=root_dir)
    print(files.search_for_file("123"))


if __name__ == "__main__":
    main()
