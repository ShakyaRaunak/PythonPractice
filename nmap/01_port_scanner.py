# https://github.com/johanlundberg/python-nmap/blob/master/nmap/example.py

"""
Nmap ("Network Mapper") is a free and open source utility for network discovery and security auditing. Many systems and
network administrators also find it useful for tasks such as network inventory, managing service upgrade schedules, and
monitoring host or service up-time.

Nmap is famous as Swiss Army knife of network discovery and security auditing.

Nmap uses raw IP packets in novel ways to determine what hosts are available on the network, what services
(application name and version) those hosts are offering, what operating systems (and OS versions) they are running,
what type of packet filters/firewalls are in use, and dozens of other characteristics.
It was designed to rapidly scan large networks, but works fine against single hosts.
"""

import sys
import os
# from pprint import pprint

from nmap import PortScannerError, PortScanner

# os.environ['PATH'] += ";C:\\Program Files (x86)\\Nmap"
# pprint({'PATH': os.environ['PATH'].split(os.pathsep)})

try:
    ns = PortScanner()  # instantiate nmap.PortScanner object
    print(ns.nmap_version())  # (7, 70)

    scanner_output = ns.scan()
    print(scanner_output)
except PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(0)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(0)
