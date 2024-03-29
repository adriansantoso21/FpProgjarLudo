import time
import pygame
from pygame import mixer
from datetime import datetime
from logic.client import Client
from ui import shareEmail

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
        counter += 1
        for pawn in player.pawns:
            pawnImage = pygame.image.load(pawn.image)
            pawnImage = pygame.transform.scale(pawnImage, (20, 33))
            screen.blit(pawnImage, (pawn.xCurrentPos, pawn.yCurrentPos))
    pygame.display.update()

def setChatBox():
    global playerChats
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
    iconLogoPlayerTurn = pygame.image.load(currentPlayer.iconLogo)
    iconLogoPlayerTurn = pygame.transform.scale(iconLogoPlayerTurn, (50, 50))
    screen.blit(iconLogoPlayerTurn, (1045, 515))

    #draw the all player Chats
    getChats()

    if playerChats:
        #limit 9 chats
        showChats = []
        if len(playerChats) > 9: showChats = playerChats[-9:]
        else: showChats = playerChats

        playerChats.reverse()

        #iterate all the chats
        for index, chat in enumerate (showChats):
            position = playerChatsPos[int(index)]
            #draw box container
            chatPlayerContainerColor = (93, 73, 60)
            pygame.draw.rect(screen, chatPlayerContainerColor, position, border_radius=25)
            #render icon logo
            iconLogoChat = pygame.image.load(chat.iconLogo)
            iconLogoChat = pygame.transform.scale(iconLogoChat, (35, 35))
            screen.blit(iconLogoChat, (position.x + 15, position.y + 2.5))
            #render name time
            text = pygame.font.Font('freesansbold.ttf', 12)
            nameTimeText = text.render(chat.name + " - " + chat.time, True, textColor)
            screen.blit(nameTimeText, (position.x + 55, position.y + 7.5))
            #rendr textchat
            text = pygame.font.Font('freesansbold.ttf', 12)
            textChatText = text.render(chat.textChat, True, textColor)
            screen.blit(textChatText, (position.x + 55, position.y + 22.5))

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

    print("get dice: " + str(diceNumber))

    #setPlayerDataDice
    client = Client()
    client.setPlayerGameDataDice("setPlayerGameDataDice", playerOrder, diceNumber)
    setPlayerComponent()

    #check if all pawn in base
    client = Client()
    playersGame = client.getPlayersGameData("getPlayersGameData")
    currentPlayer = playersGame[playerOrder]
    # check if all the pawn in base
    isAllPawnInBase = True
    for pawn in currentPlayer.pawns:
        if pawn.baseRect != pawn.currentRect:
            isAllPawnInBase = False

    if isAllPawnInBase:
        if diceNumber != 6:
            print("masuk skip player dari movepawn")
            client = Client()
            client.skipPlayerMove("skipPlayerMove")

    #check how many consecutive 6 dice
    if diceNumber == 6: sixDiceCounter += 1
    else: sixDiceCounter = 0

def movePawn():
    global sixDiceCounter, result
    if sixDiceCounter == 3:
        #if get 6 dice will skip player move
        client = Client()
        client.skipPlayerMove("skipPlayerMove")
        sixDiceCounter = 0
        return
    client = Client()
    playersGame = client.getPlayersGameData("getPlayersGameData")
    currentPlayer = playersGame[playerOrder]
    #check if all the pawn in base
    isAllPawnInBase = True
    for pawn in currentPlayer.pawns:
        if pawn.baseRect != pawn.currentRect:
            isAllPawnInBase = False

    if isAllPawnInBase:
        #if the dice 6, if not 6 skip
        if diceNumber == 6:
            client = Client()
            client.setPlayerGameDataPawn("setPlayerGameDataPawn", playerOrder, pawnPressed, 6)
            setPlayerPawn()
            setPawnMovedSound()
        else:
            print("masuk skip player dari movepawn")
            client = Client()
            client.skipPlayerMove("skipPlayerMove")
    else:
        if currentPlayer.pawns[pawnPressed].baseRect == currentPlayer.pawns[pawnPressed].currentRect:
            if diceNumber == 6:
                client = Client()
                client.setPlayerGameDataPawn("setPlayerGameDataPawn", playerOrder, pawnPressed, diceNumber)
                setPawnMovedSound()
        else:
            client = Client()
            client.setPlayerGameDataPawn("setPlayerGameDataPawn", playerOrder, pawnPressed, diceNumber)
            setPawnMovedSound()

def checkIfPlayerWin():
    client = Client()
    results = client.checkIfPlayerWin("checkIfPlayerWin", playerOrder)
    #not win
    for result in results:
        if result == "false": return
    # if len(results) == 1: return

    winPosition = results[1]
    emailPlayer = results[2]
    shareEmail.main(winPosition, emailPlayer)

def setRollDiceSound():
    mixer.init()
    mixer.music.load("../asset/song/rollDice.mp3")
    mixer.music.set_volume(1)
    mixer.music.play()

def setPawnMovedSound():
    mixer.init()
    mixer.music.load("../asset/song/pawnMoved.mp3")
    mixer.music.set_volume(1)
    mixer.music.play()

def setChangePlayerAndChatSound():
    mixer.init()
    mixer.music.load("../asset/song/changePlayerAndChat.mp3")
    mixer.music.set_volume(0.5)
    mixer.music.play()

def getChats():
    global playerChats
    client = Client()
    playerChats = client.getChats("getChats")

def main(order):
    #declare global variable
    global gameRunning, screen, rollDiceButton, textColor, colorInactive
    global colorActive, textAreaColor, textAreaActive, textChat, textAreaRect, playersGame
    global firstTime, playerOrder, turn, counterTurn, maxDiceNumber, sixDiceCounter, currentPlayer, pawnPressed, result, playerChats, playerChatsPos
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
    playerChats = []
    playerChatsPos = [
        pygame.Rect(1060, 460, 315, 40),
        pygame.Rect(1060, 410, 315, 40),
        pygame.Rect(1060, 360, 315, 40),
        pygame.Rect(1060, 310, 315, 40),
        pygame.Rect(1060, 260, 315, 40),
        pygame.Rect(1060, 210, 315, 40),
        pygame.Rect(1060, 160, 315, 40),
        pygame.Rect(1060, 110, 315, 40),
        pygame.Rect(1060, 60, 315, 40),
    ]

    setWindow()
    setBackground()
    setPlayerComponent()
    setRollDiceButton()
    setBoard()
    setPlayerPawn()
    setChatBox()

    while gameRunning:
        # setBackground()
        setPlayerComponent()
        # setRollDiceButton()
        setBoard()
        setPlayerPawn()
        setChatBox()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: gameRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if textAreaRect.collidepoint(event.pos):
                    textAreaActive = not textAreaActive
                if rollDiceButton.collidepoint(event.pos):
                    if firstTime:
                        decidePlayerTurn()
                        firstTime = False
                        #fix name stack on top
                        setBackground()
                        setRollDiceSound()
                        setRollDiceButton()
                        setChatBox()
                    else:
                        time.sleep(0.5)
                        client = Client()
                        result = client.checkTurn("checkTurn", playerOrder)
                        print("hasil cek turn: " + result)
                        if result == "true":
                            setRollDiceSound()
                            updateDiceForMove()

                #check which pawn in pressed
                if result == "true":
                    client = Client()
                    playersGame = client.getPlayersGameData("getPlayersGameData")
                    currentPlayer = playersGame[playerOrder]
                    for index, pawn in enumerate(currentPlayer.pawns):
                        if pawn.currentRect.collidepoint(event.pos):
                            if pawn.currentRect != pawn.homeRect:
                                pawnPressed = index
                                movePawn()
                                checkIfPlayerWin()

                if not textAreaRect.collidepoint(event.pos):
                    textAreaActive = False
                if textAreaActive: textAreaColor = colorActive
                else: textAreaColor = colorInactive
            if event.type == pygame.KEYDOWN:
                if textAreaActive:
                    if event.key == pygame.K_RETURN:
                        client = Client()
                        now = datetime.now()
                        current_time = now.strftime("%H:%M")
                        client.sendChat("sendChat", currentPlayer.name, currentPlayer.iconLogo, current_time, textChat)
                        textChat = ""
                    elif event.key == pygame.K_BACKSPACE:
                        textChat = textChat[:-1]
                    else:
                        textChat += event.unicode
        
        client = Client()
        client.turnNotif("turnNotif", playerOrder)
        pygame.display.update()