import glob
import os
from pathlib import Path

cwd = os.getcwd()
print(cwd)

entries = Path(str(cwd))
files = (x for x in entries.iterdir() if x.is_file())
for file in files:
    print(str(file), "is a file!")

print()

python_files = glob.glob('a*.txt')  # recursive=True
print(python_files)

print()

#############################################################

# https://stackoverflow.com/questions/11968976/list-files-only-in-the-current-directory/11969014#11969014

# Walking a directory tree and printing the names of the directories and files
for dirpath, dirnames, files in os.walk('.'):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)

print()

for dirpath, dirnames, files in os.walk('.', topdown=True):
    # with topdown true, this will prevent walk from going into subs;
    # remove the dirs.clear() line and the files in sub folders are included again
    dirnames.clear()
    for file_name in files:
        print(file_name)
