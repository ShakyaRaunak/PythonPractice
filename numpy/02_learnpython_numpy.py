# https://www.learnpython.org/en/Numpy_Arrays

"""
Convert the list of weights to a Numpy array. Then, convert all of the weights from kilograms to pounds.
Use the scalar conversion of 2.2 lbs per kilogram to make your conversion.
"""

import numpy as np

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg * 2.2

# Print out np_weight_lbs
print(np_weight_lbs)