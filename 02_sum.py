a = 10
b = 20
c = a + b
print(c)  # print c does not work

a, b = 3, 4
print(a, b)  # 3 4

# float to int to float conversion
myFloat = 7.0
print(myFloat)  # 7.0
myInt = int(myFloat)
print(myInt)  # 7
myFloat = float(myInt)
print(myFloat)  # 7.0

if isinstance(myFloat, float):
    print("Float: %f" % myFloat)
if isinstance(myInt, int):
    print("Integer: %d" % myInt)
