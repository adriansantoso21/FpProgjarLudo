import socket
import pickle
import time


class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.196"
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
            data = self.client.recv(2048).decode()
            self.client.close()
            return data
        except socket.error as e:
            print(e)

    def getPlayersRegisData(self, command):
        try:
            self.client.send(str.encode(command))
            #unpickle object
            result = self.client.recv(2048)
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
            # unpickle object
            result = self.client.recv(2048)
            result = pickle.loads(result)
            self.client.close()
            return result
        except socket.error as e:
            print(e)

    def getDiceNumber(self, command):
        try:
            self.client.send(str.encode(command))
            data = self.client.recv(2048).decode()
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