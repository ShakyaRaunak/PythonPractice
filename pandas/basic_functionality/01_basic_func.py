# https://www.tutorialspoint.com/python_pandas/python_pandas_basic_functionality.htm

# Series Basic Functionality

import numpy as np
import pandas as pd

# Create a series with 100 random numbers
s = pd.Series(np.random.randn(4))
print(s)
print()

# axes - returns the list of the labels of the series.
print("The axes are:")
print(s.axes)
print()

# empty - returns the Boolean value saying whether the Object is empty or not. True indicates that the object is empty.
print("Is the Object empty?")
print(s.empty)
print()

# ndim - returns the number of dimensions of the object. By definition, a Series is a 1D data structure, so it returns
print("The dimensions of the object:")
print(s.ndim)
print()

# size - returns the size(length) of the series.
print("The size of the object:")
print(s.size)
print()

# values - returns the actual data in the series as an array.
print("The actual data series is:")
print(s.values)
print()

# head() returns the first n rows(observe the index values). The default number of elements to display is five,
# but you may pass a custom number.
print("The first two rows of the data series:")
print(s.head(2))
print()

# tail() returns the last n rows(observe the index values). The default number of elements to display is five,
# but you may pass a custom number.
print("The last two rows of the data series:")
print(s.tail(2))
