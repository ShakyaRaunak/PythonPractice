# check python version
import sys

is_py2 = sys.version[0] == '2'
print(sys.version[0])

if is_py2:
    print("you have py2")
else:
    print("you don't have py2")
