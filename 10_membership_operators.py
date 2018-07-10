# Membership Operators

list = [1, 2, 3, 4, 5]
a = 1
b = 2
print(a in list)  # True
print(a not in list)  # False

if (a in list):
    print("a is in given list")
else:
    print("a is not in given list")

if (b not in list):
    print("b is not in given list")
else:
    print("b is in given list")
