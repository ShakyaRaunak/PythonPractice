"""
It is not possible to sort a dictionary, only to get a representation of a dictionary that is sorted.
Dictionaries are inherently orderless, but other types, such as lists and tuples, are not.
So you need an ordered data type to represent sorted values, which will be a list—probably a list of tuples.
"""

import operator

# How to sort a Python dictionary by value
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
print(sorted_x)  # sorted_x will be a list of tuples sorted by the second element in each tuple. dict(sorted_x) == x.
# OR
z = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
_z = sorted(z.items(), key=lambda z: z[1])  # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
print(_z)

# And to sort based on keys instead of values:
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(0))
print(sorted_x)  # [(0, 0), (1, 2), (2, 1), (3, 4), (4, 3)]

# create a list of dictionary keys after sorting based on dictionary values
y = {'seven': 7, 'four': 4, 'one': 1, 'two': 2, 'five': 5, 'eight': 8}
_y = sorted(y, key=y.get, reverse=True)
print(_y)  # ['eight', 'seven', 'five', 'four', 'two', 'one']
