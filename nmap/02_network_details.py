# https://github.com/johanlundberg/python-nmap/blob/master/nmap/example.py

import sys
import os

import nmap

os.environ['PATH'] += ";C:\\Program Files (x86)\\Nmap"

try:
    nm = nmap.PortScanner()  # instantiate nmap.PortScanner object
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(0)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(0)

# scan host 127.0.0.1, ports from 22 to 443
print(nm.scan('127.0.0.1', '22-443'))

# get command line used for the scan : nmap -oX - -p 22-443 127.0.0.1
print(nm.command_line())

# get nmap scan information {'tcp': {'services': '22-443', 'method': 'connect'}}
print(nm.scaninfo())

# get all hosts that were scanned
print(nm.all_hosts())

# get hostname for host 127.0.0.1
print(nm['127.0.0.1'].hostname())

# get state of host 127.0.0.1 (up|down|unknown|skipped)
print(nm['127.0.0.1'].state())

# get all scanned protocols ['tcp', 'udp'] in (ip|tcp|udp|sctp)
print(nm['127.0.0.1'].all_protocols())
