import socket
import threading


HOST = "127.0.0.1"
PORT = 6969
encoding = "utf-8"
connections = []


def receive_messages(clientsocket, address):
    while True:
        msg = clientsocket.recv(1024)
        broadcast(msg.decode(encoding), address, clientsocket)


def broadcast(message, address, expectation):
    for client in connections:
        if client == expectation:
            pass
        else:
            msg = str(address) + ": " + message
            client.send(bytes(msg, encoding))


def welcome(client, address):
    for connection in connections:
        if connection == client:
            pass
        else:
            connection.send(bytes(f"{address} has joined the chat!", encoding))


def server():
    socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_instance.bind((HOST, PORT))
    print("Server is ready!")
    socket_instance.listen(4)

    while True:
        clientsocket, address = socket_instance.accept()
        connections.append(clientsocket)
        print(f"{address} Connected to server!")
        welcome(clientsocket, address)
        threading.Thread(target=receive_messages, args=[clientsocket, address]).start()


if __name__ == "__main__":
    server()
