""""
create socket, bind to port number, listen for client, accept the connection,communicate, close connection, close socket
"""


import socket

server_socket=socket.socket()
port_number = 2000
server_socket.bind(("",port_number))
print("Server is bound to port:",port_number)
server_socket.listen()
print("Server is listening")

conn,addr= server_socket.accept()
print("Got a client from address", addr)
data= conn.recv(1000)
print(data.decode())
conn.sendall("Hey from server".encode())
conn.close()
server_socket.close()