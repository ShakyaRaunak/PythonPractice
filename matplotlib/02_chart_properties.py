# https://www.tutorialspoint.com/python/python_chart_properties.htm

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10)
y = x ^ 2

# Labeling the Axes and Title
plt.title("Graph Drawing")
plt.xlabel("Time")
plt.ylabel("Distance")

# Simple Plot
# plt.plot(x, y)
# plt.show()

# Formatting the line colors
plt.plot(x, y, 'r')

# Formatting the line type
plt.plot(x, y, '>')
# plt.show() # only after savefig operation otherwise you get empty pdf / png file or one with no title and labels

# save in pdf formats
plt.savefig('timevsdist.pdf')
plt.savefig('timevsdist.png')

plt.show()
