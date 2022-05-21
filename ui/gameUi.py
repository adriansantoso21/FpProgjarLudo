import pygame
pygame.init()

def setWindow():
    global screen
    screen = pygame.display.set_mode((1400, 700))
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
    darkBlue = (21, 19, 60)
    font = pygame.font.Font('freesansbold.ttf', 24)
    player1 = font.render('Player1', True, darkBlue)
    player2 = font.render('Player2', True, darkBlue)
    player3 = font.render('Player3', True, darkBlue)
    player4 = font.render('Player4', True, darkBlue)
    screen.blit(player1, (65, 650))
    screen.blit(player2, (65, 25))
    screen.blit(player3, (860, 25))
    screen.blit(player4, (860, 650))

def setBoard():
    xPos = 210
    yPos = 50
    xSize = 600
    ySize = 600
    pygame.draw.rect(screen, (255, 255, 255), (xPos, yPos, xSize, ySize))

setWindow()
running = True
while running:
    setBackground()
    setPlayerIcon()
    setPlayerNameEmail()
    setBoard()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    pygame.display.update()