# https://stackoverflow.com/questions/1228299/change-one-character-in-a-string
# Python strings are immutable. Work with them as lists; turn them into strings only when needed.
import timeit

str = "Hello Zorld"

# Method 1 : Which is pretty slow compared to 'Method 2'
lst = list(str)
# print(listFromStr)  # ['H', 'e', 'l', 'l', 'o', ' ', 'z', 'o', 'r', 'l', 'd']
lst[6] = 'W'
# print(listFromStr)  # ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
newStr = ''.join(lst)
print(newStr)  # 'Hello World'
print(timeit.timeit("str = 'Hello Zorld'; s = list(str); s[6] = 'W'; ''.join(s)", number=1000000))  # 0.7625341324221091

# Method 2 : FAST METHOD
print('str[:6] : {}, str[7:] : {}'.format(str[:6], str[7:]))
newStr = str[:6] + 'W' + str[7:]
print(newStr)
print(timeit.timeit("str = 'Hello Zorld'; updatedStr = str[:6] + 'W' + str[7:]", number=1000000))  # 0.3791864780586043

# Method 3 : Using byte array (SLOWEST METHOD)
print(timeit.timeit("s = 'Hello Zorld'; b_str = bytearray(s, 'utf-8'); b_str[6:7] = b'W'; str(b_str, 'utf-8')",
                    number=1000000))  # 1.2540746514344885

print("------------------------------------")

# https://www.pythoncentral.io/pythons-string-replace-method-replacing-python-strings/

"""
The prototype of the string.replace() method is as follows: string.replace(s, old, new[, maxreplace])

Function parameters
s: The string to search and replace from.
old: The old sub-string you wish to replace.
new: The new sub-string you wish to put in-place of the old one.
maxreplace: The maximum number of times you wish to replace the sub-string.
"""

# modify the contents by replacing one piece of text with another
our_str = 'Hello World'

new_str = our_str.replace('World', 'Jackson')
print(new_str)  # Hello Jackson

new_str = our_str.replace('Hello', 'Hello,')
print(new_str)  # Hello, World

our_str = 'Hello you, you and you!'
new_str = our_str.replace('you', 'me', 1)
print(new_str)  # Hello me, you and you!
new_str = our_str.replace('you', 'me', 2)
print(new_str)  # Hello me, me and you!
new_str = our_str.replace('you', 'me', 3)
print(new_str)  # Hello me, me and me!
