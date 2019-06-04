# https://www.tutorialsteacher.com/python/property-function


class Person:
    def __init__(self, name=''):
        self.__name = name

    def set_name(self, name):
        print('set_name() called')
        self.__name = name

    def get_name(self):
        print('get_name() called')
        return self.__name

    def del_name(self):
        print('del_name() called')
        del self.__name

    name = property(get_name, set_name, del_name)


p1 = Person()
p1.name = "Raunak"
print(p1.name)
# p1.del_name()
del p1.name
