import os

obj = open("mno.txt", "w")
obj.close()

# rename() -> It is used to rename a file.
os.rename('mno.txt', 'pqr.txt')

# remove() -> It is used to delete a file.
os.remove('pqr.txt')

# mkdir() -> It is used to create a directory.
os.mkdir("test_dir")

# rmdir() -> It is used to delete a directory. It takes one argument which is the name of the directory.
os.rmdir("test_dir")

# chdir() -> It is used to change the current working directory.
os.mkdir("test_dir")
os.chdir("test_dir")

# getcwd() -> It gives the current working directory.
print(os.getcwd())  # C:\Users\rauna\Desktop\PythonPractice\test_dir
