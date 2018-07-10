# https://www.tutorialspoint.com/python/python_linear_regression.htm

"""
In Linear Regression, two variables are related through an equation, where exponent (power) of both these variables is 1.
A non-linear relationship where the exponent of any variable is not equal to 1 creates a curve.
The functions in Seaborn to find the linear regression relationship is regplot.
"""

import seaborn as sb
from matplotlib import pyplot as plt

df = sb.load_dataset('tips')
sb.regplot(x="total_bill", y="tip", data=df)
plt.show()
