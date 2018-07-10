def sum(a, b=50):
    "Adding the two values"
    print("Printing within Function", a + b)
    return a + b


def msg():
    print("Hello")
    return
    # In case no expression is given after return, it will return None i.e.,
    # return statement is used to exit the function definition.


total = sum(10, 20)
print("Printing Outside: ", total)
total = sum(10)
print("Printing Outside: ", total)

msg()
print("Rest of code")  # Rest of code


# Keyword Arguments
def msg(id, name):
    "Printing passed value"
    print(id, name)
    return


msg(id=100, name='Raunak')  # 100 Raunak
msg(name='Raunak', id=101)  # 101 Raunak
