# https://pythonspot.com/python-network-sockets-programming-tutorial/

"""
The server code before can only interact with one client.  If you try to connect with a second terminal,
it simply won’t reply to the new client. To let the server interact with multiple clients you need to use multi-threading.
We rebuild the server script to accept multiple client connections:
"""

import socket
from threading import Thread


class ClientThread(Thread):

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("[+] New thread started for " + ip + ":" + str(port))

    def run(self):
        while True:
            data = conn.recv(2048)
            if not data: break
            print("received data:", data)
            conn.send(data)  # echo


TCP_IP = '0.0.0.0'
TCP_PORT = 62
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(4)
    print("Waiting for incoming connections...")
    (conn, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
