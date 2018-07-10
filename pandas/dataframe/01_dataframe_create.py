# https://www.tutorialspoint.com/python_pandas/index.htm
# import the pandas library and aliasing as pd
import pandas as pd

# Create an Empty DataFrame
df = pd.DataFrame()
print(df)
print()

# Create a DataFrame from Lists
# method one
data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data)
print(df)
print()

# method two
data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)
print()

# method three
df = pd.DataFrame(data, columns=['Name', 'Age'], dtype=float)
print(df)
print()

# Create a DataFrame from Dict of ndarrays / Lists
data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28, 34, 29, 42]}
# method one
df = pd.DataFrame(data)
print(df)
print()

# method two
df = pd.DataFrame(data, index=['rank1', 'rank2', 'rank3', 'rank4'])
print(df)

# Create a DataFrame from List of Dicts
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
# method one
df = pd.DataFrame(data)
print(df)
print()

# method two
df = pd.DataFrame(data, index=['first', 'second'])
print(df)
print()

# method three
# With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])

# With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print(df1)
print(df2)
print()

# Create a DataFrame from Dict of Series
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)
