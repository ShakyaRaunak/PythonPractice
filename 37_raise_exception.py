# raise statement -> to explicitly throw an exception and thus execution control will stop in case it is not handled.
try:
    a = 10
    print(a)
    raise NameError("Hello")
except NameError as e:
    print("An exception occurred")
    print(e)
