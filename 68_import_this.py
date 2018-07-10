# https://stackoverflow.com/questions/5855758/what-is-the-source-code-of-the-this-module-doing
import this

"""
This is called rot13 encoding:
ROT13 ("rotate by 13 places", sometimes hyphenated ROT-13) is a simple letter substitution cipher that replaces a letter 
with the 13th letter after it, in the alphabet. ROT13 is a special case of the Caesar cipher which was developed in 
ancient Rome.

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)
Builds the translation table, for both uppercase (this is what 65 is for) and lowercase (this is what 97 is for) chars.

print "".join([d.get(c, c) for c in s])
Prints the translated string.
"""
