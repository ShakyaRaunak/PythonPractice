# Open a file foo.txt containing the following lines :
# Python is a great language.
# Yeah its great!!
fo = open("foo.txt", "r")
print("Name of the file: ", fo.name)

# fileObject.readlines( sizehint ) where, sizehint − This is the number of bytes to be read from the file.
line = fo.readlines()
print("Read Line: %s" % (line))  # Read Line: ['Python is a great language.\n', 'Yeah its great!!\n']

line = fo.readlines(2)
print("Read Line: %s" % (line))  # Read Line: []

# another way to read the file
with open("foo.txt") as text_file:
    contents = text_file.read()
print(contents)

fo.close()
