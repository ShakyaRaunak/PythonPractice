# https://www.pythoncentral.io/hashing-strings-with-python/

"""
MD5: Message digest algorithm producing a 128 bit hash value. This is widely used to check data integrity.
It is not suitable for use in other fields due to the security vulnerabilities of MD5.
"""

import hashlib

# To calculate the MD5 hash, or digest, for a block of data (here a unicode string converted to a byte string), first
# create the hash object, then add the data and call digest() or hexdigest().

# METHOD 1 :
hash_object = hashlib.md5(b'Hello World')

print(hash_object.hexdigest())

# OR

# METHOD 2 :
hash_object = hashlib.md5()
hash_object.update('Hello World'.encode('utf-8'))

print(hash_object.hexdigest())
