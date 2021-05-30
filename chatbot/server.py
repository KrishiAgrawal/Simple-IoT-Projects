import socket
from continuous_threading import Thread

server_socket=socket.socket()
port_number = 2000
server_socket.bind(("",port_number))
print("Server is bounded to port ", port_number)
server_socket.listen()
print("Server is listening")
conn,addr= server_socket.accept()
print("Server is connected to address ", addr)

def receive_data():
    while True:
        data = conn.recv(1000)
        print("Client:", data.decode())

def send_data():
    while True:
        user_input = input()
        conn.sendall(user_input.encode())

t = Thread(target=receive_data)
t.start()
send_data()

conn.close()
server_socket.close()