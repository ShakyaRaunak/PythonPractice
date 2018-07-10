# https://www.pythoncentral.io/hashing-strings-with-python/

"""
Using OpenSSL Algorithms
Now suppose you need an algorithm provided by OpenSSL. Using algorithms_available, we can find the name of the algorithm
you want to use. In this case, "DSA" is available on my computer. You can then use the new and update methods.
"""

import hashlib

hash_object = hashlib.new('DSA')
hash_object.update(b'Hello World')

print(hash_object.hexdigest())
