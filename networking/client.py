"""
create a socket of ip and port number, connect to server, communicate, close
"""

import socket

client_socket=socket.socket()
client_socket.connect(("localhost",2000))
client_socket.sendall("Hi server, I'm client".encode())
data =  client_socket.recv(1000)
print(data.decode())
client_socket.close()