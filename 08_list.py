# List contain items of different data types.
# Lists are mutable i.e., modifiable.
# The values stored in List are separated by commas(,) and enclosed within a square brackets([]).
# Value stored in a List can be retrieved using the slice operator([] and [:]).
# The plus sign (+) is the list concatenation and asterisk(*) is the repetition operator.

list1 = ["raunak", 4, 7.8, "hello123"]
print(list1)  # ['raunak', 4, 7.8, 'hello123']
# print(list1[]) -> SyntaxError: invalid syntax
print("A list: %s" % list1)  # A list: ['raunak', 4, 7.8, 'hello123']
print(list1[:])  # ['raunak', 4, 7.8, 'hello123']
print(list1[0])  # raunak
print(list1[0:2])  # ['raunak', 4]
print(list1[-3:-1])  # [4, 7.8]
print(list1[0:])  # ['raunak', 4, 7.8, 'hello123']
print(list1[:2])  # ['raunak', 4]

list1[1] = 5
print(list1)  # ['raunak', 5, 7.8, 'hello123']

list1.append("Welcome")
print(list1)  # ['raunak', 5, 7.8, 'hello123', 'Welcome']
list1.append(123)
print(list1)  # ['raunak', 5, 7.8, 'hello123', 'Welcome', 123]

del list1[0]
print(list1)  # [5, 7.8, 'hello123', 'Welcome', 123]
del list1[0:3]
print(list1)  # ['Welcome', 123]

list2 = [456, "rahul"]
print(list2)  # [456, 'rahul']

print(list1[1:2])  # [123]
print(list1[1:3])  # [123]
print(list1 + list2)  # ['Welcome', 123, 456, 'rahul'] duplicates are allowed
print(list1 * 2)  # ['Welcome', 123, 'Welcome', 123]

list3 = [1, 2, 3]
print("Minimum value in List3: ", min(list3))  # 1
print("Maximum value in List3 : ", max(list3))  # 3
print("No. of elements in List3: ", len(list3))  # 3


# cmp method not defined in Python3

def cmp(a, b):
    return (a > b) - (a < b)


print(cmp(1, 2))  # -1
print(cmp(2, 1))  # 1
print(cmp(1, 1))  # 0

# List list(sequence) method Example
# It is used to form a list from the given sequence of elements.
seq = (145, "abcd", 'a', 145, 456)
data = list(seq)
print("List formed is : ", data)  # List formed is :  [145, 'abcd', 'a', 145, 456]
print("Index of a is", data.index('a'))  # Index of a is 2
print("Number of times 145 occurred is", data.count(145))  # Number of times 145 occurred is 2
print("Last element is", data.pop())  # Last element is 456
print("2nd position element:", data.pop(1))  # 2nd position element: abcd
print(data)  # [145, 'a', 145]

data = ['abc', 123, 10.5, 'a']
data.insert(2, 'hello')
print(data)  # ['abc', 123, 'hello', 10.5, 'a']

data1 = ['abc', 123, 10.5, 'a']
data2 = ['ram', 541]
data1.extend(data2)
print(data1)  # ['abc', 123, 10.5, 'a', 'ram', 541]
print(data2)  # ['ram', 541]
data2.remove('ram')
print(data2)  # [541]

data3 = [10, 20, 30, 40, 50]
data3.reverse()
print(data3)  # [50, 40, 30, 20, 10]

data3.sort()
print(data3)  # [10, 20, 30, 40, 50]

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n, )
