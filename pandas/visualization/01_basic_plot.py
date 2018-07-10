import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(10, 4), index=pd.date_range('1/1/2000', periods=10), columns=list('ABCD'))

# basic plot
df.plot()
plt.show()

df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
# bar plot
df.plot.bar()
plt.show()

# stacked bar plot
df.plot.bar(stacked=True)
plt.show()

# horizontal bar plot
df.plot.barh(stacked=True)
plt.show()

# histogram
df = pd.DataFrame({'a': np.random.randn(1000) + 1, 'b': np.random.randn(1000), 'c': np.random.randn(1000) - 1},
                  columns=['a', 'b', 'c'])

df.plot.hist(bins=20)
plt.show()

# plot different histograms for each column
df.diff().hist(bins=20)
plt.show()

# box plot
df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.plot.box()
plt.show()

# area plot
df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df.plot.area()
plt.show()

# scatter plot
df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df.plot.scatter(x='a', y='b')
plt.show()

# pie chart
df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
df.plot.pie(subplots=True)
plt.show()
