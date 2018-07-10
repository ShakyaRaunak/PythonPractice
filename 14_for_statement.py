# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 1,3,5,7 (odd numbers)
for x in range(1, 8, 2):
    print(x)

num = 2
for a in range(1, 6):
    print(num * a)

print()
for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

print()
countries = ["USA", "England", "Australia", "South Africa"]
for index in range(len(countries)):
    print(countries[index], end="   ")

print("\n")
for country in countries:
    print(country)

print()
presidents = ["Donald Trump", "Ronald Reagan", "JFK", "Richard Nixon", "George W Bush"]
for i in range(len(presidents)):
    print("President {}: {}".format(i + 1, presidents[i]))

presidents = ["Donald Trump", "Ronald Reagan", "JFK", "Richard Nixon", "George W Bush"]
for num, name in enumerate(presidents, start=1):
    print("President {}: {}".format(num, name))
