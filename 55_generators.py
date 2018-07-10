# https://www.learnpython.org/en/Generators
import random


# This function decides how to generate the random numbers on its own, and executes the yield statements one at a time,
# pausing in between to yield execution back to the main for loop.
def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)


# a simple example of a generator function which returns 7 random integers:
for random_number in lottery():
    print("And the next number is... %d!" % (random_number))

print()


# a generator function which returns the Fibonacci series.
def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b


import types

if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
