# https://www.tutorialspoint.com/scipy/scipy_constants.htm

"""
SciPy constants package provides a wide range of constants, which are used in the general scientific area.
"""

from math import pi as mathpi

import scipy.constants
from scipy.constants import G
from scipy.constants import Planck
from scipy.constants import golden
from scipy.constants import pi as scipypi
from scipy.constants import speed_of_light

print("sciPy pi => %.16f" % scipypi)
print("math pi => %.16f" % mathpi)
print('golden ratio => ', golden)
print('Speed of light in vacuum => ', speed_of_light)
print('Planck constant => ', Planck)
print('Newton’s gravitational constant => ', G)
print()

# The easy way to get which key is for which function is with the scipy.constants.find() method.
res = scipy.constants.find("alpha particle mass")
print(res)
