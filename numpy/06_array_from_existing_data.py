# https://www.tutorialspoint.com/numpy/numpy_array_from_existing_data.htm

import numpy as np

x = [1, 2, 3]
a = np.asarray(x)  # convert list to ndarray
print(a)  # [1 2 3]

a = np.asarray(x, dtype=float)  # dtype is set
print(a)  # [1. 2. 3.]

# ndarray from tuple
a = np.asarray(x)
print(a)  # [1 2 3]

# ndarray from list of tuples
x = [(1, 2, 3), (4, 5)]
a = np.asarray(x)
print(a)  # [(1, 2, 3) (4, 5)]

# numpy.frombuffer
# In PY3, the default string type is unicode. The b is used to create and display bytestrings.
a = np.frombuffer(b'hello world', dtype='S1')
print(a)  # [b'h' b'e' b'l' b'l' b'o' b' ' b'w' b'o' b'r' b'l' b'd']

# numpy.fromiter
list = range(5)  # create list object using range function
it = iter(list)  # obtain iterator object from list
x = np.fromiter(it, dtype=float)  # use iterator to create ndarray
print(x)  # [0. 1. 2. 3. 4.]
