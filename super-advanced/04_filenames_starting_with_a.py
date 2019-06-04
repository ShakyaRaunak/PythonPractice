import os

cwd = os.getcwd()
print(cwd)
files = os.listdir(cwd)
print(files)

required_list_of_files = [f for f in files if os.path.isfile(f) & f.startswith('a')]
print(required_list_of_files)
