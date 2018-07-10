# https://www.tutorialspoint.com/python/python_networking.htm

# This is 01_client.py file

import socket  # Import socket module

s = socket.socket()  # create a socket object
host = socket.gethostname()  # return the hostname
port = 12345  # reserve a port for your service

s.connect((host, port))  # actively initiate TCP server connection
print(s.recv(1024))  # receives TCP message

"""
Once server is started, run client as follows:
$ python 01_client.py
Also, keep the above terminal open and now open another terminal then type:
$ telnet localhost 12345
"""
