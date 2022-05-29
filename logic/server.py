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

def getPlayersGameData():
    return playersGame

def getDiceNumber():
    number = random.randint(1, 6)
    return number

def decidePlayerTurn(data):
    global counterTurn, firstOrder, maxDiceNumber, turn
    counterTurn += 1
    order = int(data[0])
    diceNumber = int(data[1])

    if counterTurn <= 4:
        playersGame[order].diceNumber = diceNumber
        maxDiceNumber[order] = int(diceNumber)

    if counterTurn == 4:
        sameMaxNumberIndex = []
        maxValue = max(maxDiceNumber)
        for index, value in enumerate(maxDiceNumber):
            if value == maxValue: sameMaxNumberIndex.append(index + 1)
        firstOrder = min(sameMaxNumberIndex)
        if firstOrder == 1: turn = [1, 2, 3, 4]
        elif firstOrder == 2: turn = [2, 3, 4, 1]
        elif firstOrder == 3: turn = [3, 4, 1, 2]
        elif firstOrder == 4: turn = [4, 1, 2, 3]
        print(firstOrder)
        print(turn)

try:
    global orderRegis, counterTurn, firstOrder, maxDiceNumber, turn
    orderRegis = [0, 1, 2, 3]
    counterTurn = 0
    firstOrder = 1
    maxDiceNumber = [1, 1, 1, 1]
    turn = [1, 2, 3, 4]

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

        if command == "getPlayersGameData":
            result = getPlayersGameData()
            result = pickle.dumps(result)
            client_socket.send(result)

        if command == "getDiceNumber":
            result = str(getDiceNumber())
            client_socket.send(result.encode())

        if command == "decidePlayerTurn":
            data = client_socket.recv(2048)
            data = pickle.loads(data)
            decidePlayerTurn(data)

        client_socket.close()

except KeyboardInterrupt:
    client_socket.close()
    server_socket.close()
    sys.exit(0)