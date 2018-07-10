try:
    a = 10 / 0  # malicious code
    print(a)
except ArithmeticError:
    # code to be executed in case exception occurs.
    print("This statement is raising an ArithmeticError")
except NameError:
    print("This statement is raising a NameError")
except IndentationError:
    print("This statement is raising an IndentationError")
except IOError:
    print("This statement is raising an IOError")
except EOFError:
    print("This statement is raising an EOFError")
else:
    # In case of no exception, execute the else block code.
    print("Welcome")


# another example
def do_stuff_with_number(n):
    print(n)


the_list = (1, 2, 3, 4, 5)

for i in range(20):
    try:
        do_stuff_with_number(the_list[i])
    except IndexError:  # Raised when accessing a non-existing index of a list
        do_stuff_with_number(0)
