import pygame
pygame.init()

def setWindow():
    pygame.display.set_caption("Ludo Board Game")
    iconLogo = pygame.image.load("../asset/img/gameIcon.jpg")
    pygame.display.set_icon(iconLogo)

def setBackground():
    background = pygame.image.load("../asset/img/gameBg.jpg")
    background = pygame.transform.scale(background, (1450, 700))
    screen.blit(background, (0,0))

def setPlayerIcon():
    iconLogo1 = pygame.image.load("../asset/img/playerIcon/icon1.png")
    iconLogo1 = pygame.transform.scale(iconLogo1, (175, 175))
    iconLogo2 = pygame.image.load("../asset/img/playerIcon/icon2.png")
    iconLogo2 = pygame.transform.scale(iconLogo2, (175, 175))
    iconLogo3 = pygame.image.load("../asset/img/playerIcon/icon3.png")
    iconLogo3 = pygame.transform.scale(iconLogo3, (175, 175))
    iconLogo4 = pygame.image.load("../asset/img/playerIcon/icon4.png")
    iconLogo4 = pygame.transform.scale(iconLogo4, (175, 175))
    screen.blit(iconLogo1, (25, 480))
    screen.blit(iconLogo2, (25, 40))
    screen.blit(iconLogo3, (820, 40))
    screen.blit(iconLogo4, (820, 480))

def setPlayerNameEmail():
    font = pygame.font.Font('freesansbold.ttf', 24)
    player1 = font.render(playerName1, True, textColor)
    player2 = font.render(playerName2, True, textColor)
    player3 = font.render(playerName3, True, textColor)
    player4 = font.render(playerName4, True, textColor)
    screen.blit(player1, (65, 650))
    screen.blit(player2, (65, 25))
    screen.blit(player3, (860, 25))
    screen.blit(player4, (860, 650))

def setDice():
    player1Dice = "../asset/img/dice/dice" + str(dicePlayer1) + ".png"
    player2Dice = "../asset/img/dice/dice" + str(dicePlayer2) + ".png"
    player3Dice = "../asset/img/dice/dice" + str(dicePlayer3) + ".png"
    player4Dice = "../asset/img/dice/dice" + str(dicePlayer4) + ".png"

    player1DiceImg = pygame.image.load(player1Dice)
    player1DiceImg = pygame.transform.scale(player1DiceImg, (60, 60))
    player2DiceImg = pygame.image.load(player2Dice)
    player2DiceImg = pygame.transform.scale(player2DiceImg, (60, 60))
    player3DiceImg = pygame.image.load(player3Dice)
    player3DiceImg = pygame.transform.scale(player3DiceImg, (60, 60))
    player4DiceImg = pygame.image.load(player4Dice)
    player4DiceImg = pygame.transform.scale(player4DiceImg, (60, 60))

    screen.blit(player1DiceImg, (85, 430))
    screen.blit(player2DiceImg, (85, 205))
    screen.blit(player3DiceImg, (880, 205))
    screen.blit(player4DiceImg, (880, 430))

    rollDiceButton = pygame.Rect(1115, 595, 200, 50)
    buttonColor = (232, 55, 76)
    pygame.draw.rect(screen, buttonColor, rollDiceButton, border_radius = 25)

    text = pygame.font.Font('freesansbold.ttf', 24)
    buttonText = text.render('Roll Dice !', True, textColor)
    screen.blit(buttonText, (1155, 610))

def setBoard():
    xPos = 210
    yPos = 50
    xSize = 600
    ySize = 600
    pygame.draw.rect(screen, (255, 255, 255), (xPos, yPos, xSize, ySize))

def setChatBox():
    chatBoxContainer = pygame.image.load("../asset/img/chatBg.jpg")
    chatBoxContainer = pygame.transform.scale(chatBoxContainer, (350, 515))
    screen.blit(chatBoxContainer, (1040, 50))

    text = pygame.font.Font(None, 24)
    textChatBox = text.render(textChat, True, textColor)

    #Draw the rectangle and text User input
    pygame.draw.rect(screen, textAreaColor, textAreaRect)
    screen.blit(textChatBox, (textAreaRect.x + 57.5, textAreaRect.y + 17.5))

    #Draw the userIcon
    iconLogoPlayerTurn = pygame.image.load("../asset/img/playerIcon/icon1.png")
    iconLogoPlayerTurn = pygame.transform.scale(iconLogoPlayerTurn, (50, 50))
    screen.blit(iconLogoPlayerTurn, (1045, 515))

    pygame.display.update()

def main(playerNameEmail):
    #declare global variable
    global gameRunning, screen, dicePlayer1, dicePlayer2, dicePlayer3, dicePlayer4, textColor, colorInactive
    global colorActive, textAreaColor, textAreaActive, textChat, textAreaRect
    global playerName1, playerEmail1, playerName2, playerEmail2, playerName3, playerEmail3, playerName4, playerEmail4
    gameRunning = True
    screen = pygame.display.set_mode((1450, 700))
    dicePlayer1 = dicePlayer2 = dicePlayer3 = dicePlayer4 = 1
    textColor = (255, 255, 255)
    colorInactive = (156, 121, 99)
    colorActive = (93, 73, 60)
    textAreaColor = colorInactive
    textAreaActive = False
    textChat = ''
    textAreaRect = pygame.Rect(1040, 515, 350, 50)
    playerName1 = playerNameEmail[0]; playerEmail1 = playerNameEmail[1]
    playerName2 = playerNameEmail[2]; playerEmail2 = playerNameEmail[3]
    playerName3 = playerNameEmail[4]; playerEmail3 = playerNameEmail[5]
    playerName4 = playerNameEmail[6]; playerEmail4 = playerNameEmail[7]

    while gameRunning:
        setWindow()
        setBackground()
        setPlayerIcon()
        setPlayerNameEmail()
        setDice()
        setBoard()
        setChatBox()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: gameRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if textAreaRect.collidepoint(event.pos):
                    textAreaActive = not textAreaActive
                if not textAreaRect.collidepoint(event.pos):
                    textAreaActive = False
                if textAreaActive: textAreaColor = colorActive
                else: textAreaColor = colorInactive
            if event.type == pygame.KEYDOWN:
                if textAreaActive:
                    if event.key == pygame.K_RETURN:
                        print(textChat)
                        textChat = ""
                        # TODO: add the logic soon
                    elif event.key == pygame.K_BACKSPACE:
                        textChat = textChat[:-1]
                    else:
                        textChat += event.unicode

        pygame.display.update()