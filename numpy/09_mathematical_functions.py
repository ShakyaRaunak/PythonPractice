# https://www.tutorialspoint.com/numpy/numpy_mathematical_functions.htm

# Trigonometric Functions - NumPy has standard trigonometric functions which return trigonometric ratios for a given angle in radians.
import numpy as np

# Example 1 :
a = np.array([0, 30, 45, 60, 90])

print('Sine of different angles:')
# Convert to radians by multiplying with pi/180
print(np.sin(a * np.pi / 180))
print()

print('Cosine values for angles in array:')
print(np.cos(a * np.pi / 180))
print()

print('Tangent values for given angles:')
print(np.tan(a * np.pi / 180))
print()

# Example 2 : arcsin, arcos, and arctan functions return the trigonometric inverse of sin, cos, and tan of the given angle.
# The result of these functions can be verified by numpy.degrees() function by converting radians to degrees.
print('Array containing sine values:')
sin = np.sin(a * np.pi / 180)
print(sin)
print()

print('Compute sine inverse of angles. Returned values are in radians.')
inv = np.arcsin(sin)
print(inv)
print()

print('Check result by converting to degrees:')
print(np.degrees(inv))
print()

print('arccos and arctan functions behave similarly:')
cos = np.cos(a * np.pi / 180)
print(cos)
print()

print('Inverse of cos:')
inv = np.arccos(cos)
print(inv)
print()

print('In degrees:')
print(np.degrees(inv))
print()

print('Tan function:')
tan = np.tan(a * np.pi / 180)
print(tan)
print()

print('Inverse of tan:')
inv = np.arctan(tan)
print(inv)
print()

print('In degrees:')
print(np.degrees(inv))
print()

# Functions for Rounding
# Example 3 :
a = np.array([1.0, 5.55, 123, 0.567, 25.532])

print('Original array:')
print(a)
print()

# numpy.around() returns the value rounded to the desired precision.
print('After rounding:')
print(np.around(a))
print(np.around(a, decimals=1))
print(np.around(a, decimals=-1))
print()

# Example 4 :
a = np.array([-1.7, 1.5, -0.2, 0.6, 10])

print('The given array:')
print(a)
print()

# numpy.floor() returns the largest integer not greater than the input parameter. The floor of the scalar x is the largest integer i,
# such that i <= x. Note that in Python, flooring always is rounded away from 0.
print(np.floor(a))
print()

# numpy.ceil() returns the ceiling of an input value, i.e. the ceil of the scalar x is the smallest integer i, such that i >= x.
print(np.ceil(a))
