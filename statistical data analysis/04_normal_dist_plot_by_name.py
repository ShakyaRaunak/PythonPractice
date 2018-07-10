# https://stackoverflow.com/questions/41768629/normal-distribution-plot-by-name-from-pandas-dataframe

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Normal Distribution Plot by name from pandas dataframe
np.random.seed([3, 1415])
df = pd.DataFrame(dict(
    Name='matt joe adam farley'.split() * 100,
    Seconds=np.random.randint(4000, 5000, 400)
))

df['Zscore'] = df.groupby('Name').Seconds.apply(lambda x: x.div(x.mean()))

df.groupby('Name').Zscore.plot.kde()
plt.show()

# split out plots
g = df.groupby('Name').Zscore
n = g.ngroups
fig, axes = plt.subplots(n // 2, 2, figsize=(6, 6), sharex=True, sharey=True)
for i, (name, group) in enumerate(g):
    r, c = i // 2, i % 2
    group.plot.kde(title=name, ax=axes[r, c])
fig.tight_layout()
plt.show()

# kde + hist
g = df.groupby('Name').Zscore
n = g.ngroups
fig, axes = plt.subplots(n // 2, 2, figsize=(6, 6), sharex=True, sharey=True)
for i, (name, group) in enumerate(g):
    r, c = i // 2, i % 2
    a1 = axes[r, c]
    a2 = a1.twinx()
    group.plot.hist(ax=a2, alpha=.3)
    group.plot.kde(title=name, ax=a1, c='r')
fig.tight_layout()
plt.show()
