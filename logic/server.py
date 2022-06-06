import socket
import sys
import random
import pickle
from data.playerRegisData import playersRegis
from data.playerGameData import playersGame
from data.pawnSteps import pawnsSteps
from data.chatData import chats
from entity.chat import Chat

server_address = ('localhost', 5000)
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
    number = random.randint(4, 6)
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
        if firstOrder == 1: turn = [0, 1, 2, 3]
        elif firstOrder == 2: turn = [1, 2, 3, 0]
        elif firstOrder == 3: turn = [2, 3, 0, 1]
        elif firstOrder == 4: turn = [3, 0, 1, 2]
        print(firstOrder)
        print(turn)

def checkTurn(data):
    if turn[0] == int(data): return "true"
    else: return "false"

def setPlayerGameDataDice(data):
    order = int(data[0])
    diceNumber = data[1]
    playersGame[order].diceNumber = diceNumber

def setPlayerGameDataPawn(data):
    order = int(data[0])
    pawnPressed = data[1]
    diceNumber = int(data[2])

    if turn[0] != order:
        return

    if diceNumber != 6:
        currentOrder = turn[0]
        turn.pop(0)
        turn.append(currentOrder)
        if currentOrder == 3: notif[0] = 1 #jika turn selesai, mark player dengan turn selanjutnya
        else: notif[currentOrder + 1] = 1

    if playersGame[order].pawns[pawnPressed].currentRect == playersGame[order].pawns[pawnPressed].baseRect:
        if diceNumber == 6: diceNumber = 1

    pawnLen = len(pawnsSteps[order])
    pawnCurrentSteps = playersGame[order].pawns[pawnPressed].currentSteps

    if pawnLen < pawnCurrentSteps + diceNumber:
        pawnCurrentSteps = pawnLen - (pawnCurrentSteps + diceNumber - pawnLen) - 2
    else:
        pawnCurrentSteps += diceNumber

    playersGame[order].pawns[pawnPressed].currentSteps = pawnCurrentSteps
    getNextCoordinate = pawnsSteps[order][pawnCurrentSteps]

    playersGame[order].pawns[pawnPressed].xCurrentPos = getNextCoordinate[0]
    playersGame[order].pawns[pawnPressed].yCurrentPos = getNextCoordinate[1]
    playersGame[order].pawns[pawnPressed].currentRect.x = getNextCoordinate[0]
    playersGame[order].pawns[pawnPressed].currentRect.y = getNextCoordinate[1]

    checkIfTouchOtherPlayerPawn(order)
    checkIfAllPawnInBase(order)

def checkIfTouchOtherPlayerPawn(order):
    for index, opponentPlayer in enumerate(playersGame):
        if index == order: continue
        else:
            for opponentPawn in opponentPlayer.pawns:
                for myPawn in playersGame[order].pawns:
                    if myPawn.currentRect == opponentPawn.currentRect:
                        opponentPawn.xCurrentPos = opponentPawn.xBasePos
                        opponentPawn.yCurrentPos = opponentPawn.yBasePos
                        opponentPawn.currentRect = opponentPawn.baseRect
                        opponentPawn.currentSteps = -1
                        opponentPawn.outFromBase = False
                        opponentPawn.finish = False

def checkIfAllPawnInBase(order):
    allPawnsInHome = True
    for pawn in playersGame[order].pawns:
        if pawn.currentRect != pawn.homeRect:
            allPawnsInHome = False
    #win condition
    if allPawnsInHome:
        currentOrder = turn[0]
        win.append(currentOrder)
        turn.pop(currentOrder)

def skipPlayerMove():
    currentOrder = turn[0]
    turn.pop(0)
    turn.append(currentOrder)
    if currentOrder == 3: #jika turn selesai, mark player dengan turn selanjutnya
        notif[0] = 1
    else: notif[currentOrder + 1] = 1

def turnNotif(data):
    if notif[int(data)] == 1: #jika sudah memberikan notifikasi, balikkan kembali mark menjadi 0 
        notif[int(data)] = 0
        return "true"
    else: return "false"

def checkIfPlayerWin(playerOrder):
    # if len(win) == 0: return ["false"]
    playerOrder = int(playerOrder)
    for order in win:
        if playerOrder == order:
            winPosition = len(win)
            emailPlayer = playersGame[playerOrder].email
            return ["true", winPosition, emailPlayer]

    return ["false", "false", "false"]

def sendChat(data):
    chat = Chat(data[0], data[1], data[2], data[3])
    chats.append(chat)

def getChats():
    playerChats = chats
    return playerChats

try:
    global orderRegis, counterTurn, firstOrder, maxDiceNumber, turn, win, notif
    orderRegis = [0, 1, 2, 3]
    counterTurn = 0
    firstOrder = 1
    maxDiceNumber = [1, 1, 1, 1]
    turn = [0, 1, 2, 3]
    win = []
    notif = [0, 0, 0, 0] #untuk mark player jika perlu diberi notifikasi untuk gerak

    while True:
        client_socket, client_address = server_socket.accept()
        command = client_socket.recv(4096).decode('utf-8', 'ignore')
        result = ""

        if command == "getOrderRegis":
            result = str(getOrderRegis())
            client_socket.send(result.encode())

        if command == "getPlayersRegisData":
            result = getPlayerRegisData()
            result = pickle.dumps(result)
            client_socket.send(result)
            
        if command == "setPlayerGameData":
            data = client_socket.recv(4096)
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
            data = client_socket.recv(4096)
            data = pickle.loads(data)
            decidePlayerTurn(data)

        if command == "checkTurn":
            data = client_socket.recv(4096).decode()
            result = checkTurn(data)
            client_socket.send(result.encode())

        if command == "setPlayerGameDataDice":
            data = client_socket.recv(4096)
            data = pickle.loads(data)
            setPlayerGameDataDice(data)

        if command == "setPlayerGameDataPawn":
            data = client_socket.recv(4096)
            data = pickle.loads(data)
            print("ini data setPlayerGameDataPawn")
            print(data)
            setPlayerGameDataPawn(data)

        if command == "skipPlayerMove":
            skipPlayerMove()

        if command == "checkIfPlayerWin":
            order = client_socket.recv(4096).decode()
            result = checkIfPlayerWin(order)
            result = pickle.dumps(result)
            client_socket.send(result)

        if command == "turnNotif": #command untuk notifikasi gerak/turn, menggunakan data "order"
            data = client_socket.recv(4096).decode()
            result = turnNotif(data)
            client_socket.send(result.encode())

        if command == "sendChat":
            data = client_socket.recv(4096)
            data = pickle.loads(data)
            sendChat(data)

        if command == "getChats":
            result = getChats()
            result = pickle.dumps(result)
            client_socket.send(result)

        client_socket.close()

except KeyboardInterrupt:
    client_socket.close()
    server_socket.close()
    sys.exit(0)