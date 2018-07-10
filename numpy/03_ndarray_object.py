# https://www.tutorialspoint.com/numpy/numpy_ndarray_object.htm

"""
The most important object defined in NumPy is an N-dimensional array type called ndarray. It describes the collection of items
of the same type. Items in the collection can be accessed using a zero-based index.

Every item in an ndarray takes the same size of block in the memory. Each element in ndarray is an object of data-type object
(called dtype).
"""

import numpy as np

a = np.array([1, 2, 3])
print(a)

# more than one dimensions
a = np.array([[1, 2], [3, 4]])
print(a)

# minimum dimensions
a = np.array([1, 2, 3, 4, 5], ndmin=2)
print(a)

# dtype parameter
a = np.array([1, 2, 3], dtype=complex)
print(a)
