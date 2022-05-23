import pygame
from data.playerGameData import playersGame
import socket
pygame.init()

def setWindow():
    pygame.display.set_caption("Ludo Board Game")
    iconLogo = pygame.image.load("../asset/img/gameIcon.jpg")
    pygame.display.set_icon(iconLogo)

def setBackground():
    background = pygame.image.load("../asset/img/gameBg.jpg")
    background = pygame.transform.scale(background, (1450, 700))
    screen.blit(background, (0,0))

def setPlayerComponent():
    for player in players:
        #setIcon
        iconLogo = pygame.image.load(player.iconLogo)
        iconLogo = pygame.transform.scale(iconLogo, (175, 175))
        screen.blit(iconLogo, player.iconPosition)

        #setName
        font = pygame.font.Font('freesansbold.ttf', 24)
        name = font.render(player.name, True, textColor)
        screen.blit(name, player.namePosition)

        #setDice
        dice = "../asset/img/dice/dice" + str(player.diceNumber) + ".png"
        dice = pygame.image.load(dice)
        dice = pygame.transform.scale(dice, (60,60))
        screen.blit(dice, player.dicePosition)

def setRollDiceButton():
    buttonColor = (232, 55, 76)
    pygame.draw.rect(screen, buttonColor, rollDiceButton, border_radius = 25)

    text = pygame.font.Font('freesansbold.ttf', 24)
    buttonText = text.render('Roll Dice !', True, textColor)
    screen.blit(buttonText, (1155, 610))

def setBoard():
    boardImage = pygame.image.load("../asset/img/board.jpg")
    boardImage = pygame.transform.scale(boardImage, (600, 600))
    screen.blit(boardImage, (210, 50))

def setPawn():
    yellowPawnImage = pygame.image.load("../asset/img/Pawn/yellowPawn.png")
    yellowPawnImage = pygame.transform.scale(yellowPawnImage, (20, 33))
    screen.blit(yellowPawnImage, (466,599))
    pawnList_yellow = [(276, 295), (314, 295), (352, 295), (390, 295), (428, 295),
                       (466, 257), (466, 219), (466, 181), (466, 143), (466, 105), (466, 67), (504, 67), (542, 67),
                       (542, 105), (542, 143), (542, 181), (542, 219), (542, 257),
                       (580, 295), (618, 295), (656, 295), (694, 295), (732, 295), (770, 295), (770, 333), (770, 371),
                       (732, 371), (694, 371), (656, 371), (618, 371), (580, 371),
                       (542, 409), (542, 447), (542, 485), (542, 523), (542, 561), (542, 599), (504, 599), (466, 599),
                       (466, 561), (466, 523), (466, 485), (466, 447), (466, 409),
                       (428, 371), (390, 371), (352, 371), (314, 371), (276, 371), (238, 371), (238, 333), (238, 295)]

    greenPawnImage = pygame.image.load("../asset/img/Pawn/greenPawn.png")
    greenPawnImage = pygame.transform.scale(greenPawnImage, (20, 33))
    screen.blit(greenPawnImage, (466,599))
    pawnList_green   = [(542, 105), (542, 143), (542, 181), (542, 219), (542, 257),
                       (580, 295), (618, 295), (656, 295), (694, 295), (732, 295), (770, 295), (770, 333), (770, 371),
                       (732, 371), (694, 371), (656, 371), (618, 371), (580, 371),
                       (542, 409), (542, 447), (542, 485), (542, 523), (542, 561), (542, 599), (504, 599), (466, 599),
                       (466, 561), (466, 523), (466, 485), (466, 447), (466, 409),
                       (428, 371), (390, 371), (352, 371), (314, 371), (276, 371), (238, 371), (238, 333), (238, 295),
                       (276, 295), (314, 295), (352, 295), (390, 295), (428, 295),
                       (466, 257), (466, 219), (466, 181), (466, 143), (466, 105), (466, 67), (504, 67), (542, 67)]

    redPawnImage = pygame.image.load("../asset/img/Pawn/redPawn.png")
    redPawnImage = pygame.transform.scale(redPawnImage, (20, 33))
    screen.blit(redPawnImage, (466,599))
    pawnList_red     = [(732, 371), (694, 371), (656, 371), (618, 371), (580, 371),
                       (542, 409), (542, 447), (542, 485), (542, 523), (542, 561), (542, 599), (504, 599), (466, 599),
                       (466, 561), (466, 523), (466, 485), (466, 447), (466, 409),
                       (428, 371), (390, 371), (352, 371), (314, 371), (276, 371), (238, 371), (238, 333), (238, 295),
                       (276, 295), (314, 295), (352, 295), (390, 295), (428, 295),
                       (466, 257), (466, 219), (466, 181), (466, 143), (466, 105), (466, 67), (504, 67), (542, 67),
                       (542, 105), (542, 143), (542, 181), (542, 219), (542, 257),
                       (580, 295), (618, 295), (656, 295), (694, 295), (732, 295), (770, 295), (770, 333), (770, 371)]

    bluePawnImage = pygame.image.load("../asset/img/Pawn/bluePawn.png")
    bluePawnImage = pygame.transform.scale(bluePawnImage, (20, 33))
    screen.blit(bluePawnImage, (466,599))
    pawnList_blue   = [(466, 561), (466, 523), (466, 485), (466, 447), (466, 409),
                       (428, 371), (390, 371), (352, 371), (314, 371), (276, 371), (238, 371), (238, 333), (238, 295),
                       (276, 295), (314, 295), (352, 295), (390, 295), (428, 295),
                       (466, 257), (466, 219), (466, 181), (466, 143), (466, 105), (466, 67), (504, 67), (542, 67),
                       (542, 105), (542, 143), (542, 181), (542, 219), (542, 257),
                       (580, 295), (618, 295), (656, 295), (694, 295), (732, 295), (770, 295), (770, 333), (770, 371),
                       (732, 371), (694, 371), (656, 371), (618, 371), (580, 371),
                       (542, 409), (542, 447), (542, 485), (542, 523), (542, 561), (542, 599), (504, 599), (466, 599)]

def setChatBox():
    #draw the chatBox container
    chatBoxContainer = pygame.image.load("../asset/img/chatBg.jpg")
    chatBoxContainer = pygame.transform.scale(chatBoxContainer, (350, 515))
    screen.blit(chatBoxContainer, (1040, 50))

    #set text for textUser input
    text = pygame.font.Font(None, 24)
    textChatBox = text.render(textChat, True, textColor)

    #draw the textAreaContainer and textUser input
    pygame.draw.rect(screen, textAreaColor, textAreaRect)
    screen.blit(textChatBox, (textAreaRect.x + 57.5, textAreaRect.y + 17.5))

    #draw the userIcon
    iconLogoPlayerTurn = pygame.image.load("../asset/img/playerIcon/icon1.png")
    iconLogoPlayerTurn = pygame.transform.scale(iconLogoPlayerTurn, (50, 50))
    screen.blit(iconLogoPlayerTurn, (1045, 515))

    pygame.display.update()

def decidePlayerTurn(firstTime):
    if firstTime:
        if counterTurn < 4:
            client_socket.send("getDiceNumber".encode())
            diceNumber = client_socket.recv(1024).decode()
            players[counterTurn].diceNumber = diceNumber
            maxDiceNumber[counterTurn] = int(diceNumber)
        if counterTurn == 3:
            sameMaxNumberIndex = []
            maxValue = max(maxDiceNumber)
            for index, value in enumerate(maxDiceNumber):
                if value == maxValue: sameMaxNumberIndex.append(index + 1)
            return min(sameMaxNumberIndex)

def main():
    #declare global variable
    global server_address, client_socket
    global gameRunning, screen, rollDiceButton, textColor, colorInactive
    global colorActive, textAreaColor, textAreaActive, textChat, textAreaRect
    global firstTime, player1, player2, player3, player4, players, turn, counterTurn, maxDiceNumber
    gameRunning = True
    screen = pygame.display.set_mode((1450, 700))
    rollDiceButton = pygame.Rect(1115, 595, 200, 50)
    textColor = (255, 255, 255)
    colorInactive = (156, 121, 99)
    colorActive = (93, 73, 60)
    textAreaColor = colorInactive
    textAreaActive = False
    textChat = ''
    textAreaRect = pygame.Rect(1040, 515, 350, 50)
    firstTime = True
    turn = [1, 2, 3, 4]
    counterTurn = -1
    maxDiceNumber = [1, 1, 1, 1]

    while gameRunning:
        server_address = ('localhost', 5000)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(server_address)
        setWindow()
        setBackground()
        setPlayerComponent()
        setRollDiceButton()
        setBoard()
        setPawn()
        setChatBox()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: gameRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if textAreaRect.collidepoint(event.pos):
                    textAreaActive = not textAreaActive
                if rollDiceButton.collidepoint(event.pos):
                    counterTurn += 1
                    #to decide order turn
                    if counterTurn < 4:
                        resultTurn = decidePlayerTurn(True)
                        if resultTurn == 1: turn = [1, 2, 3, 4]
                        elif resultTurn == 2: turn = [2, 3, 4, 1]
                        elif resultTurn == 3: turn = [3, 4, 1, 2]
                        elif resultTurn == 4: turn = [4, 1, 2, 3]
                        print(turn)

                if not textAreaRect.collidepoint(event.pos):
                    textAreaActive = False
                if textAreaActive: textAreaColor = colorActive
                else: textAreaColor = colorInactive
            if event.type == pygame.KEYDOWN:
                if textAreaActive:
                    if event.key == pygame.K_RETURN:
                        textChat = ""
                    elif event.key == pygame.K_BACKSPACE:
                        textChat = textChat[:-1]
                    else:
                        textChat += event.unicode

        pygame.display.update()