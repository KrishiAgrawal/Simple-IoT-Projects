import socket
from continuous_threading import Thread

client_socket = socket.socket()
client_socket.connect(("localhost", 2000))
name = input("Enter your name: ")
client_socket.sendall(name.encode())


def receive_data():
    while True:
        data = client_socket.recv(1000)
        print(data.decode())

def sending_data():
    while True:
        user_input = input()
        client_socket.sendall(user_input.encode())


t = Thread(target=receive_data)
t.start()
sending_data()

