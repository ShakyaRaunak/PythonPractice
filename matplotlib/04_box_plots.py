# https://www.tutorialspoint.com/python/python_box_plots.htm

"""
Boxplots are a measure of how well distributed the data in a data set is. It divides the data set into three quartiles.
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.plot.box(grid='True')
plt.show()
