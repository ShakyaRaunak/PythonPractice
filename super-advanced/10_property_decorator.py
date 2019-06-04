class Person:
    def __init__(self):
        self.__name = ''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        print('Deleting..')
        del self.__name


p1 = Person()
p1.name = "Raunak"
print(p1.name)  # Raunak
del p1.name  # Deleting..
# print(p1.name)  # AttributeError: 'Person' object has no attribute '_Person__name'
