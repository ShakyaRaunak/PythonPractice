""" The name of the constructor is always the same __init__().
    Constructor can be parameterized and non-parameterized as well.
    When we create a class without a constructor, Python automatically creates a default constructor that doesn't do anything.
    Every class must have a constructor, even if it simply relies on the default constructor.
"""


class ComplexNumeber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real, self.imag))


c1 = ComplexNumeber(5, 6)
c1.getData()

c2 = ComplexNumeber(11)
c2.getData()
c2.attr = 12
print(c2.real, c2.imag, c2.attr)
