# METHOD 1 :
def f(x):
    return {
        'a': 1,
        'b': 2,
    }[x]


print(f('a'))  # 1
print(f('b'))  # 2


# METHOD 2 :
# If you want defaults, you could use the dictionary get(key[, default]) method:
def g(x):
    return {
        'a': 1,
        'b': 2
    }.get(x, 9)


print(g('a'))  # 1
print(g('c'))  # 9


# METHOD 3 :
# Because Python has first-class functions they can be used to emulate switch/case statements.
def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    else:
        return None


def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()


print(dispatch_if('mul', 2, 8))  # 16
print(dispatch_dict('mul', 2, 8))  # 16
print(dispatch_if('unknown', 2, 8))  # None
print(dispatch_dict('unknown', 2, 8))  # None
