# https://www.tutorialspoint.com/python_pandas/index.htm
# import the pandas library and aliasing as pd
import pandas as pd

# Create an Empty Series
s = pd.Series()
print(s)  # Series([], dtype: float64)
print()

# Create a Series from ndarray
import numpy as np

# method one
data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)
print(s)
print()

# method two
data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data, index=[100, 101, 102, 103])
print(s)
print()

# Create a Series from dict
data = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(data)
print(s)
print()

data = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(data, index=['b', 'c', 'd', 'a'])
print(s)
print()

# Create a Series from Scalar
s = pd.Series(5, index=[0, 1, 2, 3])
print(s)
