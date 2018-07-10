# Selecting the Data from Panel
import pandas as pd
import numpy as np

data = {'Item1': pd.DataFrame(np.random.randn(4, 3)), 'Item2': pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)

# Using Items
print(p['Item1'])
print()

# Using major_axis
print(p.major_xs(1))
print()

# Using minor_axis
print(p.minor_xs(1))
