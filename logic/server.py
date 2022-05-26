import socket
import sys
import random

server_address = ('localhost', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)

orderRegis = [1, 2, 3, 4]

def getDiceNumber():
    number = random.randint(1, 6)
    return number

def getOrderRegis():
    order = orderRegis[0]
    return order

try:
    while True:
        client_socket, client_address = server_socket.accept()
        command = client_socket.recv(1024).decode()
        result = ""

        if command == "getDiceNumber":
            result = str(getDiceNumber())

        if command == "getOrderRegis":
            result = str(getOrderRegis())

        client_socket.send(result.encode())
        client_socket.close()

except KeyboardInterrupt:
    client_socket.close()
    server_socket.close()
    sys.exit(0)