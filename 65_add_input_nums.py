# This program adds up integers in the command line

# $ python 65_add_input_nums.py 1 2 3

import sys

try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print('sum =', total)
except ValueError:
    print('Please supply integer arguments')
