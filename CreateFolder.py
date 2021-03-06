import os
import config
from bs4 import BeautifulSoup
from shutil import make_archive
from distutils.dir_util import copy_tree

path = config.file_path


def main():
    working = get_work_dir()
    folders = create_folders(working)
    if input("Copy files from examples? [y/n] ") == 'y':
        copy_files(folders, working)
        # There's only text to replace if we're using examples
        if input("Replace all placeholder text in files? [y/n] ") == 'y':
            replace_html(folders)
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
    working += '/Practice ' + get_digit_suffix(working)
    for i in range(1, int(input("How many assignments? ")) + 1):
        current = working + '.' + str(i)
        created.append(current + '/')
        if not os.path.exists(current):
            os.makedirs(current)
    return created


def get_digit_suffix(working):
    # Search working for digit suffix in current directory
    # Allows for more directories with 2-digit suffixes
    # to be operated on
    suffix = ""

    for c in reversed(working):
        if c.isdigit():
            suffix += c
        else:
            break
    return suffix[::-1]


def get_src_folders(working, assignments):
    # Get the example folders inside working directory to get
    # copy contents for new folders
    src_folders = []
    working += '/' + get_digit_suffix(working)
    for i in range(1, assignments + 1):
        current = working + '.' + str(i)
        src_folders.append(current)
    return src_folders


def copy_files(folders, working):
    # Copy contents from one directory (left) to a new location (right)
    sources = get_src_folders(working, len(folders))
    for i in range(len(sources)):
        copy_tree(sources[i], folders[i])


def replace_html(folders):
    # Iterates through all copied files and replace text accordingly
    for folder in folders:
        # Find all HTML files in directory and read them
        for subdir, dirs, files in os.walk(folder):
            for filename in files:
                file_path = subdir + os.sep + filename
                if file_path.endswith(".html"):
                    html = read_html(file_path)
                    soup = edit_html_text(html)
                    overwrite_html(file_path, soup)


def read_html(file_name):
    # Return the html from the file passed in
    with open(file_name, "r") as f:
        return f.read()


def overwrite_html(file_name, soup):
    with open(file_name, "w") as f:
        f.write(soup.prettify(formatter='html5'))
        f.close()


def edit_html_text(html):
    # Create a soup and sift through it
    soup = BeautifulSoup(html, "html.parser")
    for tags in soup.find_all():
        for child in tags.descendants:
            # This checks if nav tag and will prevent the text from changing if it is
            if child.find_parent(config.SKIP_TAGS) is None:
                if child.parent.name not in config.IGNORE_TAGS and child.string is not None:
                    child.string = lorem(get_word_count(child.string))

    if soup.find(config.CUSTOM_EDIT):
        foot = soup.footer
        foot.clear()
        foot.insert(0, config.FOOTER_CUSTOM_TEXT)
    return soup


def get_word_count(s):
    # Return the number of words in a string denoted by spaces
    return len(s.split(" "))


def lorem(n):
    # Return that same number of words from the LOREM_IPSUM placeholder text
    return " ".join(config.LOREM_IPSUM.split(" ")[0:n])


# TODO: Replace current file open using with
def populate_folders(created):
    # If a HTML file isn't already in a folder, provide a default one
    for i in created:
        if not os.path.exists(i + "index.html"):
            f = open(i + "index.html", "w")
            write_html(f)


# TODO: Rework template HTML to use BS4 rather than strings
def write_html(f):
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
