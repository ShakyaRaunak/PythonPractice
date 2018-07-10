# https://www.tutorialspoint.com/python/python_classes_objects.htm

"""
Python deletes unneeded objects (built-in types or class instances) automatically to free the memory space. The process
by which Python periodically reclaims blocks of memory that no longer are in use is termed Garbage Collection.

Python's garbage collector runs during program execution and is triggered when an object's reference count reaches zero.
An object's reference count changes as the number of aliases that point to it changes.
"""

a = 40  # Create object <40>
b = a  # Increase ref. count  of <40>
c = [b]  # Increase ref. count  of <40>

del a  # Decrease ref. count  of <40>
b = 100  # Decrease ref. count  of <40>
c[0] = -1  # Decrease ref. count  of <40>

print("------------------------------------")


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # This __del__() destructor prints the class name of an instance that is about to be destroyed.
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")


pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))  # prints the ids of the objects
del pt1
del pt2
del pt3
