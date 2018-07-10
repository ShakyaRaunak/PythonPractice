# https://www.datacamp.com/community/tutorials/machine-learning-python

import pandas as pd

# Load in the data with `read_csv()`
digits = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tra", header=None)

# Print out `digits`
print(digits)

"""
Note that if you download the data like this, the data is already split up in a training and a test set, indicated by 
the extensions .tra and .tes. Here, you only load in the training set.
"""
