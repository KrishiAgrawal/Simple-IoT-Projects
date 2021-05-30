import socket
from continuous_threading import Thread

server_socket=socket.socket()
server_socket.bind(("",2000))
server_socket.listen()
clients={}

def client_task(client_name,client_conn,client_addr):
    while True:
        data = client_conn.recv(1000)
        message = client_name + ": " + data.decode()
        for client in clients:
            if client!=client_name:
                clients[client].sendall(message.encode())

while True:
    conn,addr= server_socket.accept()
    print("Got a connection from of address", addr)
    name = conn.recv(1000)
    clients[name.decode()]=conn
    t = Thread(target=client_task, args=(name.decode(),conn,addr))
    t.start()