# https://www.tutorialspoint.com/numpy/numpy_array_attributes.htm

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)  # (2, 3)

# ndarray.shape returns a tuple consisting of array dimensions and also used to resize the ndarray.
a.shape = (3, 2)
print(a)

a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.reshape(3, 2)
print(b)

# ndarray.ndim returns the number of array dimensions.
# an array of evenly spaced numbers
a = np.arange(24)
print(a)

# this is one dimensional array
a = np.arange(24)
print(a.ndim)

# now reshape it
b = a.reshape(2, 4, 3)
print(b)
# b is having three dimensions

# numpy.itemsize returns the length of each element of array in bytes.
# dtype of array is int8 (1 byte)
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(x.itemsize)

# dtype of array is now float32 (4 bytes)
x = np.array([1, 2, 3, 4, 5], dtype=np.float32)
print(x.itemsize)

# numpy.flags
x = np.array([1, 2, 3, 4, 5])
print(x.flags)
