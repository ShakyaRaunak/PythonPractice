# https://www.tutorialspoint.com/python_pandas/python_pandas_basic_functionality.htm

# DataFrame Basic Functionality

import pandas as pd

# Create a Dictionary of series
d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8])}

# Create a DataFrame
df = pd.DataFrame(d)
print("Our data series is:")
print(df)
print()

# T (Transpose) - Returns the transpose of the DataFrame.
print("The transpose of the data series is:")
print(df.T)
print()

# axes - Returns the list of row axis labels and column axis labels.
print("Row axis labels and column axis labels are:")
print(df.axes)
print()

# dtypes - Returns the data type of each column.
print("The data types of each column are:")
print(df.dtypes)
print()

# empty - Returns the Boolean value saying whether the Object is empty or not; True indicates that the object is empty.
print("Is the object empty?")
print(df.empty)
print()

# ndim - Returns the number of dimensions of the object. By definition, DataFrame is a 2D object.
print("The dimension of the object is:")
print(df.ndim)
print()

# shape - Returns a tuple representing the dimensionality of the DataFrame.
# Tuple (a,b), where a represents the number of rows and b represents the number of columns.
print("The shape of the object is:")
print(df.shape)
print()

# size - Returns the number of elements in the DataFrame.
print("The total number of elements in our object is:")
print(df.size)
print()

# values - Returns the actual data in the DataFrame as an NDarray.
print("The actual data in our data frame is:")
print(df.values)
print()

# head() returns the first n rows (observe the index values). The default number of elements to display is five,
# but you may pass a custom number.
print("The first two rows of the data frame is:")
print(df.head(2))
print()

# tail() returns the last n rows (observe the index values). The default number of elements to display is five,
# but you may pass a custom number.
print("The last two rows of the data frame is:")
print(df.tail(2))
