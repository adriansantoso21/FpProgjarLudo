import pygame
from ui import regisUi
pygame.init()

def setWindow():
    pygame.display.set_caption("Ludo Board Game")
    iconLogo = pygame.image.load("../asset/img/gameIcon.jpg")
    pygame.display.set_icon(iconLogo)

def setBackground():
    background = pygame.image.load("../asset/img/homeBg.jpg")
    background = pygame.transform.scale(background, (1450, 700))
    screen.blit(background, (0,0))

def setTitle():
    font = pygame.font.Font('freesansbold.ttf', 48)
    titleFont = font.render('Ludo Board Game', True, textColor)
    screen.blit(titleFont, (500, 50))

def setImageIcon():
    imageIcon = pygame.image.load("../asset/img/gameIcon.jpg")
    imageIcon = pygame.transform.scale(imageIcon, (400, 400))
    screen.blit(imageIcon, (300, 175))

def setPlayButton():
    buttonColor = (2, 188, 111)
    pygame.draw.rect(screen, buttonColor, playButton, border_radius=25)

    buttonText = text.render('Play !', True, textColor)
    screen.blit(buttonText, (860, 237.5))

def setRuleButton():
    buttonColor = (1, 86, 213)
    pygame.draw.rect(screen, buttonColor, ruleButton, border_radius=25)

    buttonText = text.render('Rule', True, textColor)
    screen.blit(buttonText, (865, 362.5))

def setExitButton():
    buttonColor = (232, 55, 76)
    pygame.draw.rect(screen, buttonColor, exitButton, border_radius=25)

    buttonText = text.render('Exit', True, textColor)
    screen.blit(buttonText, (867.5, 487.5))

#declare global variable
gameRunning = True
screen = pygame.display.set_mode((1450, 700))
textColor = (255, 255, 255)
text = pygame.font.Font('freesansbold.ttf', 28)
playButton = pygame.Rect(800, 225, 200, 50)
ruleButton = pygame.Rect(800, 350, 200, 50)
exitButton = pygame.Rect(800, 475, 200, 50)

setWindow()
while gameRunning:
    setBackground()
    setTitle()
    setImageIcon()
    setPlayButton()
    setRuleButton()
    setExitButton()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: gameRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if playButton.collidepoint(event.pos):
                gameRunning = False
                regisUi.main()
            elif exitButton.collidepoint(event.pos): gameRunning = False

    pygame.display.update()