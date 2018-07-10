# https://www.javatpoint.com/multiple-inheritance-in-python

"""
Multiple Inheritance allows us to inherit multiple parent classes. We can derive a child class from more than one base
(parent) classes. The multi-derived class inherits the properties of all the base classes.
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
        """
        The super() method is most commonly used with __init__ function in base class. This is usually the only place
        where we need to do some things in a child then complete the initialization in the parent.
        """
        super(Third, self).__init__()
        print("third")


Third()
