""" Anonymous Function
In python, the keyword lambda is used to create what is known as anonymous functions. These are essentially functions
with no pre-defined name. They are good for constructing adaptable functions, and thus good for event handling.

Lambda takes any number of arguments and returns an evaluated expression.
Lambda is created without using the def keyword.
"""

# Example 1 :
# Function Definiton
square = lambda x1: x1 * x1

# Calling square as a function
print("Square of number is", square(10))  # Square of number is 100


# Example 2 :
def myfunc(n):
    return lambda i: i * n


# The power of lambda is better shown when you generate anonymous functions at run-time, as shown in the following example:
doubler = myfunc(2)
tripler = myfunc(3)
val = 11

print("Doubled: " + str(doubler(val)) + ". Tripled: " + str(tripler(val)))
# Here we see the defined function, myfunc, which creates an anonymous function that doubles some on-the-fly variable i
# with a just-in-time variable n representing our multiplier.
