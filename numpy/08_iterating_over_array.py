# https://www.tutorialspoint.com/numpy/numpy_iterating_over_array.htm

"""
NumPy package contains an iterator object numpy.nditer. It is an efficient multidimensional iterator object using which
it is possible to iterate over an array.
"""

import numpy as np

# # Example 1 : Create a 3X4 array using arange() function and iterate over it using nditer.
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)

print('Original array is:')
print(a)
print()

print('Modified array is:')
for x in np.nditer(a):
    print(x, end=' ')
print('\n')

# Example 2 : The order of iteration is chosen to match the memory layout of an array, without considering a particular ordering.
print('Transpose of the original array is:')
b = a.T
print(b)
print()

print('Modified array is:')
for x in np.nditer(b):
    print(x, end=' ')
print('\n')

# Iteration Order - If the same elements are stored using F-style order, the iterator chooses the more efficient way of
# iterating over an array.
# Example 3 :
print('Sorted in C-style order:')
c = b.copy(order='C')
print(c)
for x in np.nditer(c):
    print(x, end=' ')
print('\n')

print('Sorted in F-style order:')
c = b.copy(order='F')
print(c)
for x in np.nditer(c):
    print(x, end=' ')
print('\n')

# Example 4 : It is possible to force nditer object to use a specific order by explicitly mentioning it.
print('Sorted in C-style order:')
for x in np.nditer(a, order='C'):
    print(x, end=' ')
print('\n')

print('Sorted in F-style order:')
for x in np.nditer(a, order='F'):
    print(x, end=' ')
print()

# Modifying Array Values - The nditer object has another optional parameter called op_flags. Its default value is read-only,
# but can be set to read-write or write-only mode. This will enable modifying array elements using this iterator.
# Example 5 :
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2 * x
print('Modified array is:')
print(a)
print()

# External Loop - The nditer class constructor has a ‘flags’ parameter.
# Example 6 : here, one-dimensional arrays corresponding to each column is traversed by the iterator.
print('Modified array is:')
for x in np.nditer(a, flags=['external_loop'], order='F'):
    print(x, end=' ')
print('\n')

# Broadcasting Iteration - If two arrays are broadcastable, a combined nditer object is able to iterate upon them concurrently.
# Example 7 : Assuming that an array a has dimension 3X4, and there is another array b of dimension 1X4, the iterator of
# following type is used (array b is broadcast to size of a).
print('First array is:')
print(a)
print()

print('Second array is:')
b = np.array([1, 2, 3, 4], dtype=int)
print(b)
print()

print('Modified array is:')
for x, y in np.nditer([a, b]):
    print("%d:%d" % (x, y), end=' ')
