# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


a = my_gen()
next(a)
next(a)
next(a)
# next(a)  # produces StopIteration error

print()

# Using for loop
for item in my_gen():
    print(item)
