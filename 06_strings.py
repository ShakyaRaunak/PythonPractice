# Python Strings are immutable sequences of Unicode points.

string1 = 'hello'
string2 = "hello"  # same as using ''

# two ways to create Multiline Strings:
string3 = "hello \n\
 \
world"
print(string3)

string4 = """hello
world"""
print(string4)

# Concatenation of strings
s1 = "Hello "
s2 = "World"
print(s1 + s2)
# print(s1 + 123) -> error because both the operands passed for concatenation must be of same type.

# String Replication Operator * - used to repeat a string number of times
print(s1 * 5)  # Hello Hello Hello Hello Hello
print(5 * s1)  # Hello Hello Hello Hello Hello

# Relational Operators
print("RAJAT" == "RAJAT")  # True
print("afsha" >= 'Afsha')  # True
# deprecated -> print("Z" <> "z")
print("Z" != "z")  # True

# String Slice
str = "Raunak"
print(str[0:6])  # Raunak
print(str[0:3])  # Rau
print(str[2:5])  # una
print(str[:6])  # Raunak
print(str[3:])  # nak

myString = "Hello world!"
print(myString[3:7])  # lo w
print(myString[3:7:1])  # lo w

# This prints the characters of string from 3 to 7 skipping one character. This is extended slice syntax.
# The general form is [start:stop:step]
print(myString[3:7:2])  # l

# This reverses a string.
print(myString[::-1])  # !dlrow olleH

print(myString.count("l"))  # 3

print(str[:3] + str[3:])  # Raunak

print("String: %s" % str)

# Cannot concatenate string to an integer using + operator
myInt = 10
# print(myInt + myString)  # produces error

# uppercase and lowercase
print(myString.upper())  # HELLO WORLD!
print(myString.lower())  # hello world!
print(myString.swapcase())  # hELLO WORLD!

print(' '.join(reversed(myString)))  # ! d l r o w   o l l e H

print(myString.startswith("Hello"))  # True
print(myString.endswith("asdf"))  # False

print(myString.split(" "))  # ['Hello', 'world!']

# Python string strip / trim
str = "abc    xyz    abc"
newStr = str.strip("abc")  # output :     xyz
print(newStr)  # output :     xyz
print(newStr.strip())  # removes characters (default white-space) from both ends
print(newStr.lstrip())  # removes leading characters (default white-space)
print(newStr.rstrip())  # removes trailing characters (default white-space)
