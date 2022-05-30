import time
import pygame
import schedule

from logic.client import Client
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
    client = Client()
    playersGame = client.getPlayersGameData("getPlayersGameData")
    for player in playersGame:
        #setIcon
        iconLogo = pygame.image.load(player.iconLogo)
        iconLogo = pygame.transform.scale(iconLogo, (175, 175))
        screen.blit(iconLogo, player.iconPosition)

        #setName
        font = pygame.font.Font('freesansbold.ttf', 24)
        name = font.render(player.name[0:7], True, textColor)
        screen.blit(name, player.namePosition)

        #setDice
        dice = "../asset/img/dice/dice" + str(player.diceNumber) + ".png"
        dice = pygame.image.load(dice)
        dice = pygame.transform.scale(dice, (60,60))
        screen.blit(dice, player.dicePosition)
    pygame.display.update()

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

def setPlayerPawn():
    time.sleep(0.5)
    client = Client()
    playersGame = client.getPlayersGameData("getPlayersGameData")
    counter = 0
    for player in playersGame:
        print("counter")
        print(counter)
        counter += 1
        for pawn in player.pawns:
            pawnImage = pygame.image.load(pawn.image)
            pawnImage = pygame.transform.scale(pawnImage, (20, 33))
            screen.blit(pawnImage, (pawn.xCurrentPos, pawn.yCurrentPos))
    pygame.display.update()

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
    client = Client()
    diceNumber = int(client.getDiceNumber("getDiceNumber"))
    print("ini dice number")
    print(diceNumber)
    client = Client()
    client.decidePlayerTurn("decidePlayerTurn", playerOrder, diceNumber)
    time.sleep(0.5)
    setPlayerComponent()

def updateDiceForMove():
    global sixDiceCounter, diceNumber
    #get dice number
    client = Client()
    diceNumber = int(client.getDiceNumber("getDiceNumber"))

    print("updateDiceForMove")
    print(diceNumber)

    #setPlayerDataDice
    client = Client()
    client.setPlayerGameDataDice("setPlayerGameDataDice", playerOrder, diceNumber)
    setPlayerComponent()

    #check how many consecutive 6 dice
    if diceNumber == 6: sixDiceCounter += 1
    else: sixDiceCounter = 0

def movePawn():
    client = Client()
    playersGame = client.getPlayersGameData("getPlayersGameData")
    currentPlayer = playersGame[playerOrder]
    #check if all the pawn in base
    isAllPawnInBase = True
    for pawn in currentPlayer.pawns:
        if pawn.baseRect != pawn.currentRect:
            isAllPawnInBase = False

    if isAllPawnInBase:
        #if the dice 6
        if diceNumber < 7 :
            print("masuk move Pawn")
            client = Client()
            client.setPlayerGameDataPawn("setPlayerGameDataPawn", playerOrder, pawnPressed, diceNumber)
            setPlayerPawn()
        #if the dice not 6: skip
    # else:
    #elif all the pawn not in base
        #if base pawn -> must get six
        #if not base pawn ok

def main(order):
    #declare global variable
    global gameRunning, screen, rollDiceButton, textColor, colorInactive
    global colorActive, textAreaColor, textAreaActive, textChat, textAreaRect, playersGame
    global firstTime, playerOrder, turn, counterTurn, maxDiceNumber, sixDiceCounter, currentPlayer, pawnPressed, result
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
    client = Client()
    playersGame = client.getPlayersGameData("getPlayersGameData")
    firstTime = True
    playerOrder = order
    sixDiceCounter = 0
    currentPlayer = playersGame[playerOrder]
    pawnPressed = 0
    result = ""

    setWindow()
    setBackground()
    setPlayerComponent()
    setRollDiceButton()
    setBoard()
    setPlayerPawn()
    setChatBox()

    schedule.every(3).seconds.do(setPlayerComponent)
    schedule.every(3).seconds.do(setRollDiceButton)
    schedule.every(3).seconds.do(setPlayerPawn)

    while gameRunning:
        schedule.run_pending()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: gameRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if textAreaRect.collidepoint(event.pos):
                    textAreaActive = not textAreaActive
                if rollDiceButton.collidepoint(event.pos):
                    if firstTime:
                        decidePlayerTurn()
                        firstTime = False
                    else:
                        client = Client()
                        result = client.checkTurn("checkTurn", playerOrder)
                        print("hasil cek turn")
                        print(result)
                        if result == "true":
                            updateDiceForMove()

                #check which pawn in pressed
                if result == "true":
                    client = Client()
                    playersGame = client.getPlayersGameData("getPlayersGameData")
                    currentPlayer = playersGame[playerOrder]
                    for index, pawn in enumerate(currentPlayer.pawns):
                        if pawn.currentRect.collidepoint(event.pos):
                            pawnPressed = index
                            movePawn()

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