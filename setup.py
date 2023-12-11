import os
import logging

def enum_folders_and_create_readmes(path: str) -> list:
    # A file pattern to ignore
    ignore_pattern = [
        ".git", ".gitignore", "README.md"
    ]

    # Folders in the current directory
    folders: list[str] = os.listdir(path=path)

    for folder in folders:
        if folder.__contains__("*.*"):
            folders.remove(folder)

    print(folders)

    # Loop in the current directory
    for folder in folders:
        with open(f"{folder}/README.md", "w") as f:
            pass


if __name__ == '__main__':
    # enum_folders_and_create_readmes(".")
    d = {'clientip': '192.168.0.1', 'user': os.name}
    FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
    logging.basicConfig(format=FORMAT, filename="demo.log")
    logging.error("Error", extra=d)
