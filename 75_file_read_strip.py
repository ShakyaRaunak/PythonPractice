# https://www.py4e.com/tools/pythonauto/?PHPSESSID=84a1e31859aa77beda0681cf5aecd6e1

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")  # Enter : mbox-short.txt
fh = open(fname)

count = 0
total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    val = line.lstrip("X-DSPAM-Confidence:").rstrip()
    total = total + float(val)
    count = count + 1

average = total / count

print("Average spam confidence:", average)
