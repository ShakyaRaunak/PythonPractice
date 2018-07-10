"""
Python’s built-in enumerate function allows us to loop over a list and retrieve both the index and
the value of each item in the list.
"""

presidents = ["Donald Trump", "Ronald Reagan", "John F Kennedy", "Richard Nixon", "George W Bush"]
for num, name in enumerate(presidents, start=1):  # remove start=1 will start counting at 0 by default
    print("{}. {}".format(num, name))
print()

#  looping over two lists at the same time using indexes to look up corresponding elements
religions = ["Christian", "Unaffiliated", "Jewish", "Buddhist", "Hindu", "Muslim"]
proportions = [0.7, 0.26, 0.01, 0.01, 0.01, 0.01]
for i, religion in enumerate(religions):
    proportion = proportions[i]
    print("{} -> {} %".format(religion, proportion * 100))
