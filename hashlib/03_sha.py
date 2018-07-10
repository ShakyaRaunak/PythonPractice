# https://www.pythoncentral.io/hashing-strings-with-python/

"""
SHA: Group of algorithms designed by the U.S's NSA that are part of the U.S Federal Information processing standard.
These algorithms are used widely in several cryptographic applications.
The message length ranges from 160 bits to 512 bits.
"""

import hashlib

hash_object = hashlib.sha1(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)

hash_object = hashlib.sha224(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)

hash_object = hashlib.sha256(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)

hash_object = hashlib.sha384(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)

hash_object = hashlib.sha512(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)
