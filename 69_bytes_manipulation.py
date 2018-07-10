# https://www.w3resource.com/python/python-bytes.php

"""
bytes objects are immutable sequences of integers, each value in the sequence whereas,
string objects are immutable sequences of unicode characters.
"""

nyString = "Hello Zorld"
bytearray_str = bytearray(nyString, "utf-8")
print(bytearray_str)  # bytearray(b'Hello Zorld')

# update the string
bytearray_str[6:7] = b"W"

# append a new character to the bytearray
# bytearray_str.append(65)  # only takes an integer; cannot have a string or a character

newString = bytearray_str.decode("utf-8")
# OR
# newString = str(bytearray_str, "utf-8")

print(newString)  # Hello World
