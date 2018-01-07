##  Single file script that counts files, lines, and characters of plain text files in the current directory.
##  Excludes itself and any files whos path are partly or entirely included in excludedPathList
##  (assuming excludePathsis true).
# Author:   Catsymptote
# Email:    catsymptote@gmail.com


##########################################
##########################################

## Settings:
# Count lines and/or characters?
checkLines = True
checkChars = True

# Exclude certain paths from the check?
excludePaths = True

# Paths (or parts of paths) to be excluded.
excludedPathList = [
    ".idea", "venv",    # PyCharm folders.
    ".git"              # .git folder and .gitignore file.
]

##########################################
##########################################


print("This script counts all files, lines, and characters in all (non-excluded) files (depending on settings).\n")


import os


##  Returns list of flies in current directory.
def get_files(directory):
    file_list = []
    for path, subdirs, files in os.walk(directory):
        for name in files:
            file_list.append(os.path.join(path, name))
    return file_list


##  Checks if "file" is the path to this script file.
def is_this_file(file):
    if (file == os.path.realpath(__file__)):
        return True
    return False


##  Count lines (and characters) in the file.
def counter(file):
    global totalLines
    global totalChars
    try:
        with open(file) as f:
            lines = f.readlines()
        if(checkChars):
            for i in range(len(lines)):
                totalChars += len(lines[i])
        totalLines += len(lines)
    except(Exception):
        return 0


##  Removes excluded paths from the file (path) list.
def purge_dirs():
    for j in range(len(excludedPathList)):
        i = 0
        while(i < len(file_list)):
            if (excludedPathList[j] in file_list[i]):
                file_list.pop(i)
                continue
            i += 1


##  Wannabe main().
def run():
    if(excludePaths):
        purge_dirs()

    for i in range(len(file_list)):
        if(not is_this_file(file_list[i])):
            if(checkLines):
                counter(file_list[i])


##  Get current dir, create file list and counter values, run dat shit, print the results, and waits for exit.
directory   = os.getcwd()
file_list   = get_files(directory)
totalLines  = 0
totalChars  = 0
run()
print("Total files:\t\t" + str(len(file_list)))
if(checkLines):
    print("Total lines:\t\t" + str(totalLines))
if(checkChars):
    print("Total characters:\t" + str(totalChars))
input("\nPress enter to exit...")