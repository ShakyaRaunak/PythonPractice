import os
import shutil

os.mkdir("testing")
os.rmdir('testing')

os.rmdir('testing_2')
os.rename('testing', 'testing_2')

os.remove('old.txt')
os.rmdir('new_one')

shutil.rmtree('testing_2')
f = open("test.txt")

f1 = open("myfile.txt", "x")  # will create a file, returns an error if the file exists
f1.close()

f2 = open("myfile.txt", "w")  # will create a file, if does not exist but does not return an error if the file exists
f2.close()
