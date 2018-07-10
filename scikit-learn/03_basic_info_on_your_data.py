# https://www.datacamp.com/community/tutorials/machine-learning-python

# Optical Recognition of Handwritten Digits Data Set

from sklearn import datasets
import numpy as np

# Load in the `digits` data
digits = datasets.load_digits()

# To see which keys you have available to already get to know your data, you can just run digits.keys().
print(digits.keys())  # Gets the keys of the `digits` data
print('----------------------------------------------------------')

# You can access the digits data through the attribute data.
print(digits.data)  # Prints out the data
print('----------------------------------------------------------')

# You can also access the target values or labels through the target attribute.
print(digits.target)  # Prints out the target values
print('----------------------------------------------------------')

# You can also access the description through the DESCR attribute.
print(digits.DESCR)  # Prints out the description of the `digits` data
print('----------------------------------------------------------')

# Isolate the `digits` data
digits_data = digits.data

# Inspect the shape
print(digits_data.shape)
# You see that there are 1797 samples and that there are 64 features.
print('----------------------------------------------------------')

# Isolate the target values with `target`
digits_target = digits.target

# Inspect the shape
print(digits_target.shape)
# Because you have 1797 samples, you also have 1797 target values.
print('----------------------------------------------------------')

# Print the number of unique labels
number_digits = len(np.unique(digits.target))
print(number_digits)  # 10
# All the target values contain 10 unique values, namely, from 0 to 9. In other words, all 1797 target values are
# made up of numbers that lie between 0 and 9.
# This means that the digits that your model will need to recognize are numbers from 0 to 9.
print('----------------------------------------------------------')

# Isolate the `images`
digits_images = digits.images

# Inspect the shape
print(digits_images.shape)
# You see that the images data contains three dimensions: there are 1797 instances that are 8 by 8 pixels big.
