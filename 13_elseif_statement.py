# basic example
a = 20
if (a > 20):
    print("a is greater than 20.")
elif (a < 20):
    print("a is less than 20.")
else:
    print("a is equal to 20.")

# another example
x = range(1, 4)
if isinstance(x, tuple):
    print("x is a tuple")
if isinstance(x, list):
    print("x is a list")
if isinstance(x, range):
    print("x is a range")

# another example
number = 16
second_number = 0
first_array = [1, 2, 3]
second_array = [1, 2]

if number > 15:
    print("1")  # 1

if first_array:
    print("2")  # 2

if len(second_array) == 2:
    print("3")  # 3

if len(first_array) + len(second_array) == 5:
    print("4")  # 4

if first_array and first_array[0] == 1:
    print("5")  # 5

if not second_number:
    print("6")  # 6
