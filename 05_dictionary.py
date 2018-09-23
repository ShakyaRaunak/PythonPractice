"""
Dictionary is a collection which works on a key-value pair.
It works like an associated array where no two keys can be same.
Dictionaries are enclosed by curly braces ({}) and values can be retrieved by square bracket([]).
"""

dictionary = {'name': 'charlie', 'id': 100, 'dept': 'IT'}
print(dictionary)  # {'dept': 'IT', 'name': 'charlie', 'id': 100}
print(dictionary.keys())  # dict_keys(['name', 'id', 'dept'])
print(dictionary.values())  # dict_values(['charlie', 100, 'IT'])
print(dictionary.items())  # dict_items([('name', 'charlie'), ('id', 100), ('dept', 'IT')])

print(dictionary['name'])  # charlie

print(len(dictionary))  # 3

# Dictionary str(dictionary) -> returns string formation of the value.
print(str(dictionary))  # {'name': 'charlie', 'id': 100, 'dept': 'IT'}

dictionary['name'] = "raunak"
print(dictionary)  # {'name': 'raunak', 'id': 100, 'dept': 'IT'}

del dictionary['dept']
print(dictionary)  # {'name': 'raunak', 'id': 100}
del dictionary
# print(dictionary) -> error


# Dictionary update(dictionary2) -> to add items of dictionary2 to first dictionary.
data1 = {100: 'Ram', 101: 'Suraj', 102: 'Alok'}
data2 = {103: 'Sanjay'}
data1.update(data2)
print(data1)  # {100: 'Ram', 101: 'Suraj', 102: 'Alok', 103: 'Sanjay'}
print(data2)  # {103: 'Sanjay'}

# Dictionary clear() -> It returns an ordered copy of the data.
data1.clear()
print(data1)  # {}

# Dictionary fromkeys(sequence)/fromkeys(seq,value)
# It is used to create a new dictionary from the sequence where sequence elements forms the key and
# all keys share the values ?value1?. In case value1 is not given, it set the values of keys to be none.
sequence = ('Id', 'Number', 'Email')
data1 = {}
data2 = {}
data1 = data1.fromkeys(sequence)
print(data1)  # {'Id': None, 'Number': None, 'Email': None}
data2 = data2.fromkeys(sequence, 100)
print(data2)  # {'Id': 100, 'Number': 100, 'Email': 100}

# Dictionary copy() -> It returns an ordered copy of the data.
data3 = data2.copy()
print(data3)  # {'Id': 100, 'Number': 100, 'Email': 100}

# Dictionary has_key(key) is deprecated.

# Dictionary get(key) -> It returns the value of the given key. If key is not present it returns none.
data = {'Id': 100, 'Name': 'Aakash', 'Age': 23}
print(data.get('Age'))  # 23
print(data.get('Email'))  # None

# merge two dictionaries (with duplicate keys)
dict1 = {'name': 'Inception', 'name': 'The Departed', 'collection': '$500 million'}
dict2 = {'actor': 'Leonardo DiCaprio', 'actress': 'Marion Cotillard', 'actress': 'Ellen Page'}
z = {**dict1, **dict2}
# {'name': 'The Departed', 'collection': '$500 million', 'actor': 'Leonardo Di Caprio', 'actress': 'Ellen Page'}
print(z)

phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}
phonebook.pop("Jack")
print(phonebook)  # {'Jill': 947662781, 'John': 938477566}
