# https://www.tutorialspoint.com/numpy/numpy_arithmetic_operations.htm

import numpy as np

a = np.arange(9, dtype=np.float_).reshape(3, 3)

print('First array:')
print(a)
print()

print('Second array:')
b = np.array([10, 10, 10])
print(b)
print()

print('Add the two arrays:')
print(np.add(a, b))
print()

print('Subtract the two arrays:')
print(np.subtract(a, b))
print()

print('Multiply the two arrays:')
print(np.multiply(a, b))
print()

print('Divide the two arrays:')
print(np.divide(a, b))
print()

"""
numpy.reciprocal() - returns the reciprocal of argument, element-wise. For elements with absolute values larger than 1, 
the result is always 0 because of the way in which Python handles integer division. For integer 0, an overflow warning is issued.
"""
a = np.array([0.25, 1.33, 1, 0, 100])

print('Our array is:')
print(a)
print()

print('After applying reciprocal function:')
print(np.reciprocal(a))
print()

b = np.array([100], dtype=int)
print('The second array is:')
print(b)
print()

print('After applying reciprocal function:')
print(np.reciprocal(b))
print()

"""
numpy.power() treats elements in the first input array as base and returns it raised to the power of the corresponding element 
in the second input array.
"""
a = np.array([10, 100, 1000])

print('Our array is:')
print(a)
print()

print('Applying power function:')
print(np.power(a, 2))
print()

print('Second array:')
b = np.array([1, 2, 3])
print(b)
print()

print('Applying power function again:')
print(np.power(a, b))
print()

"""
numpy.mod() - returns the remainder of division of the corresponding elements in the input array. Same as function numpy.remainder().
"""
a = np.array([10, 20, 30])
b = np.array([3, 5, 7])

print('First array:')
print(a)
print()

print('Second array:')
print(b)
print()

print('Applying mod() function:')
print(np.mod(a, b))
print()

print('Applying remainder() function:')
print(np.remainder(a, b))
print()

# Performing operations on array with complex numbers - numpy.real(), numpy.imag(), numpy.conj(), numpy.angle()
a = np.array([-5.6j, 0.2j, 11., 1 + 1j])

print('Our array is:')
print(a)
print()

print('Applying real() function:')
print(np.real(a))  # returns the real part of the complex data type argument
print()

print('Applying imag() function:')
print(np.imag(a))  # returns the imaginary part of the complex data type argument
print()

print('Applying conj() function:')
print(np.conj(a))  # returns the complex conjugate
print()

print('Applying angle() function:')
print(np.angle(a))  # returns the angle of the complex argument
print()

print('Applying angle() function again (result in degrees)')
print(np.angle(a, deg=True))
