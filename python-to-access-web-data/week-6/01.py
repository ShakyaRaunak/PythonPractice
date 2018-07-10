import urllib.request
import json

url = 'http://py4e-data.dr-chuck.net/comments_105520.json'

uh = urllib.request.urlopen(url)
data = uh.read()

info = json.loads(data)
# print(info['note'])
# print(info['comments'])

comments = info['comments']
count = 0

for comment in comments:
    count += comment['count']

print(count)
