# https://www.learnpython.org/en/Pandas_Basics
import pandas as pd

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98]}

brics = pd.DataFrame(dict)
print(brics)
# Pandas has assigned a key for each country as the numerical values 0 through 4.
print()

# If you would like to have different index values, say, the two letter country code, here's how you can do it.
# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out brics with new index values
print(brics)
