# create a new list from tuple, update the list and form a new tuple from that list
t = ('275', '54000', '0.0', '5000.0', '0.0')
lst = list(t)
lst[0] = '300'
t = tuple(lst)
print(t)

# example to update the tuples in a list of tuples
prodName = [(1.0, 1), (1.1, 2), (1.2, 3), (1.3, None), (1.4, 5)]
prodDict = {1: 'name_1', 2: 'name_2', 3: 'name_3'}

# new_prodName = [(f, prodDict[id]) for f, id in prodName]
# This will fail if the id isn't found in the prodDict dict. You can set a default (ex: None) using .get():
new_prodName = [(f, prodDict.get(id, None)) for f, id in prodName]
print(new_prodName)
