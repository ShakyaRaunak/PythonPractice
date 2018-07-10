import urllib.request

x = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

print(x)
print(type(x))
