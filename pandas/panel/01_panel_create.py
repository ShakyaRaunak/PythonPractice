# creating an empty panel
import pandas as pd
import numpy as np

# Create an Empty Panel
p = pd.Panel()
print(p)
print()

# From 3D ndarray
data = np.random.rand(2, 4, 5)
p = pd.Panel(data)
print(p)
print()

# From dict of DataFrame Objects
data = {'Item1': pd.DataFrame(np.random.randn(4, 3)), 'Item2': pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p)
