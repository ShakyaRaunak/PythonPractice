# https://www.tutorialspoint.com/python/python_chart_styling.htm

import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 10)
y = x ^ 2
z = x ^ 3
t = x ^ 4

# Labeling the Axes and Title
plt.title("Graph Drawing")
plt.xlabel("Time")
plt.ylabel("Distance")
plt.plot(x, y)

# Annotate the chart by highlighting the specific locations of the chart to indicate the sharp change in values at those points
plt.annotate(xy=[2, 1], s='Second Entry')
plt.annotate(xy=[4, 6], s='Third Entry')

# Adding Legends to represent the meaning associated with each line
plt.plot(x, z)
plt.plot(x, t)
plt.legend(['Race1', 'Race2', 'Race3'], loc=4)

# Style the background
plt.style.use('fast')
plt.plot(x, z)
plt.show()
