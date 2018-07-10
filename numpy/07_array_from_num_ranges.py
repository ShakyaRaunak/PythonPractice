# https://www.tutorialspoint.com/numpy/numpy_array_from_numerical_ranges.htm

import numpy as np

# numpy.arange returns an ndarray object containing evenly spaced values within a given range.
# numpy.arange(start, stop, step, dtype)
x = np.arange(5)
print(x)  # [0 1 2 3 4]

# dtype set
x = np.arange(5, dtype=float)
print(x)  # [0. 1. 2. 3. 4.]

# start and stop parameters set
x = np.arange(10, 20, 2)
print(x)  # [10 12 14 16 18]

# numpy.linspace - similar to arange() but instead of step size, the number of evenly spaced values between the interval is specified.
x = np.linspace(10, 20, 5)
print(x)  # [10.  12.5 15.  17.5 20. ]

# endpoint set to false
x = np.linspace(10, 20, 5, endpoint=False)
print(x)  # [10. 12. 14. 16. 18.]

# find retstep value
x = np.linspace(1, 2, 5, retstep=True)
print(x)  # (array([1.  , 1.25, 1.5 , 1.75, 2.  ]), 0.25) : here, retstep is 0.25

# numpy.logspace - returns an ndarray object that contains the numbers that are evenly spaced on a log scale.
# Start and stop endpoints of the scale are indices of the base, default base is 10.
a = np.logspace(1.0, 2.0, num=10)
print(a)

# set base of log space to 2
a = np.logspace(1, 10, num=10, base=2)
print(a)
