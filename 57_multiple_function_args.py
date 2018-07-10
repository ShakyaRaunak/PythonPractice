# https://www.learnpython.org/en/Multiple_Function_Arguments
def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))  # And all the rest... [4, 5]


# The "therest" variable is a list of variables, which receives all arguments which were given to the "foo" function
# after the first 3 arguments.
foo(1, 2, 3, 4, 5)


# Another example : send functions arguments by keyword, so that the order of the argument does not matter
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" % (first + second + third))

    if options.get("number") == "first":
        return first
    else:
        return 0


result = bar(1, 2, 3, action="sum", number="first")  # The sum is: 6
print("Result: %d" % (result))  # Result: 1


# Another example : foo function must return the amount of extra arguments received. The bar must return True if the argument with
# the keyword magicnumber is worth 7, and False otherwise.
def foo(a, b, c, *args):
    return len(args)


def bar(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7

# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")
