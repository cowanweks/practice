import os
import logging

def enum_folders_and_create_readmes() -> list:
    path = os.getcwd()

    # A file pattern to ignore
    ignore_pattern = [
        ".git", ".gitignore", "README.md"
    ]

    # Loop in the current directory
    for subdir, dirs, files in os.walk(path):
        with open(f"{subdir}/README.md", "w") as f:
            pass


if __name__ == '__main__':
    enum_folders_and_create_readmes()
