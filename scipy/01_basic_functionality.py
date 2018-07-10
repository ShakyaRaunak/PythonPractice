# https://www.tutorialspoint.com/scipy/scipy_basic_functionality.htm
import numpy as np

# Converting Python array-like objects to NumPy Vector
list = [1, 2, 3, 4]
arr = np.array(list)
print(arr)
print()

# Using zeros()
print(np.zeros((2, 3)))
print()

# Using ones()
print(np.ones((2, 3)))
print()

# arange() function will create arrays with regularly incrementing values.
print(np.arange(7))

# Defining the data type of the values
arr = np.arange(2, 10, dtype=np.float)
print(arr)
print("Array Data Type :", arr.dtype)

# linspace() function will create arrays with a specified number of elements, which will be spaced equally between
# the specified beginning and end values.
print(np.linspace(1., 4., 6))

# Create a matrix
matrix = np.matrix('1 2; 3 4')
conjugate_transpose_of_matrix = matrix.H
print(conjugate_transpose_of_matrix)
print()

transpose_of_matrix = matrix.T
print(transpose_of_matrix)
