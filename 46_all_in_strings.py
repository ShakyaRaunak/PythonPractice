s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first character is '%s'" % s[0])  # S
print("The first five characters are '%s'" % s[:5])  # Strin
print("The next five characters are '%s'" % s[5:10])  # gs ar
print("The thirteenth character is '%s'" % s[12])  # a
print("The characters with odd index are '%s'" % s[1::2])  # (0-based indexing) output : 'tig r wsm!'
print("The characters with even index are '%s'" % s[-20::2])  # (0-based indexing) output : 'Srnsaeaeoe'
print("The last five characters are '%s'" % s[-5:])  # some!

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

# more string methods
str = "Hello World"
print(str.isalnum())  # check if all char are alphanumeric
print(str.isalpha())  # check if all char in the string are alphabetic
print(str.isdigit())  # test if string contains digits
print(str.istitle())  # test if string contains title words
print(str.isupper())  # test if string contains upper case
print(str.islower())  # test if string contains lower case
print(str.isspace())  # test if string contains spaces
print(str.endswith('d'))  # test if string endswith a d
print(str.startswith('H'))  # test if string startswith H
