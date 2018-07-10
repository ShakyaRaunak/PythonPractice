"""
Python’s zip function allows us to loop over multiple lists at the same time.

The zip function takes multiple lists and returns an iterable that provides a tuple of the
corresponding elements of each list as we loop over it.
Note that zip with different size lists will stop after the shortest list runs out of items.
"""

religions = ["Christian", "Unaffiliated", "Jewish", "Buddhist", "Hindu", "Muslim"]
proportions = [0.7, 0.26, 0.01, 0.01, 0.01, 0.01]
for religion, proportion in zip(religions, proportions):
    print("{} -> {} %".format(religion, proportion * 100))

headers = [1, 2, 3]
columns = [11, 22, 33]
for header, col in zip(headers, columns):
    print("{}: {}".format(header, ", ".join(str(col))))
