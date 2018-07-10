""" In Python, pass keyword is used to execute nothing; it means, when we don't want to execute code,
    the pass can be used to execute empty. It just makes the control to pass by without executing any code.
    If we want to bypass any code pass, statement can be used.
"""

for i in [1, 2, 3, 4, 5]:
    if i == 3:
        pass
        print("Pass when value is", i)
    print(i)
