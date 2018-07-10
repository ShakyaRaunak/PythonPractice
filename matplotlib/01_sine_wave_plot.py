# https://www.tutorialspoint.com/python/python_matplotlib.htm

"""
Matplotlib is a python library used to create 2D graphs and plots by using a module named pyplot.
"""

# Example to produce the sine wave plot using matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
plt.title("sine wave form")

# Plot the points using matplotlib
plt.plot(x, y)
plt.show()
