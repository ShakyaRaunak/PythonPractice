# https://www.tutorialspoint.com/python/python_3d_charts.htm

import matplotlib.pyplot as plt
# 3D plot is drawn by mpl_toolkits.mplot3d.
from mpl_toolkits.mplot3d import axes3d

chart = plt.figure()
# 3D chart involves adding a subplot to an existing two-dimensional plot and assigning the projection parameter as 3d.
chart3d = chart.add_subplot(111, projection='3d')

# Create some test data.
X, Y, Z = axes3d.get_test_data(0.08)

# Plot a wireframe.
chart3d.plot_wireframe(X, Y, Z, color='r', rstride=15, cstride=10)

plt.show()
