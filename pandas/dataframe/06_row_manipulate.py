import pandas as pd

d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)
print()

# Rows selection by Label (loc function)
print(df.loc['b'])
print()

# Rows selection by integer location (iloc function)
print(df.iloc[2])
print()

# Slice Rows
# Multiple rows can be selected using ‘ : ’ operator
print(df[2:4])
print()

# Addition of Rows
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a', 'b'])
df = df.append(df2)
print(df)
print()

# Deletion of Rows
# Drop rows with label 0
df = df.drop(0)
print(df)
