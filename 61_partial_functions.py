# https://www.learnpython.org/en/Partial_functions
from functools import partial


def multiply(x, y):
    return x * y  # x: 2, y: 4


# create a new function that multiplies by 2
dbl = partial(multiply, 2)
print(dbl(4))  # 8


# Example : call partial() and replace the first three variables in func(). Then print with the new partial function using
# only one input variable so that the output equals 60.
def func(u, v, w, x):
    return u * 4 + v * 3 + w * 2 + x


p = partial(func, 5, 6, 7)
print(p(8))  # 60
