# https://www.pythoncentral.io/hashing-strings-with-python/

"""
A hash function is a function that takes input of a variable length sequence of bytes and converts it to a fixed length
sequence. It is a one way function. This means if f is the hashing function, calculating f(x) is pretty fast and simple,
but trying to obtain x again will take years.

The value returned by a hash function is often called a hash, message digest, hash value, or checksum. Most of the time
a hash function will produce unique output for a given input. However depending on the algorithm, there is a possibility
to find a collision due to the mathematical theory behind these functions.
"""

# The hashlib module defines an API for accessing different cryptographic hashing algorithms.
import hashlib

# By using algorithms_guaranteed function you can see the algorithms present in the module.
print('Guaranteed:\n{}\n'.format(', '.join(sorted(hashlib.algorithms_guaranteed))))

# We can use algorithms_available function to get the list of all the algorithms available in the system,
# including those available through OpenSSl.
print('Available:\n{}'.format(', '.join(sorted(hashlib.algorithms_available))))
