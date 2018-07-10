# https://www.tutorialspoint.com/python/python_time_series.htm

"""
Time series is a series of data points in which each data point is associated with a timestamp. A simple example is the price of a stock
at different points of time on a given day.
Here, we take the value of stock prices every day for a quarter for a particular stock symbol. We capture these values as a csv file and
then organize them to a dataframe using pandas library. We then set the date field as index of the dataframe by recreatingthe additional
Valuedate column as index and deleting the old valuedate column.
"""

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('stocks.csv')
df = pd.DataFrame(data, columns=['ValueDate', 'Price'])

# Set the Date as Index
df['ValueDate'] = pd.to_datetime(df['ValueDate'])
df.index = df['ValueDate']
del df['ValueDate']

df.plot(figsize=(15, 6))
plt.show()
