# https://resources.infosecinstitute.com/writing-hacking-tools-with-python-part-1

# $ C:\ProgramData\Anaconda3\python.exe 01.py testintrude.txt
import requests
import sys

file_name = sys.argv[1]
filewriter = open('test_report.csv', 'w')
fileopener = open(file_name, 'r')
counter = 0

for x in fileopener.readlines():
    counter = counter + 1
    url = x.strip('\n')
    req = None

    try:
        req = requests.get(url)
        success = 'true'
    except Exception as e:
        print(e)
        success = 'false'

    if success == 'false':
        print('[-] ' + url.strip('\n') + ',' + ',' + '\n')
        filewriter.write('[-],' + str(counter) + ',' + url.strip('\n') + 'No Result' + ',' + '\n')
    else:
        if req.status_code == 200:
            print('[+] ' + url.strip('\n') + ',' + str(req.status_code) + ',' + '\n')
            filewriter.write('[+],' + str(counter) + ',' + url.strip('\n') + ',' + str(req.status_code) + ',' + '\n')
        else:
            print('[-] ' + url.strip('\n') + ',' + str(req.status_code) + ',' + '\n')
            filewriter.write('[-],' + str(counter) + ',' + url.strip('\n') + ',' + str(req.status_code) + ',' + '\n')

filewriter.close()
fileopener.close()
