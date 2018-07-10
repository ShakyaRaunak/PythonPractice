# https://www.scipy-lectures.org/packages/scikit-image/index.html

"""
scikit-image is a collection of algorithms for image processing. It is a Python package dedicated to image processing,
and using natively NumPy arrays as image objects.
"""

import matplotlib.pyplot as plt
import numpy as np

check = np.zeros((9, 9))
check[::2, 1::2] = 1
check[1::2, ::2] = 1

plt.imshow(check, cmap='gray', interpolation='nearest')
plt.show()
