import socket
import sys

def main(command):
    server_address = ('localhost', 5000)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(5)

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            client_socket.send(command.encode())

            data = client_socket.recv(1024).decode()
            return data
            print(str(data))
            client_socket.close()

    except KeyboardInterrupt:
        server_socket.close()
        sys.exit(0)