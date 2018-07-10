# https://codeclubprojects.org/en-GB/python/password-generator/
from random import choice

CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*(){}[_+-=<>?,./]'

password_length = input('Enter password length? ')
password_length = int(password_length)

for p in range(3):
    password = ''
    for c in range(password_length):
        password += choice(CHARS)

    print(password)
