import socket


HOST = "127.0.0.1"
PORT = 6969
encoding = "utf-8"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


def recieving_messages(socket_instance):
    while True:
        msg = socket_instance.recv(1024)
        if msg:
            print(msg.decode())
        else:
            connection.close()
            break


def client():
    threading.Thread(target=recieving_messages, args=[s]).start()
    print('Connected to chat!')

    while True:
        msg = input()
        
        if msg == 'quit':
                break

        socket_instance.send(bytes(msg, encoding))

    socket_instance.close()


if __name__ == "__name__":
    client()