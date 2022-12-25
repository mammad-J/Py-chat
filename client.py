import socket
import threading

HOST = "127.0.0.1"
PORT = 6969
encoding = "utf-8"


def get_message(client_socket):
    while True:
        msg = str(input(""))
        if msg == "quit":
            client_socket.close()
        else:
            client_socket.send(bytes(msg, encoding))


def client():
    socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_instance.connect((HOST, PORT))
    print("Connected to server!")
    threading.Thread(target=get_message, args=[socket_instance]).start()
    while True:
        msg = socket_instance.recv(1024)
        print(msg.decode(encoding))


if __name__ == "__main__":
    client()
