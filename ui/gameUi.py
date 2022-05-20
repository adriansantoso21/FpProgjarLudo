import pygame
pygame.init()

def setWindow():
    global screen
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Ludo Board Game")
    iconLogo = pygame.image.load("../asset/img/gameIcon.jpg")
    pygame.display.set_icon(iconLogo)

def setBackground():
    background = pygame.image.load("../asset/img/gameBg.jpg")
    background = pygame.transform.scale(background, (1200, 700))
    screen.blit(background, (0,0))

def setPlayerIcon():
    iconLogo1 = pygame.image.load("../asset/img/playerIcon/icon1.png")
    iconLogo1 = pygame.transform.scale(iconLogo1, (200, 200))
    iconLogo2 = pygame.image.load("../asset/img/playerIcon/icon2.png")
    iconLogo2 = pygame.transform.scale(iconLogo2, (200, 200))
    iconLogo3 = pygame.image.load("../asset/img/playerIcon/icon3.png")
    iconLogo3 = pygame.transform.scale(iconLogo3, (200, 200))
    iconLogo4 = pygame.image.load("../asset/img/playerIcon/icon4.png")
    iconLogo4 = pygame.transform.scale(iconLogo4, (200, 200))
    screen.blit(iconLogo1, (25, 460))
    screen.blit(iconLogo2, (25, 40))
    screen.blit(iconLogo3, (975, 40))
    screen.blit(iconLogo4, (975, 460))

setWindow()
running = True
while running:
    setBackground()
    setPlayerIcon()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    pygame.display.update()