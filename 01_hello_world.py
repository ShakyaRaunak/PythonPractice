print("Hello World!")

name = "Raunak"
score = 100

# Pass the values as parameters and print will do it:
print("Total score for", name, "is", score)

# Pass it as a dictionary:
print("Total score for %s is %s" % (name, score))

print("Total score for %(n)s is %(s)s" % {'n': name, 's': score})

# Use the new-style string formatting:
print("Total score for {} is {}".format(name, score))

# Use the new-style string formatting with explicit names:
print("Total score for {n} is {s}".format(n=name, s=score))

# If you don't want spaces to be inserted automatically by print in the above example, change the sep parameter:
print("Total score for ", name, " is ", score, sep='    ')

# Play with the order of the parameters:
print("You got {1}. Hello, {0}.".format(name, score))  # You got 100. Hello, Raunak.

# Use the new and much cleaner f-string formatting in Python 3.6: MODERN APPROACH and you can call functions with it.
print(f'Total score for {name} is {score}')

# You can also use ** to do this neat trick with dictionaries:
person = {'name': 'Eric', 'age': 74}
print("Hello, {name}. You are {age}.".format(**person))  # Hello, Eric. You are 74.

# https://realpython.com/python-f-strings/
"""
f-strings are faster than both %-formatting and str.format() as f-strings are expressions evaluated at runtime rather 
than constant values. At runtime, the expression inside the curly braces is evaluated in its own scope and then 
put together with the string literal part of the f-string. The resulting string is then returned.
"""

# f-strings are evaluated at runtime, you can put any and all valid Python expressions:
print(f"{2 * 37}")  # 74

# You also have the option of calling a method directly:
print(f"{name.upper()} is funny.")  # RAUNAK is funny.
