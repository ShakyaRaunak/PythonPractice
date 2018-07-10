# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a
# regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

import re

fh = open("regex_sum_105515.txt", "r")
total = 0

for line in fh:
    y = re.findall("[0-9]+", line)
    if len(y) > 0:
        total += sum(int(i) for i in y)

print(total)  # 453167
