# Arithmetic Operators
print(10 / 3)  # 3.3333333333333335
print(10 // 3)  # 3

print(10 % 3)  # 1

print(2 * 3)  # 6
print(2 ** 3)  # 8

# Logical Operators
a = 1 > 2 and 2 > 3
print(a)  # False
a = 1 > 2 or 2 > 3
print(a)  # False
a = 1 < 2 and 2 > 3
print(a)  # False
a = 1 < 2 or 2 > 3
print(a)  # True
a = 2 > 3
print(a)  # False
a = not (2 > 3)
print(a)  # True

# <> -> It means NOT EQUAL, but it is deprecated, use != instead.

# Operator precedence
number = 1 + 2 * 3 / 4.0
print(number)  # 3 / 4.0 -> 0.75 -> 0.75 * 2 -> 1.5 -> 1.5 + 1 -> 2.5

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # True
# Unlike the double equals operator "==", the "is" operator does not match the values of the variables,
# but the instances themselves.
print(x is y)  # False

x = 1  # x = 'hello'
y = 1  # x = 'hello'
print(x == y)  # True
print(x is y)  # True
