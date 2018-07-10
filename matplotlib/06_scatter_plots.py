# https://www.tutorialspoint.com/python/python_scatter_plots.htm

"""
Scatterplots show many points plotted in the Cartesian plane. Each point represents the values of two variables.
One variable is chosen in the horizontal axis and another in the vertical axis.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df.plot.scatter(x='a', y='b')
plt.show()
