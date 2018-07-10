# https://docs.python.org/3.0/library/socket.html

"""
These two examples support both IPv4 and IPv6. On most of IPv6-ready systems, IPv6 will take precedence and
the server may not accept IPv4 traffic.
The client side will try to connect to the all addresses returned as a result of the name resolution, and sends traffic
to the first one connected successfully.
"""

# Echo server program
import socket
import sys

HOST = None  # Symbolic name meaning all available interfaces
PORT = 12345  # Arbitrary non-privileged port

s = None

for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res

    try:
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        s = None
        continue

    try:
        s.bind(sa)
        s.listen(1)
    except socket.error as msg:
        s.close()
        s = None
        continue
    break

if s is None:
    print('could not open socket')
    sys.exit(1)

conn, addr = s.accept()
print('Connected by', addr)

while True:
    data = conn.recv(1024)
    if not data: break
    conn.send(data)

conn.close()
