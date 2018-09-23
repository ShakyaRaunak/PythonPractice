x = y = z = 50
print(x)  # 50
print(y)  # 50
print(z)  # 50
# print xyz -> gives error
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(xyz)?
print(x, y, z)  # 1 2 3
# in python shell: x, y, z -> (50, 50, 50)

x, y, z = 1, 2, 3
print(x)  # 1
print(y)  # 2
print(z)  # 3

x, y = y, x
print(x)  # 2
print(y)  # 1
