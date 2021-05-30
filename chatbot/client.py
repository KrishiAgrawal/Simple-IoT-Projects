import socket
from continuous_threading import Thread

client_socket = socket.socket()
client_socket.connect(("localhost", 2000))
print("Connected to server")


def receive_data():
    while True:
        data = client_socket.recv(1000)
        print("Server:", data.decode())

def sending_data():
    while True:
        user_input = input()
        client_socket.sendall(user_input.encode())


t = Thread(target=receive_data)
t.start()
sending_data()

client_socket.close()
