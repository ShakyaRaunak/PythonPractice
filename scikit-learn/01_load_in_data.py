# https://www.datacamp.com/community/tutorials/machine-learning-python

"""
The first step to about anything in data science is loading in your data. This discipline typically works with observed
data. This data might be collected by yourself or you can browse through other sources to find data sets.
For now, you just load in the digits data set that comes with a Python library, called scikit-learn.
"""

# Import `datasets` from `sklearn`
from sklearn import datasets

# To load in the data, you import the module datasets from sklearn. Then, you can use the load_digits() method from
# datasets to load in the data:

# Load in the `digits` data
digits = datasets.load_digits()

# Print the `digits` data
print(digits)
