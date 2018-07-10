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

for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())

    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)

        lport = list(nm[host][proto].keys())
        lport.sort()
        for port in lport:
            print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
