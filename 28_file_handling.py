obj = open("file_handling_demo.txt", "w")
obj.write("Welcome to the world of Python")
print(obj.closed)  # False
obj.close()
print(obj.name)  # file_handling_demo.txt
print(obj.mode)  # w
print(obj.closed)  # True

obj1 = open("file_handling_demo.txt", "r")
s = obj1.read()
print(s)
obj1.close()

obj2 = open("file_handling_demo.txt", "r")
s1 = obj2.read(20)
print(s1)
obj2.close()
