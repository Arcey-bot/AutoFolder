import os
import config
from shutil import make_archive
from distutils.dir_util import copy_tree
from bs4 import BeautifulSoup

path = config.file_path


def main():
    working = get_work_dir()
    folders = create_folders(working)
    if input("Copy files from examples? [y/n] ") == 'y':
        copy_files(folders, working)
    else:
        populate_folders(folders)
    if input("Zip files? [y/n]: ") == 'y':
        zip_folders(folders)


def get_work_dir():
    # Get the current subfolder you will be working in
    loc = input("Folder to create subfolders in: ")
    working = path + '/' + loc
    if not os.path.exists(working):
        os.makedirs(working)
    return working


def create_folders(working):
    # Create specified number of folders in previously defined
    # subfolder if it does not already exist.
    created = []
    working += '/Practice ' + working[len(working) - 1]
    for i in range(1, int(input("How many assignments? ")) + 1):
        current = working + '.' + str(i)
        created.append(current + '/')
        if not os.path.exists(current):
            os.makedirs(current)
    return created


def get_src_folders(working, assignments):
    # Get the example folders inside working directory to get
    # copy contents for new folders
    src_folders = []
    working += '/' + working[len(working) - 1]
    for i in range(1, assignments):
        current = working + '.' + str(i)
        src_folders.append(current)
    return src_folders


def copy_files(folders, working):
    # Copy contents from one directory (left) to a new location (right)
    sources = get_src_folders(working, len(folders))
    for i in range(len(sources)):
        copy_tree(sources[i], folders[i])


def populate_folders(created):
    # If a HTML file isn't already in a folder, provide a default one
    for i in created:
        if not os.path.exists(i + "index.html"):
            f = open(i + "index.html", "w")
            write_HTML(f)


# noinspection PyPep8Naming
def write_HTML(f):
    # Default HTML
    f.write("<!DOCTYPE html>\n")
    f.write('<html lang="en">')
    f.write("\n")
    f.write("\n<head>\n")
    f.write("    <title> </title>\n")
    f.write('    <meta charset="utf-8">')
    f.write("\n</head>\n")
    f.write("\n")
    f.write("<body>\n")
    f.write("</body>\n")
    f.write("\n")
    f.write("</html>\n")
    f.close()


def zip_folders(created):
    # Zip all created folders
    for i in range(0, len(created)):
        created[i] = created[i][:-1]
        make_archive(created[i], 'zip', root_dir=created[i])


if __name__ == '__main__':
    main()
