import socket
import threading
import time


HOST = "127.0.0.1"
PORT = 6969
encoding = "utf-8"
connections = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(3)


def broadcast(message, expection):
    for clients in connections:
        if clients == expection:
            pass
        else:
            time.sleep(0.09)
            clients.sendall(bytes(message, encoding))

def recieve_message(client):
    while True:
        time.sleep(0.09)
        msg = client.recv(1024)
        broadcast(msg.decode(encoding), client)


def server():
    while True:
        clientsocket, address = s.accept()
        connections.append(clientsocket)
        print(f"{address} connected to server!")
        broadcast(f"{address} connected to server!", "no")
        time.sleep(0.09)
        threading.Thread(target=recieve_message, args=[clientsocket]).start()
        time.sleep(0.09)


if __name__ == "__main__":
    server()