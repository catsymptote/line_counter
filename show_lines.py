## Single file script that counts lines in all plain text files in the current directory.
## Excludes itself and any folders included in the excludedFolders list (assuming excludeFolders is true).
# Author:   Catsymptote
# Email:    catsymptote@gmail.com

##########################################
##########################################

## Settings:
# Exclude certain folders from the check?
excludeFolders = True

# Folders to be excluded.
excludedFolders = [
    ".idea",
    "venv",
    ".git"
]

##########################################
##########################################


import os


def get_files(directory):
    file_list = []
    for path, subdirs, files in os.walk(directory):
        for name in files:
            file_list.append(os.path.join(path, name))
    return file_list


def is_this_file(file):
    if (file == os.path.realpath(__file__)):
        return True
    return False


def count_lines(file):
    try:
        with open(file) as f:
            lines = f.readlines()
        return len(lines)
    except(Exception):
        return 0


def purge_dirs():
    for j in range(len(excludedFolders)):
        i = 0
        while(i < len(file_list)):
            if (excludedFolders[j] in file_list[i]):
                file_list.pop(i)
                continue
            i += 1


def run():
    print("Start")
    if(excludeFolders):
        purge_dirs()

    lines = 0
    for i in range(len(file_list)):
        if(not is_this_file(file_list[i])):
            lines += count_lines(file_list[i])

    print("Total lines: " + str(lines))


directory = os.getcwd()
file_list = get_files(directory)
run()
