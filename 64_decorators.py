# https://www.learnpython.org/en/Decorators
# https://realpython.com/primer-on-python-decorators/
"""
decorators wrap a function, modifying its behavior.
"""


# Example 1 :
def my_decorator(some_function):
    def wrapper():
        num = 10
        if num == 10:
            print("Yes!")
        else:
            print("No!")

        some_function()
        print("Something is happening after some_function() is called.")

    return wrapper


def just_some_function():
    print("Wheee!")


just_some_function = my_decorator(just_some_function)
just_some_function()
print()

"""
Syntactic Sugar!
Python allows you to simplify the calling of decorators using the @ symbol (this is called “pie” syntax).
"""

# Example 2 : using @{decorator_name}
from decorator_module import my_decorator


# @my_decorator is just an easier way of saying just_some_function = my_decorator(just_some_function).
# It’s how you apply a decorator to a function.
@my_decorator
def just_some_function2():
    print("Wheee!")


just_some_function2()
print()


# Example 3 :
def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwds):
            return multiplier * old_function(*args, **kwds)

        return new_function

    return multiply_generator  # it returns the new generator


# Usage
@multiply(3)  # multiply is not a generator, but multiply(3) is
def return_num(num):
    return num


# Now return_num is decorated and reassigned into itself
print(return_num(5))  # should return 15
print()


# Example 4 :
# It creates a decorator factory which returns a decorator that decorates functions with one argument.
# The factory takes one argument, a type, and then returns a decorator that makes function should check if
# the input is the correct type. If it is wrong, it should print"Bad Type".
def type_check(correct_type):
    def check(old_function):
        def new_function(arg):
            if (isinstance(arg, correct_type)):
                return old_function(arg)
            else:
                print("Bad Type")

        return new_function

    return check


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
times2('Not A Number')


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])
