# https://www.tutorialspoint.com/scipy/scipy_integrate.htm

import scipy.integrate
from numpy import exp

# Example 1 :
"""
The general form of quad is scipy.integrate.quad(f, a, b), where ‘f’ is the name of the function to be integrated, 
whereas, ‘a’ and ‘b’ are the lower and upper limits, respectively.
"""
# define the function f(x)=e−x2
f = lambda x: exp(-x ** 2)
i = scipy.integrate.quad(f, 0, 1)
print(i)  # (0.7468241328124271, 8.291413475940725e-15)
# The quad function returns the two values, in which the first number is the value of integral and
# the second value is the estimate of the absolute error in the value of integral.

# Example 2 :
"""
The general form of dblquad is scipy.integrate.dblquad(func, a, b, gfun, hfun) where, func is the name of the function to be integrated, 
‘a’ and ‘b’ are the lower and upper limits of the x variable, respectively, while gfun and hfun are the names of the functions 
that define the lower and upper limits of the y variable.
"""
from math import sqrt

f = lambda x, y: 16 * x * y
g = lambda x: 0
h = lambda y: sqrt(1 - 4 * y ** 2)
i = scipy.integrate.dblquad(f, 0, 0.5, g, h)
print(i)  # (0.5, 1.7092350012594845e-14)
