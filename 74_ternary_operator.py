# https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator

# The syntax is: a if condition else b
target = 299

score = 300
result = 'winner' if score > target else 'loser'
print(result)

score = 299
result = 'winner' if score > target else ('loser' if score < target else 'draw')  # nested ternary conditional operator
print(result)

print('true' if True else 'false')  # 'true'
print('true' if False else 'false')  # 'false'

# Note that conditionals are an expression, not a statement. This means you can't use assignments or  pass or other
# statements in a conditional:
# pass if False else x = 3
