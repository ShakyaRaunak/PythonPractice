# iteration through a list of dictionaries

dataList = [{'a': 1, 'm': 2}, {'b': 3, 'n': 4}, {'c': 5, 'o': 6}]

# iterate over the indices of the range of the len of your list
for index in range(len(dataList)):
    for key in dataList[index]:
        print('{}: {}'.format(key, dataList[index][key]), end=' ')
print()

# use a while loop with an index counter
index = 0
while index < len(dataList):
    for key in dataList[index]:
        print(dataList[index][key], end=' ')
    index += 1
print()

# iterate over the elements in the list directly
for dic in dataList:
    for key in dic:
        print(dic[key], end=' ')
print()

# even without any lookups by just iterating over the values of the dictionaries
for dic in dataList:
    for val in dic.values():
        print(val, end=' ')
print()

# wrap the iterations inside a list-comprehension or a generator and unpack them later
print(*[val for dic in dataList for val in dic.values()], sep=' ')

# retrieve keys and values of dictionaries in a list
ipl_players = [
    {'Rank': 1, 'Name': 'Kane Williamson'},
    {'Rank': 2, 'Name': 'Rashid Khan'},
    {'Rank': 3, 'Name': 'Jos Butler'},
    {'Rank': 4, 'Name': 'AB De Villiers'},
    {'Rank': 5, 'Name': 'Trent Boult'}
]
for player in ipl_players:
    for k, v in player.items():
        print('{}: {} '.format(k, v), end=' ')
        # print("%s: %s " % (k, v)) does the same
    print()

# access a value in a tuple that is in a list
# return the second value from each tuple of the list
list_of_tuples = [(1, 2), (2, 3), (4, 5), (3, 4), (6, 7), (6, 7), (3, 8)]
print([x[1] for x in list_of_tuples])
