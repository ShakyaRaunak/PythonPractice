"""
The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment
counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other
is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_105519.xml (Sum ends with 28)
"""

import urllib.request
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_105519.xml'

# print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
# print('Retrieved', len(data), 'characters')
# print(data)
# print(data.decode())

tree = ET.fromstring(data)
total_count = 0

comments = tree.findall('comments/comment')
# print('Comments count:', len(comments))

for comment in comments:
    count = comment.find('count').text
    total_count += int(count)

print(total_count)
