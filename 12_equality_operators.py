""" An is expression evaluates to True if two variables point to the same (identical) object.
	An == expression evaluates to True if the objects referred to by the variables are equal (have the same contents). """

a = [1, 2, 3]
b = a
print(a == b)  # True
print(a is b)  # True

c = list(a)  # we create an identical copy of our list object
print(a == c)  # True
print(a is c)  # False because c and a are pointing to two different objects, even though their contents are the same.
