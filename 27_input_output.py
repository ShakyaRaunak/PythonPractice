# input() function is used to take input from the user.
# Whatever expression is given by the user, it is evaluated and result is returned back.
# raw_input() function is deprecated.
n = input("Enter your expression: ")
print("The evaluated expression is ", n)

# calculate simple interest
prn = int(input("Enter Principal: "))
r = int(input("Enter Rate: "))
t = int(input("Enter Time: "))
si = (prn * r * t) / 100
print("Simple Interest is ", si)
