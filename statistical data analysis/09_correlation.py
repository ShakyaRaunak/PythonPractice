# https://www.tutorialspoint.com/python/python_correlation.htm

"""
Correlation refers to some statistical relationships involving dependence between two data sets.

We take example of the iris data set available in seaborn python library. We try to establish the correlation between
the length and the width of the sepals and petals of three species of iris flower. Based on the correlation found,
a strong model could be created which easily distinguishes one species from another.
"""

import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('iris')

# without regression
sns.pairplot(df, kind="scatter")
plt.show()
