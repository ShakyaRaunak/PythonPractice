import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of New List:', id(new_list))

print()

###############################################


old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)
print("Old list:", old_list)
print("New list:", new_list)

old_list.append([4, 4, 4])
print("Old list:", old_list)
print("New list:", new_list)

print()

###############################################


old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'

print("Old list:", old_list)  # Old list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
print("New list:", new_list)  # New list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]

old_list.append([4, 4, 4])
print("Old list:", old_list)  # Old list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3], [4, 4, 4]]
print("New list:", new_list)  # New list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]

old_list[1][1] = 'BB'
print("Old list:", old_list)  # Old list: [[1, 1, 1], [2, 'BB', 2], [3, 3, 3], [4, 4, 4]]
print("New list:", new_list)  # New list: [[1, 1, 1], [2, 'BB', 2], [3, 3, 3]]
