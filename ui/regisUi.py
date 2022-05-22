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

def setTitle():
    font = pygame.font.Font('freesansbold.ttf', 36)
    titleFont = font.render('Enter Your Name & Email', True, textColor)
    screen.blit(titleFont, (500, 40))

def setPlayerTitle():
    font = pygame.font.Font('freesansbold.ttf', 28)
    player1 = font.render('Player1', True, textColor)
    player2 = font.render('Player2', True, textColor)
    player3 = font.render('Player3', True, textColor)
    player4 = font.render('Player4', True, textColor)
    screen.blit(player1, (205.2, 135))
    screen.blit(player2, (516.4, 135))
    screen.blit(player3, (827.6, 135))
    screen.blit(player4, (1138.8, 135))

def setPlayerIcon():
    iconLogo1 = pygame.image.load("../asset/img/playerIcon/icon1.png")
    iconLogo1 = pygame.transform.scale(iconLogo1, (225, 225))
    iconLogo2 = pygame.image.load("../asset/img/playerIcon/icon2.png")
    iconLogo2 = pygame.transform.scale(iconLogo2, (225, 225))
    iconLogo3 = pygame.image.load("../asset/img/playerIcon/icon3.png")
    iconLogo3 = pygame.transform.scale(iconLogo3, (225, 225))
    iconLogo4 = pygame.image.load("../asset/img/playerIcon/icon4.png")
    iconLogo4 = pygame.transform.scale(iconLogo4, (225, 225))
    screen.blit(iconLogo1, (140, 165))
    screen.blit(iconLogo2, (450, 165))
    screen.blit(iconLogo3, (765, 165))
    screen.blit(iconLogo4, (1080, 165))

def main():
    #declare global variable
    global gameRunning, screen, textColor
    gameRunning = True
    screen = pygame.display.set_mode((1450, 700))
    textColor = (255, 255, 255)

    while gameRunning:
        setWindow()
        setBackground()
        setTitle()
        setPlayerTitle()
        setPlayerIcon()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: gameRunning = False

        pygame.display.update()