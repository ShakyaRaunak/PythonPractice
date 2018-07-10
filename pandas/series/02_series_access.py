import pandas as pd

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

# Accessing Data from Series with Position
# retrieve the first element
print(s[0])  # 1
print()

# retrieve the first three element
print(s[:3])
print()

# retrieve the last three element
print(s[-3:])
print()

# Retrieve Data Using Label (Index)
# retrieve a single element
print(s['a'])  # 1
print()

# retrieve multiple elements
print(s[['a', 'c', 'd']])
print()

# retrieve multiple elements
# print(s['f']) # error
