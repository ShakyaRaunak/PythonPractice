import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print("Old list:", old_list)  # Old list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
print("New list:", new_list)  # New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

print()

###############################################


old_list[1][0] = 'BB'

print("Old list:", old_list)  # Old list: [[1, 1, 1], ['BB', 2, 2], [3, 3, 3]]
print("New list:", new_list)  # New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
