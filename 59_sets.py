# Example 1
print(set("my name is Eric and Eric is my name".split()))  # {'Eric', 'my', 'and', 'is', 'name'}

# Example 2
a = set(["Jake", "John", "Eric"])  # use : a = {"Jake", "John", "Eric"}
print(a)  # {'Eric', 'John', 'Jake'}
b = set(["John", "Jill"])  # use : b = {"John", "Jill"}
print(b)  # {'Jill', 'John'}

# use the "intersection" method to find out which members attended both events :
print(a.intersection(b))  # {'John'}
print(b.intersection(a))  # {'John'}

# use the "symmetric_difference" method to find out which members attended only one of the events :
print(a.symmetric_difference(b))  # {'Jake', 'Jill', 'Eric'}
print(b.symmetric_difference(a))  # {'Jake', 'Jill', 'Eric'}

# use the "difference" method to find out which members attended only one event and not the other :
print(a.difference(b))  # {'Eric', 'Jake'}
print(b.difference(a))  # {'Jill'}

# use the "union" method to receive a list of all participants :
print(a.union(b))  # {'Eric', 'John', 'Jill', 'Jake'}

# use the given lists to print out a set containing all the participants from event A which did not attend event B :
a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]

A = set(a)
B = set(b)

print(A.difference(B))  # {'Jake', 'Eric'}
