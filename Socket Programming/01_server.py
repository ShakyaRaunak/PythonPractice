# https://www.tutorialspoint.com/python/python_networking.htm

# This is 01_server.py file.

import socket  # Import socket module

# socket.socket() is used to create a socket, which has the general syntax −
# s = socket.socket (socket_family, socket_type, protocol=0)
s = socket.socket()  # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 12345  # Reserve a port for your service

# s.bind() binds address (hostname, port number pair) to socket.
s.bind((host, port))  # Bind to the port

# s.listen() sets up and start TCP listener.
s.listen(5)  # Now wait for client connection

# s.accept() -  passively accept TCP client connection, waiting until connection arrives (blocking).
while True:
    conn, addr = s.accept()
    print('Got connection from', addr)
    conn.send('Thank you for connecting')
    conn.close()  # Close the connection

"""
Following would start a server in background:
$ python 01_server.py
"""
