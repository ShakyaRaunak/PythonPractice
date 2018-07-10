# https://www.tutorialspoint.com/python/python_measuring_central_tendency.htm

"""
Mathematically central tendency means measuring the center or distribution of location of values of a data set.
Three main measures of central tendency - mean, median and mode.
"""

import pandas as pd

# Create a Dictionary of series
d = {'Name': pd.Series(
    ['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Steve', 'Jack', 'Lee', 'Steve', 'Gasper', 'Naviya', 'Andres']),
    'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 25, 46]),
    'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 2.56, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}

# Create a DataFrame
df = pd.DataFrame(d)

# The pandas functions can be directly used to calculate these values.
print("Mean Values in the Distribution")
print(df.mean())
print("*******************************")
print("Median Values in the Distribution")
print(df.median())
print("*******************************")
print("Mode Values in the Distribution")
# Mode may or may not be available in a distribution depending on whether there are values with maximum frquency.
print(df.mode())
