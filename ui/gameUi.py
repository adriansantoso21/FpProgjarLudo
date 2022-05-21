import pygame
pygame.init()

def setGlobalVariable():
    global screen
    global dicePlayer1
    global dicePlayer2
    global dicePlayer3
    global dicePlayer4
    screen = pygame.display.set_mode((1450, 700))
    dicePlayer1 = 1
    dicePlayer2 = 1
    dicePlayer3 = 1
    dicePlayer4 = 1

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
    playerNameColor = (255, 227, 169)
    font = pygame.font.Font('freesansbold.ttf', 24)
    player1 = font.render('Player1', True, playerNameColor)
    player2 = font.render('Player2', True, playerNameColor)
    player3 = font.render('Player3', True, playerNameColor)
    player4 = font.render('Player4', True, playerNameColor)
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

setGlobalVariable()
setWindow()
running = True
while running:
    setBackground()
    setPlayerIcon()
    setPlayerNameEmail()
    setDice()
    setBoard()
    setChatBox()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    pygame.display.update()