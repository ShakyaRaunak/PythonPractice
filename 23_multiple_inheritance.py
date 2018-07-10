"""
    The super() method is most commonly used with __init__ function in base class.
    This is usually the only place where we need to do some things in a child then complete the initialization in the parent.
"""


class First(object):
    def __init__(self):
        super(First, self).__init__()
        print("first")


class Second(object):
    def __init__(self):
        super(Second, self).__init__()
        print("second")


class Third(Second, First):
    def __init__(self):
        super(Third, self).__init__()
        print("third")


Third();
