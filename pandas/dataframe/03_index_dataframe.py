# Import pandas and cars.csv
import pandas as pd

cars = pd.read_csv('cars.csv', index_col=0)

# Print out country column as Pandas Series
print(cars['cars_per_cap'])
print()

# Print out country column as Pandas DataFrame
print(cars[['cars_per_cap']])
print()

# Print out DataFrame with country and drives_right columns
print(cars[['cars_per_cap', 'country']])
print()

# access observations (rows) from a DataFrame
# Print out first 4 observations
print(cars[0:4])
print()

# Print out fifth, sixth, and seventh observation
print(cars[4:6])

