# https://www.tutorialspoint.com/scipy/scipy_interpolate.htm

"""
Interpolation is the process of finding a value between two points on a line or a curve.
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 4, 12)
y = np.cos(x ** 2 / 3 + 4)
print(x, y)

plt.plot(x, y)
plt.show()

from scipy.interpolate import interp1d

"""
The interp1d class in the scipy.interpolate is a convenient method to create a function based on fixed data points, 
which can be evaluated anywhere within the domain defined by the given data using linear interpolation.
"""
f1 = interp1d(x, y, kind='linear')
f2 = interp1d(x, y, kind='cubic')
# We created two functions f1 and f2 which, for a given input x returns y. The third variable represents the interpolation technique.

xnew = np.linspace(0, 4, 30)
plt.plot(x, y, 'o', xnew, f1(xnew), '-', xnew, f2(xnew), '--')
# 'Linear', 'Nearest', 'Zero', 'Slinear', 'Quadratic', 'Cubic' are a few techniques of interpolation.
plt.legend(['data', 'linear', 'cubic', 'nearest'], loc='best')
plt.show()
