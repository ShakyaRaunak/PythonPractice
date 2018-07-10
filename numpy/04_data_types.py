# using array-scalar type
import numpy as np

dt = np.dtype(np.int32)
print(dt)  # int32

# int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2','i4', etc.
dt = np.dtype('i4')
print(dt)  # int32

# using endian notation
dt = np.dtype('>i4')
print(dt)  # >i4

# first create structured data type
dt = np.dtype([('age', np.int8)])
print(dt)  # [('age', 'i1')]

# now apply it to ndarray object
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a)  # [(10,) (20,) (30,)]

# file name can be used to access content of age column
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a['age'])  # [10 20 30]

# a structured data type called student with a string field 'name', an integer field 'age' and a float field 'marks'.
# This dtype is applied to ndarray object.
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)  # [('name', 'S20'), ('age', 'i1'), ('marks', '<f4')]

a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
print(a)  # [(b'abc', 21, 50.) (b'xyz', 18, 75.)]
