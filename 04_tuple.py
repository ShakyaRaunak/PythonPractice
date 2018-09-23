"""
Tuple is a form of collection where different type of data can be stored.
Similar to list where data is separated by commas. Only the difference is that list uses square bracket and tuple uses parenthesis.
Tuples are enclosed in parenthesis and cannot be changed.

Why should we use Tuple? (Advantages of Tuple)
- Processing of Tuples are faster than Lists.
- It makes the data safe as Tuples are immutable and hence cannot be changed.
- Tuples are used for String formatting.
"""

t1 = (10)
print(t1)  # 10
t1 = (10,)
print(t1)  # (10,)

del t1  # will delete the tuple data
# print(t1) -> error

tuple1 = ()
print(tuple1)  # ()

tuple1 = ('rahul', 100, 60.4, 'deepak')
print(tuple1)  # ('rahul', 100, 60.4, 'deepak')
print(tuple1[0])
# print(tuple1[]) -> error

tuple2 = ("sanjay", 10)
print(tuple2)  # ('sanjay', 10)
print(tuple1[2:])  # (60.4, 'deepak')
print(tuple1[0:])  # ('rahul', 100, 60.4, 'deepak')
print(tuple1[:])  # ('rahul', 100, 60.4, 'deepak')
print(tuple1[1])  # 100
# print(t1[]) -> SyntaxError: invalid syntax
print(tuple1 + tuple2)  # ('rahul', 100, 60.4, 'deepak', 'sanjay', 10)

print(tuple1 * 2)  # ('rahul', 100, 60.4, 'deepak', 'rahul', 100, 60.4, 'deepak')
print(len(tuple1))  # 4

t2 = (1, 2, 3)
print(min(t2))  # 1
print(max(t2))  # 3

t3 = tuple(t2)
print(t3)  # (1, 2, 3)

print(tuple1[1:3])  # (100, 60.4)

t4 = "a", 10, 20.9
print(t4)  # ('a', 10, 20.9)
