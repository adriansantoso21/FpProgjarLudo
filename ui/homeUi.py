import pygame
pygame.init()

gameRunning = True
screen = pygame.display.set_mode((1450, 700))

def setWindow():
    pygame.display.set_caption("Ludo Board Game")
    iconLogo = pygame.image.load("../asset/img/gameIcon.jpg")
    pygame.display.set_icon(iconLogo)

def setBackground():
    background = pygame.image.load("../asset/img/gameBg.jpg")
    background = pygame.transform.scale(background, (1450, 700))
    screen.blit(background, (0,0))

def setTitle():
    titleColor = (255, 227, 169)
    font = pygame.font.Font('freesansbold.ttf', 48)
    titleFont = font.render('Ludo Board Game', True, titleColor)
    screen.blit(titleFont, (500, 50))

def setImageIcon():
    imageIcon = pygame.image.load("../asset/img/gameIcon.jpg")
    imageIcon = pygame.transform.scale(imageIcon, (400, 400))
    screen.blit(imageIcon, (150, 175))

# def setPlayButton():
#
# def setRuleButton():
#
# def setExitButton():

setWindow()
while gameRunning:
    setBackground()
    setTitle()
    setImageIcon()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: gameRunning = False
    pygame.display.update()