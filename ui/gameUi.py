import pygame
import socket
pygame.init()

class player:
    def __init__(self, name, namePosition, email, iconLogo, iconPosition, dice, dicePosition):
        self.name = name
        self.namePosition = namePosition
        self.email = email
        self.iconLogo = iconLogo
        self.iconPosition = iconPosition
        self.dice = dice
        self.dicePosition = dicePosition
        self.diceFirstTime = 1

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
        dice = "../asset/img/dice/dice" + str(player.dice) + ".png"
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

def decidePlayerTurn():
    if firstTime:
        client_socket.send("getDiceNumber".encode())
        diceNumber = client_socket.recv(1024).decode()
        print(diceNumber)

def main(playerNameEmail):
    #declare global variable
    global server_address, client_socket
    global gameRunning, screen, rollDiceButton, textColor, colorInactive
    global colorActive, textAreaColor, textAreaActive, textChat, textAreaRect
    global firstTime, player1, player2, player3, player4, players
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
    player1 = player(
        playerNameEmail[0],
        (65, 650),
        playerNameEmail[1],
        "../asset/img/playerIcon/icon1.png",
        (25, 480),
        1,
        (85, 430)
    )
    player2 = player(
        playerNameEmail[2],
        (65, 25),
        playerNameEmail[3],
        "../asset/img/playerIcon/icon2.png",
        (25, 40),
        1,
        (85, 205)
    )
    player3 = player(
        playerNameEmail[4],
        (860, 25),
        playerNameEmail[5],
        "../asset/img/playerIcon/icon3.png",
        (820, 40),
        1,
        (880, 205)
    )
    player4 = player(
        playerNameEmail[6],
        (860, 650),
        playerNameEmail[7],
        "../asset/img/playerIcon/icon4.png",
        (820, 480),
        1,
        (880, 430)
    )
    players = [player1, player2, player3, player4]

    while gameRunning:
        server_address = ('localhost', 5000)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(server_address)
        setWindow()
        setBackground()
        setPlayerComponent()
        setRollDiceButton()
        setBoard()
        setChatBox()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: gameRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if textAreaRect.collidepoint(event.pos):
                    textAreaActive = not textAreaActive
                if rollDiceButton.collidepoint(event.pos):
                    decidePlayerTurn()
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