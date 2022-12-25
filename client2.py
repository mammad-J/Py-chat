import socket
import threading

HOST = '127.0.0.1'
PORT = 6969
encoding = "utf-8"


def receiving_messages(connection):
    while True:
        msg = connection.recv(1024)
        if msg:
            print(msg.decode(encoding))
        else:
            connection.close()
            break


def client():
    socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_instance.connect((HOST, PORT))
    print('[+] Connected to server!')
    threading.Thread(target=receiving_messages, args=[socket_instance])
    while True:
        msg = input()

        if msg == 'quit':
            break

        socket_instance.send(bytes(msg, encoding))


if __name__ == "__main__":
    client()
