name = "raunak"

# String len(string) returns the length of a string
length = len(name)
i = 0
for n in range(-1, (-length - 1), -1):
    print(name[i], "\t", name[n])
    i += 1

print(name.capitalize())  # RAUNAK

str = "Welcome to Python"

# String count(string)
print(str.count('o', 3, len(str)))  # 3
print(str.count('e'))  # 2

# String endswith(string)
print(str.endswith("on"))  # True
print(str.endswith("to", 4, 9))  # False
print(str.endswith("to", 4, 10))  # True

# String find(string)
print(str.find("to"))  # 8
print(str.find("e", 0, len(str)))  # 1
print(str.find("e", 4, len(str)))  # 6

# String index()
print(str.index("to"))  # 8
print(str.index("Py", 3, 16))  # 11

# String isalnum() -> returns True if characters in the string are alphanumeric i.e., alphabets or numbers and
# there is at least 1 character. Otherwise it returns False.
print(str.isalnum())  # False
str1 = "Python101"
print(str1.isalnum())  # True

# String isalpha()
# It returns True when all the characters are alphabets and there is at least one character, otherwise False.
print(str.isalpha())  # False
print(str1.isalpha())  # False
str2 = "HelloPython"
print(str2.isalpha())  # True

# String isdigit()
# It returns True if all the characters are digit and there is at least one character, otherwise False.
print(str2.isdigit())  # False
str3 = "98564738"
print(str3.isdigit())  # True

# String islower()
# It returns True if the characters of a string are in lower case, otherwise False.
print(name.islower())  # True

# String isupper()
# It returns False if characters of a string are in Upper case, otherwise False.
str4 = "RAUNAK"
print(str4.isupper())  # True

# String isspace()
# It returns True if the characters of a string are whitespace, otherwise false.
str5 = "    "
print(str5.isspace())  # True
print(str.isspace())  # False

# String lower()
# It converts all the characters of a string to Lower case.
print(str.lower())  # welcome to python

# String upper()
# It converts all the characters of a string to upper case.
print(name.upper())  # RAUNAK

# String startswith(string)
# It returns a Boolean value if the string starts with given str between begin and end.
print(str.startswith('Wel'))  # True
print(str.startswith('come', 3, 7))  # True

# String swapcase()
# It inverts case of all characters in a string.
print(str.swapcase())  # wELCOME TO pYTHON

# String lstrip()
# It removes all leading whitespace of a string and can also be used to remove particular character from leading.
str7 = "    Hello Python     "
print(str7.lstrip())  # Hello Python
str6 = "@@@@@@@@welcome to SSSIT"
print(str6.lstrip('@'))  # welcome to SSSIT

# String rstrip()
# It removes all trailing whitespace of a string and can also be used to remove particular character from trailing.
print(str7.rstrip())  # Hello Python
str8 = "@welcome to SSSIT!!!"
print(str8.rstrip('!'))  # @welcome to SSSIT

# "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list)
data = ("John", "Doe", 53.44)
# output to be shown : Hello John Doe. Your current balance is $53.44.
format_string = "Hello %s %s. Your current balance is $%s."
# print(format_string % (data[0], data[1], data[2]))
print(format_string % data)
# if one argument specifier is missing, there occurs error : not all arguments converted during string formatting
