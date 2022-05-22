import pygame
pygame.init()

class PlayerNameEmail:
    def __init__(self, colorInactive, colorActive, nameRect, emailRect):
        self.colorInactive = colorInactive
        self.colorActive = colorActive
        self.nameColor = colorInactive
        self.emailColor = colorInactive
        self.nameActive = False
        self.emailActive = False
        self.name = ""
        self.email = ""
        self.nameRect = nameRect
        self.emailRect = emailRect

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

def setPlayerNameAndEmail():
    for player in players:
        #set text for nameEmail
        text = pygame.font.Font(None, 24)
        name = text.render(player.name, True, textColor)
        email = text.render(player.email, True, textColor)
        #draw nameEmail container
        pygame.draw.rect(screen, player.nameColor, player.nameRect)
        pygame.draw.rect(screen, player.emailColor, player.emailRect)
        #draw nameText and emailText
        screen.blit(name, (player.nameRect.x + 57.5, player.nameRect.y + 17.5))
        screen.blit(email, (player.emailRect.x + 57.5, player.emailRect.y + 17.5))
    pygame.display.update()


def main():
    #declare global variable
    global gameRunning, screen, textColor, player1, player2, player3, player4, players
    gameRunning = True
    screen = pygame.display.set_mode((1450, 700))
    textColor = (255, 255, 255)
    #blue
    player1 = PlayerNameEmail(
        (1, 86, 213),#colorInactive
        (1, 61, 152),#colorActive
        pygame.Rect(152.5, 420, 200, 40),#nameRect
        pygame.Rect(152.5, 480, 200, 40)#emailRect
    )
    #yellow
    player2 = PlayerNameEmail(
        (255, 179, 34),
        (204, 133, 0),
        pygame.Rect(460, 420, 200, 40),
        pygame.Rect(460, 480, 200, 40)
    )
    #green
    player3 = PlayerNameEmail(
        (2, 188, 111),
        (2, 100, 59),
        pygame.Rect(780, 420, 200, 40),
        pygame.Rect(780, 480, 200, 40)
    )
    #red
    player4 = PlayerNameEmail(
        (232, 55, 76),
        (183, 21, 40),
        pygame.Rect(1090, 420, 200, 40),
        pygame.Rect(1090, 480, 200, 40)
    )
    players = [player1, player2, player3, player4]

    while gameRunning:
        setWindow()
        setBackground()
        setTitle()
        setPlayerTitle()
        setPlayerIcon()
        setPlayerNameAndEmail()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: gameRunning = False

        pygame.display.update()