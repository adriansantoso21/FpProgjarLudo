import socket
import pickle
import time
from plyer import notification

class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "26.128.63.26"
        self.port = 5000
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
        except:
            pass

    def getOrderRegis(self, command):
        try:
            self.client.send(str.encode(command))
            data = self.client.recv(4096).decode()
            self.client.close()
            return data
        except socket.error as e:
            print(e)

    def getPlayersRegisData(self, command):
        try:
            self.client.send(str.encode(command))
            #unpickle object
            result = self.client.recv(4096)
            self.client.close()
            result = pickle.loads(result)
            return result
        except socket.error as e:
            print(e)

    def setPlayerGameData(self, command, order, nameTemp, emailTemp):
        try:
            self.client.send(str.encode(command))
            data = [order, nameTemp, emailTemp]
            data = pickle.dumps(data)
            time.sleep(0.5)
            self.client.send(data)
            self.client.close()
        except socket.error as e:
            print(e)

    def getPlayersGameData(self, command):
        try:
            self.client.send(str.encode(command))
            time.sleep(0.1)
            # unpickle object
            result = self.client.recv(4096)
            while (result is None) and (not result) and result == b'':
                self.client.send(str.encode(command))
                time.sleep(0.1)
                # unpickle object
                result = self.client.recv(4096)
            print("Ini result GameData")
            print(result)
            result = pickle.loads(result)
            self.client.close()
            return result
        except socket.error as e:
            print(e)

    def getDiceNumber(self, command):
        try:
            self.client.send(str.encode(command))
            data = self.client.recv(4096).decode()
            notification.notify(title="Ludo Board Game",message="Dice result is " + data,timeout=10)
            self.client.close()
            return data
        except socket.error as e:
            print(e)

    def decidePlayerTurn(self, command, order, diceNumber):
        try:
            self.client.send(str.encode(command))
            time.sleep(0.5)
            data = [order, diceNumber]
            data = pickle.dumps(data)
            self.client.send(data)
            self.client.close()
        except socket.error as e:
            print(e)

    def checkTurn(self, command, order):
        try:
            self.client.send(str.encode(command))
            time.sleep(0.5)
            self.client.send(str.encode(str(order)))
            data = self.client.recv(4096).decode()
            self.client.close()
            return data
        except socket.error as e:
            print(e)

    def setPlayerGameDataDice(self, command, order, diceNumber):
        try:
            self.client.send(str.encode(command))
            data = [order, diceNumber]
            data = pickle.dumps(data)
            time.sleep(0.5)
            self.client.send(data)
            self.client.close()
        except socket.error as e:
            print(e)

    def setPlayerGameDataPawn(self, command, order, pawnPressed, diceNumber):
        try:
            self.client.send(str.encode(command))
            data = [order, pawnPressed, diceNumber]
            data = pickle.dumps(data)
            time.sleep(0.5)
            self.client.send(data)
            self.client.close()
        except socket.error as e:
            print(e)

    def skipPlayerMove(self, command):
        try:
            self.client.send(str.encode(command))
            self.client.close()
        except socket.error as e:
            print(e)

    def checkIfPlayerWin(self, command, order):
        try:
            self.client.send(str.encode(command))
            time.sleep(0.5)
            self.client.send(str.encode(str(order)))
            result = self.client.recv(4096)
            while (result is None ) and (not result) and result == b'':
                self.client.send(str.encode(command))
                time.sleep(0.5)
                self.client.send(str.encode(str(order)))
                result = self.client.recv(4096)
            print("Ini result PlayerWin")
            print(result)
            # default value
            if result == b'':
                result = ["false", "false", "false"]
                result = pickle.dumps(result)
            result = pickle.loads(result)
            self.client.close()
            return result

        except socket.error as e:
            print(e)

    def turnNotif(self, command, order):
        try:
            self.client.send(str.encode(command))
            time.sleep(0.5)
            self.client.send(str.encode(str(order)))
            data = self.client.recv(4096).decode()
            if data == "true": notification.notify(title="Ludo", message="Sekarang giliran Anda!", timeout=10)
            self.client.close()
            return data
        except socket.error as e:
            print(e)
    def sendChat(self, command, order, iconLogo, timeChat, textChat):
        try:
            self.client.send(str.encode(command))
            time.sleep(0.5)
            data = [order, iconLogo, timeChat, textChat]
            data = pickle.dumps(data)
            self.client.send(data)
            self.client.close()
        except socket.error as e:
            print(e)

    def getChats(self, command):
        try:
            self.client.send(str.encode(command))
            result = self.client.recv(4096)
            result = pickle.loads(result)
            self.client.close()
            return result
        except socket.error as e:
            print(e)