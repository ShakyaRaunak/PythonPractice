import csv

f = open('country-list.csv', "r")
reader = csv.reader(f)
for row in reader:
    print(row)

f.close()
