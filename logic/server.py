import socket
import sys
import random
import pickle
from data.playerRegisData import playersRegis
from data.playerGameData import playersGame

server_address = ('192.168.0.196', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)

def getOrderRegis():
    order = orderRegis[0]
    orderRegis.pop(0)
    return order

def getPlayerRegisData():
    return playersRegis

def setPlayerGameData(data):
    order = int(data[0])
    name = data[1]
    email = data[2]
    playersGame[order].name = name
    playersGame[order].email = email

def getDiceNumber():
    number = random.randint(1, 6)
    return number

try:
    orderRegis = [0, 1, 2, 3]
    while True:
        client_socket, client_address = server_socket.accept()
        command = client_socket.recv(2048).decode()
        result = ""

        if command == "getOrderRegis":
            result = str(getOrderRegis())
            client_socket.send(result.encode())

        if command == "getPlayersRegisData":
            result = getPlayerRegisData()
            result = pickle.dumps(result)
            client_socket.send(result)
            
        if command == "setPlayerGameData":
            data = client_socket.recv(2048)
            data = pickle.loads(data)
            setPlayerGameData(data)

        if command == "getDiceNumber":
            result = str(getDiceNumber())
            client_socket.send(result.encode())

        client_socket.close()

except KeyboardInterrupt:
    client_socket.close()
    server_socket.close()
    sys.exit(0)