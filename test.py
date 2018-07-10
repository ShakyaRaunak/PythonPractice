fruit = 'Banana'
# fruit[0] = 'b' # error
print(fruit)

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])

friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends[0])  # Glenn

print(friends)
friends.sort(reverse=True)
print(friends)

t = (1, 2, 3)
i = t.index(1)
print(i)

l = [1, 2, 3]
i = l.index(3)
print(i)

x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()
print(y)

x = (5, 1, 3)
a = (4, 100, 200)
b = (6, 0, 0)
c = (0, 1000, 2000)
d = (5, 0, 300)
if a > x : print("a")
if b > x : print("b")
if c > x : print("c")
if d > x : print("d")

# Exercise 1 START
stuff = dict()
# print(stuff['candy']) # error
print(stuff.get('candy', -1))  # -1

stuff.update({'item3': 65})
stuff.update({'item5': 123})
stuff.update({'item4': 32})

print(stuff)
print(stuff.keys())
print(stuff.values())

for x in stuff:
    print(x)
# Exercise 1 END

# Exercise 2 START
fname = input("Enter file:")
if len(fname) < 1: fname = "mbox-short.txt"
fh = open(fname)

hours = []
for line in fh:
    if line.startswith('From '):
        words = line.split(" ")
        hours.append(words[-2].split(":")[0])

dic = {x: hours.count(x) for x in hours}
print(dic)

# for k, v in dic.items(): print(k, v)

for key in sorted(dic.keys()):
    print("%s: %s" % (key, dic[key]))
# Exercise 2 END


# Exercise 3 START
fname = input("Enter file:")
if len(fname) < 1: fname = "mbox-short.txt"
fh = open(fname)

address_list = []

for line in fh:
    if line.startswith('From '):
        words = line.split(" ")
        address_list.append(words[1].strip())

d = {x: address_list.count(x) for x in address_list}
max_key = max(d, key=lambda k: d[k])
print('%s %i' % (max_key, d[max_key]))

maximum = max(d, key=d.get)
print('%s %i' % (maximum, d[maximum]))
print(max(d.values()))

maxcount = max(d.values())
for k, v in d.items():
    if v == maxcount:
        print('%s %i' % (k, v))
# Exercise 3 END
